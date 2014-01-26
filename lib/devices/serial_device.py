'''
Created on Jan 8, 2014
@author: elistavitski
'''

from epics import pv

class SerialDevice(object):

    _is_simulation=False
    _attr=('AOUT','TINP','OEOS')
    _prefix='asynRecord'
    _init_command_sequence_file='macro.mac'

    def __init__(self, prefix='',):

        if prefix is not '':
            self._prefix=prefix

        pvname_write=self._prefix+'.'+self._attr[0]
        pvname_read=self._prefix+'.'+self._attr[1]
        pvname_terminator=self._prefix+'.'+self._attr[2]
        if not self._is_simulation:
            self._pv_write = pv.PV(pvname_write)
            if  not self._pv_write.connected:
                self._pv_write.wait_for_connection()

            self._pv_read = pv.PV(pvname_read)
            if  not self._pv_read.connected:
                self._pv_read.wait_for_connection()

            self._pv_terminator = pv.PV(pvname_terminator)
            if  not self._pv_terminator.connected:
                self._pv_terminator.wait_for_connection()
            self._pv_terminator.put('\r')

    def write(self, string_to_write=''):
        self._pv_write.put(string_to_write)


    def read(self):
        return self._pv_read.get()




