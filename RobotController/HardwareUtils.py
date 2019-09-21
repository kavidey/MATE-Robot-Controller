# Import I2C Communication Libraries
from board import SCL, SDA
import busio
from adafruit_motor import servo

# Import the PCA9685 module (16 Motor 12 bit PWM Servo Driver)
from adafruit_pca9685 import PCA9685

settings = {
    "servo_settings": {
        "T100": {
            "min_pulse": 1500,
            "max_pulse": 1900
        }
    }
}

i2c = busio.I2C(SCL, SDA)

class ServoDriver():
    def __init__(servo_locs,frequency=50):
        self.pca = PCA9685(i2c)
        self.pca.frequency = frequency
        self.servos = [None]*16
        for i,(loc,s_type) in enumerate(servo_locs):
            self.servos.append((servo.Servo(pca.channels[loc],
                                           settings["servo_settings"][s_type]["min_pulse"],
                                           settings["servo_settings"][s_type]["max_pulse"]),s_type))
    def set_servo(loc,speed):
        if self.servos[loc]:
            self.servos[loc][0].angle = speed
        else:
            raise Exception("There is no servo at {}".format(loc))

    def set_all_servos(loc, speed, only_type=False):
        for servo,s_type in self.servos:
            if servo and (only_type == False or s_type == only_type):
                servo.angle = speed
    
    def shutdown():
        self.pca.deinit()