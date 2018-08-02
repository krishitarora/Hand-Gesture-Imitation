
#include <Servo.h>

Servo myservo;
Servo myservo1;
Servo myservo2;
Servo myservo3;
Servo myservo4;
// create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
char choice;


void setup() {
  myservo.attach(9);  //Index
  myservo1.attach(8); //Thumb
  myservo2.attach(12); //Little
  myservo3.attach(11);  //Ring
  myservo4.attach(10); // Middle
  Serial.begin(9600);

        myservo.write(180);
        myservo1.write(0);
        myservo2.write(0);
        myservo3.write(0);
        myservo4.write(150);
}

void loop() {


  while (Serial.available())
  {
    choice = Serial.read();
  }

  if (choice == '1') {
    {
      for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
        // in steps of 1 degree
        myservo.write(180);
        myservo1.write(pos);
        myservo2.write(0);
        myservo3.write(0);
        myservo4.write(150);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
        myservo.write(180);
        myservo1.write(pos);
        myservo2.write(0);
        myservo3.write(0);
        myservo4.write(150);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
    }
    choice=0;
  }

  if (choice == '2') {
    {
      for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
        // in steps of 1 degree
        myservo.write(180);
        myservo1.write(pos);
        myservo2.write(pos);
        myservo3.write(0);
        myservo4.write(150);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
        myservo.write(180);
        myservo1.write(pos);
        myservo2.write(pos);
        myservo3.write(0);
        myservo4.write(150);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
    }
    choice=0;
  }

  if (choice == '3') {
    {
      for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
        // in steps of 1 degree
        myservo.write(180);
        myservo1.write(0);
        myservo2.write(pos);
        myservo3.write(pos);
        myservo4.write(150-pos);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
        myservo.write(180);
        myservo1.write(0);
        myservo2.write(pos);
        myservo3.write(pos);
        myservo4.write(150-pos);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
    }
    choice=0;
  }
  if (choice == '4') {
    {
      for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
        // in steps of 1 degree
        myservo.write(180 - pos);
        myservo1.write(pos);
        myservo2.write(pos);
        myservo3.write(pos);
        myservo4.write(150-pos);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
      for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
        myservo.write(180 - pos);
        myservo1.write(pos);
        myservo2.write(pos);
        myservo3.write(pos);
        myservo4.write(150-pos);
        // tell servo to go to position in variable 'pos'
        delay(15);                       // waits 15ms for the servo to reach the position
      }
    }
  choice=0;
  }
}

