import sys

sys.path
from PyQt4 import  QtGui
from lib.widgets.gui_elements.gui_setup import *
from lib.widgets import setup_indicators
from lib.widgets.gui_elements import main_Xlive

import getpass





class gui_main_Xlive(QtGui.QMainWindow, main_Xlive.Ui_main_Xlive):
    def __init__(self, parent=None):
        super(gui_main_Xlive, self).__init__(parent)
        self.setupUi(self)
        self.setWidgets()
        self.setStatusbar()
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle('Xlive / NSLS-II ISS beamline/ logged as ' + getpass.getuser())

    def setWidgets(self):
        self.tab_layout_BeamlineStatus.addWidget(gui_tab_BeamlineStatus())
        self.tab_layout_ExperimentDesign.addWidget(gui_tab_ExperimentDesign())


    def setStatusbar(self):

        a=setup_indicators.indicator_BeamCurrent_statusbar()
        self.statusbar_main_Xlive.addPermanentWidget(a, stretch = 2 )


if __name__ == "__main__":
    sys.path
    app = QtGui.QApplication(sys.argv)
    f = gui_main_Xlive()
    f.show()
    app.exec_()