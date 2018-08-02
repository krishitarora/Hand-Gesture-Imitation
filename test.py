from __future__ import print_function
#from azure.cognitiveservices.vision.customvision.training import training_api
#from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

import tensorflow as tf
import os

import copy
import math
import requests
import operator
import time
import datetime 


from PIL import Image
import numpy as np
import cv2

''' Code for Arduino

import serial                                 # add Serial library for Serial communication

rial = serial.Serial('com6',9600)             # creates Serial port object, read Serial documentation incase error in port name
print (rial.readline())                       # can comment this line 

'''

def convert_to_opencv(image):
    # RGB -> BGR conversion is performed as well.
    # Gray to RGB
    image = cv2.cvtColor(np.array(image),cv2.COLOR_GRAY2RGB)
    r,g,b = np.array(image).T    
    opencv_image = np.array([b,g,r]).transpose()
    return opencv_image

def crop_center(img,cropx,cropy):
    h, w = img.shape[:2]
    startx = w//2-(cropx//2)
    starty = h//2-(cropy//2)
    return img[starty:starty+cropy, startx:startx+cropx]

def resize_down_to_1600_max_dim(image):
    h, w = image.shape[:2]
    if (h < 1600 and w < 1600):
        return image

    new_size = (1600 * w // h, 1600) if (h > w) else (1600, 1600 * h // w)
    return cv2.resize(image, new_size, interpolation = cv2.INTER_LINEAR)

def resize_to_256_square(image):
    h, w = image.shape[:2]
    return cv2.resize(image, (256, 256), interpolation = cv2.INTER_LINEAR)

def update_orientation(image):
    exif_orientation_tag = 0x0112
    if hasattr(image, '_getexif'):
        exif = image._getexif()
        if (exif != None and exif_orientation_tag in exif):
            orientation = exif.get(exif_orientation_tag, 1)
            # orientation is 1 based, shift to zero based and flip/transpose based on 0-based values
            orientation -= 1
            if orientation >= 4:
                image = image.transpose(Image.TRANSPOSE)
            if orientation == 2 or orientation == 3 or orientation == 6 or orientation == 7:
                image = image.transpose(Image.FLIP_TOP_BOTTOM)
            if orientation == 1 or orientation == 2 or orientation == 5 or orientation == 6:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return image
    
graph_def = tf.GraphDef()
labels = []

# Import the TF graph
with tf.gfile.FastGFile("model16.pb", 'rb') as f:
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')

# Create a list of labels.
with open("labels.txt", 'rt') as lf:
    for l in lf:
        labels.append(l.strip())
    
def classify(time_now):   
    

    # Load from a file
    imageFile = 'pics/'+time_now+".jpg"
    image = Image.open(imageFile)

    # Update orientation based on EXIF tags, if the file has orientation info.
    image = update_orientation(image)

    # Convert to OpenCV format
    image = convert_to_opencv(image)

    # If the image has either w or h greater than 1600 we resize it down respecting
    # aspect ratio such that the largest dimension is 1600
    image = resize_down_to_1600_max_dim(image)

    # We next get the largest center square
    h, w = image.shape[:2]
    min_dim = min(w,h)
    max_square_image = crop_center(image, min_dim, min_dim)

    # Resize that square down to 256x256
    augmented_image = resize_to_256_square(max_square_image)

    # The compact models have a network size of 227x227, the model requires this size.
    network_input_size = 227

    # Crop the center for the specified network_input_Size
    augmented_image = crop_center(augmented_image, network_input_size, network_input_size)

    # These names are part of the model and cannot be changed.
    output_layer = 'loss:0'
    input_node = 'Placeholder:0'

    with tf.Session() as sess:
        prob_tensor = sess.graph.get_tensor_by_name(output_layer)
        predictions, = sess.run(prob_tensor, {input_node: [augmented_image] })

    # Print the highest probability label
        highest_probability_index = np.argmax(predictions)
        print('Classified as: ' + labels[highest_probability_index])
        maxProb = 0
        # Or you can print out all of the results mapping labels to probabilities.
        label_index = 0
        for p in predictions:
            truncated_probablity = np.float64(round(p,8))
            if(truncated_probablity>maxProb):
                maxProb = truncated_probablity
            print (labels[label_index], truncated_probablity)
            label_index += 1
        print('\n\n')
        return([labels[highest_probability_index],maxProb])

# parameters
cap_region_x_begin=0.5  # start point/total width
cap_region_y_end=0.8  # start point/total width
threshold = 60  #  BINARY threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50

# variables
isBgCaptured = 0   # bool, whether the background captured
triggerSwitch = False  # if true, keyborad simulator works
i=0

def printThreshold(thr):
    print("Changed threshold to "+str(thr))


def removeBG(frame):
    fgmask = bgModel.apply(frame, 0 ,0)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res




# Camera
camera = cv2.VideoCapture(0)
camera.set(10,200)

continuous=False

while i<1:
 while camera.isOpened():
    ret, frame = camera.read()
    threshold = cv2.getTrackbarPos('trh1', 'trackbar')
    frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
    frame = cv2.flip(frame, 1)  # flip the frame horizontally
    cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
                 (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
    cv2.imshow('original', frame)

    #  Main operation
    if isBgCaptured == 1:  # this part wont run until background captured
        img = removeBG(frame)
        img = img[0:int(cap_region_y_end * frame.shape[0]),
                    int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]  # clip the ROI
        cv2.imshow('mask', img)


    # Keyboard Input operation
    k = cv2.waitKey(10)
    if k == 27:  # press ESC to exit
        cv2.destroyAllWindows()
        break
    elif k == ord('b'):  # press 'b' to capture the background
        bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
        isBgCaptured = 1
        print ('Background Captured.')
        i=i+1
        continuous=False
    elif((k == ord('s') or continuous) and i!=0):
        if (i==0):
            print ('Please capture Background first.')
        else:
            continuous=True
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            time_now= str(datetime.datetime.now().time()).replace(':', '_').replace('.','_')
            cv2.imwrite('pics/'+time_now+'.jpg', img_gray)
            label, prob = classify(time_now)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_gray, label,(10,350), font, 2,(255,255,255), 2 ,cv2.LINE_AA)
            cv2.imshow('output_c', img_gray)
    elif k == ord('c'):
        if (i==0):
            print ('Please capture Background first.')
        else:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            time_now= str(datetime.datetime.now().time()).replace(':', '_').replace('.','_')
            cv2.imwrite('pics/'+time_now+'.jpg', img_gray) #fix path accordingly
            label, prob = classify(time_now)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img_gray, label,(10,350), font, 2,(255,255,255), 2 ,cv2.LINE_AA)
            cv2.imshow('output', img_gray)
            print("Successfully Classified.")
    elif k == ord('r'):  # press 'r' to reset the background
        bgModel = None
        triggerSwitch = False
        isBgCaptured = 0
        i=0
        print ('Reset Background.')
    elif k == ord('n'):
        triggerSwitch = True
        print ('Trigger On.')
    
    ''' Hand control through Arduino
    elif k == ord('a'):
            print(label)
            if(label=="One"):
                    one='1'
                    rial.write(one.encode())             #send 1 to arduino
                    print ("Robot Hand Performing Gesture: 1")
            elif(label=="Two"):
                    two='2'
                    rial.write(two.encode())             #send 2 to arduino
                    print ("Robot Hand Performing Gesture: 2")
            elif(label=="Okay"):
                    okay='3'
                    rial.write(okay.encode())             #send 3 to arduino
                    print ("Robot Hand Performing Gesture: Okay")
            elif(label=="Five"):
                    five='4'
                    rial.write(five.encode())             #send 4 to arduino
                    print ("Robot Hand Performing Gesture: Five")
    '''                      
    













