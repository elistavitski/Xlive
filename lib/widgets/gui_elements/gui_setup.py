'''
Created on Jan 5, 2014

@author: elistavitski
'''
from PyQt4 import  QtGui
import widget_BeamlineStatus
import widget_ExperimentDesign
import  indicator_pv_status_vertical, indicator_pv_status_horizontal 


'''
class gui_indicator_pv_status_vertical(QtGui.QWidget,indicator_PVstatus_vertical.Ui_indicator_pv_status_vertical):
    def __init__(self, parent=None):
        super(gui_indicator_PVstatus_vertical, self).__init__(parent)
        self.setupUi(self)

   '''     
class gui_indicator_pv_status_horizontal(QtGui.QWidget,indicator_pv_status_horizontal.Ui_indicator_pv_status_horizontal):
    def __init__(self, parent=None):
        super(gui_indicator_pv_status_horizontal, self).__init__(parent)
        self.setupUi(self)


class gui_tab_BeamlineStatus(QtGui.QWidget,widget_BeamlineStatus.Ui_widget_BeamlineStatus):
    def __init__(self, parent=None):
        super(gui_tab_BeamlineStatus, self).__init__(parent)
        self.setupUi(self)

class gui_tab_ExperimentDesign(QtGui.QWidget,widget_ExperimentDesign.Ui_widget_ExperimentDesign):
    def __init__(self, parent=None):
        super(gui_tab_ExperimentDesign, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.setHeaderHidden(True)