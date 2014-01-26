'''
Created on Jan 8, 2014

@author: elistavitski
'''
from servomotor import ServoMotor

if __name__ == '__main__':
    a=ServoMotor(motor_num=1)
    a.initialize()