import RPi.GPIO as GPIO          
from time import sleep

in1 = 23
in2 = 24
enA = 25

enB = 22
in3 = 27
in4 = 17

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.setwarnings(False)

p=GPIO.PWM(enA,1000)
Q = GPIO.PWM(enB,1000)

p.start(50)
Q.start(50)


def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    

def forward(x):
    p.ChangeDutyCycle(x)
    Q.ChangeDutyCycle(x)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("Forward.........")
    sleep(.5)
    stop()

   


def reverse(x):
    p.ChangeDutyCycle(x)
    Q.ChangeDutyCycle(x)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.HIGH)
    print("Reverse.........")
    sleep(.5)
    stop()


def left(x):
    p.ChangeDutyCycle(x)
    Q.ChangeDutyCycle(x)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)  
    print("Left.........")
    sleep(.5)
    stop()
       

def right(x):
    p.ChangeDutyCycle(x)
    Q.ChangeDutyCycle(x)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print("Right.........")
    sleep(.5)
    stop()



forward(30)
sleep(2)
reverse(30)
sleep(2)
left(30)
sleep(2)
right(30)
GPIO.cleanup()