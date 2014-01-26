'''
Created on Jan 14, 2014

@author: elistavitski
'''
import sys
from PyQt4 import  QtGui
from lib.widgets import widget_setup

class indicator_PVstatus_vertical(widget_setup.gui_indicator_PVstatus_vertical):
    def __init__(self, pv_name=None, pv_value):
        super(gui_tab_ExperimentDesign, self).__init__(parent)
        self.setupUi(self)

