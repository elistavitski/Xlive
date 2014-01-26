'''
Created on Jan 8, 2014
@author: elistavitski
'''

from serial_device import SerialDevice
import time
import sys

class ServoMotor(SerialDevice):
    _init_sequence_file='servomotor.ini'

    def __init__(self, motor_num=None):
        super(ServoMotor,self).__init__()
        if motor_num is None:
            raise Exception('Motor number is not defined')
            pass
        else:
            self._motor_num=motor_num;


    def initialize(self):
        init_file_id=open(self._init_sequence_file,'r')
        init_seq=init_file_id.readlines()
        init_seq_updated=['']*len(init_seq)
        for index, macro_line in enumerate(init_seq):
            num_param=macro_line.count('%s')
            if num_param is 2:
                init_seq_updated[index]=macro_line%(str(self._motor_num),(str(self._motor_num)))
            elif num_param is 1:
                init_seq_updated[index]=macro_line%str(self._motor_num)
            else:
                init_seq_updated[index]=macro_line%(str(self._motor_num),(str(self._motor_num*2+1)),\
                                               (str(self._motor_num*2)),'0','0')
        if self._is_simulation:
            print init_seq_updated
        
        else:
            print 'Initialization in progress...'
            for init_line in init_seq_updated:
                string_to_write=init_line.rstrip('\n')
                self.write(string_to_write)
                feedback=str(self.read())
                while feedback[0:len(string_to_write)]!=string_to_write:
                    time.sleep(0.5)
                    feedback=str(self.read())
                sys.stdout.write('.')
        print 'Initialization complete'

    def move_abs(self, move=0):
        self.write('ma %s %s'%(str(self._motor_num),str(move)))

    def move_rel(self, move=0):
        self.write('mr %s %s'%(str(self._motor_num),str(move)))
