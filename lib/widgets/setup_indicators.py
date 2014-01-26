'''
Created on Jan 14, 2014

@author: elistavitski
'''
from PyQt4 import  QtGui, QtCore
from gui_elements import gui_setup

class indicator_BeamCurrent_statusbar(gui_setup.gui_indicator_pv_status_horizontal):
    def __init__(self,parent=None):
        super(indicator_BeamCurrent_statusbar, self).__init__(parent)
        self.label_pv_name.setText('Beam current')
        self.label_pv_value.setText('0 mA')
        font = QtGui.QFont("Cantarell", 11,QtGui.QFont.Bold )
        self.label_pv_value.setFont(font)
        self.label_pv_value.setStyleSheet("color: rgb(255,0,0)")