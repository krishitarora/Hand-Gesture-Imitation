# Hand Gesture Imitation

This is a project to make a robotic hand imitate hand gestures performed by a human.

## There are 3 files, a .py file, a .pb model and .ino file.

### The .py file contains the Python code for Hand Gesture Classification.
### The .pb file contains the trained model that is imported by the python file.
### The .ino file is the Arduino file used to communicate with and control the Ardiuno Mega placed inside the Robotic Hand.

Large parts of the code are self-explanatory. Comments are added to make it more understandable.

## Pre-processing:

Pre-processing techniques include background subtraction and converting the image to grayscale.

The removeBG function does majority of the pre-processing. Information about the functions can be found in the OpenCV documenatation.

## Result:

The result is classification by the CNN into 4 classes: One, Two, Five, Okay. More classes can be added with ease once training data is available.
The Python file then communicates with the Arduino and the hand gesture is imitated.
The parts of code relating to Arduino in the python file have been commented so that atleast the classifciation part can be run if hardware is unavailable.

## Program flow is as follows:

To capture initial static background, press b.

To get single classification result, press c.

To get continuous classification result, press s.
To stop continuous classification, press b.

To perform imitation by hardware using arduino, press a.

To reset static background, press r.

To close windows, press Esc.

Video Capture of the Gesture Classification is available here:
[linkname](https://youtu.be/TLEVXG2YohI)

## Dependencies:
- click=6.7=py36hec8c647_0
- flask=1.0.2=py36_1
- git=2.16.1=0
- itsdangerous=0.24=py36hb6c5a24_1
- absl-py=0.1.10=py_0
- backcall=0.1.0=py_0
- backports=1.0=py36_1
- backports.weakref=1.0rc1=py36_1
- bleach=1.5.0=py36_0
- boost=1.64.0=py36_vc14_4
- boost-cpp=1.64.0=vc14_1
- certifi=2018.1.18=py36_0
- colorama=0.3.9=py36_0
- decorator=4.2.1=py36_0
- dlib=19.4=np113py36_201
- entrypoints=0.2.3=py36_1
- html5lib=0.9999999=py36_0
- ipykernel=4.8.2=py36_0
- ipython=6.3.0=py36_0
- ipython_genutils=0.2.0=py36_0
- jedi=0.11.1=py36_0
- jinja2=2.10=py36_0
- jsonschema=2.6.0=py36_1
- jupyter_client=5.2.3=py36_0
- jupyter_core=4.4.0=py_0
- libpng=1.6.34=vc14_0
- libprotobuf=3.5.2=vc14_0
- libsodium=1.0.16=vc14_0
- markdown=2.6.11=py_0
- markupsafe=1.0=py36_0
- mistune=0.8.3=py_0
- nb_conda=2.2.1=py36_0
- nb_conda_kernels=2.1.0=py36_0
- nbconvert=5.3.1=py_1
- nbformat=4.4.0=py36_0
- notebook=5.4.1=py36_0
- pandoc=2.1.3=0
- pandocfilters=1.4.1=py36_0
- parso=0.1.1=py_0
- pickleshare=0.7.4=py36_0
- pip=9.0.1=py36_1
- prompt_toolkit=1.0.15=py36_0
- protobuf=3.5.2=py36_vc14_0
- pygments=2.2.0=py36_0
- pyserial=3.4=py36_0
- python=3.6.4=0
- python-dateutil=2.7.2=py_0
- pywinpty=0.5=py36_2
- pyzmq=17.0.0=py36_4
- send2trash=1.5.0=py_0
- setuptools=39.0.1=py36_0
- simplegeneric=0.8.1=py36_0
- six=1.11.0=py36_1
- tensorboard=1.5.1=py36_1
- tensorflow=1.5.0=py36_0
- terminado=0.8.1=py36_0
- testpath=0.3.1=py36_0
- tornado=5.0.1=py36_1
- traitlets=4.3.2=py36_0
- vc=14=0
- vs2008_runtime=9.0.30729.6161=0
- vs2015_runtime=14.0.25420=0
- wcwidth=0.1.7=py36_0
- webencodings=0.5=py36_0
- werkzeug=0.14.1=py_0
- wheel=0.30.0=py36_2
- wincertstore=0.2=py36_0
- winpty=0.4.3=vc14_2
- zeromq=4.2.5=vc14_1
- zlib=1.2.11=vc14_0
- m2w64-gcc-libgfortran=5.3.0=6
- m2w64-gcc-libs=5.3.0=7
- m2w64-gcc-libs-core=5.3.0=7
- m2w64-gmp=6.1.0=2
- m2w64-libwinpthread-git=5.0.0.4634.697f757=2
- mkl=2017.0.3=0
- msys2-conda-epoch=20160418=1
- numpy=1.13.1=py36_0

