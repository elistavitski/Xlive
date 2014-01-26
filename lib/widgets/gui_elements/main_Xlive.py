# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_Xlive.ui'
#
# Created: Tue Jan 14 21:42:32 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main_Xlive(object):
    def setupUi(self, main_Xlive):
        main_Xlive.setObjectName(_fromUtf8("main_Xlive"))
        main_Xlive.resize(976, 786)
        self.centralwidget_main_Xlive = QtGui.QWidget(main_Xlive)
        self.centralwidget_main_Xlive.setObjectName(_fromUtf8("centralwidget_main_Xlive"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget_main_Xlive)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 951, 711))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_BeamlineStatus = QtGui.QWidget()
        self.tab_BeamlineStatus.setObjectName(_fromUtf8("tab_BeamlineStatus"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_BeamlineStatus)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 661))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.tab_layout_BeamlineStatus = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.tab_layout_BeamlineStatus.setMargin(0)
        self.tab_layout_BeamlineStatus.setObjectName(_fromUtf8("tab_layout_BeamlineStatus"))
        self.tabWidget.addTab(self.tab_BeamlineStatus, _fromUtf8(""))
        self.tab_ExperimentDesign = QtGui.QWidget()
        self.tab_ExperimentDesign.setObjectName(_fromUtf8("tab_ExperimentDesign"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_ExperimentDesign)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 931, 661))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.tab_layout_ExperimentDesign = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.tab_layout_ExperimentDesign.setMargin(0)
        self.tab_layout_ExperimentDesign.setObjectName(_fromUtf8("tab_layout_ExperimentDesign"))
        self.tabWidget.addTab(self.tab_ExperimentDesign, _fromUtf8(""))
        self.tab_DataAcquisition = QtGui.QWidget()
        self.tab_DataAcquisition.setObjectName(_fromUtf8("tab_DataAcquisition"))
        self.tabWidget.addTab(self.tab_DataAcquisition, _fromUtf8(""))
        main_Xlive.setCentralWidget(self.centralwidget_main_Xlive)
        self.menubar_main_Xlive = QtGui.QMenuBar(main_Xlive)
        self.menubar_main_Xlive.setGeometry(QtCore.QRect(0, 0, 976, 29))
        self.menubar_main_Xlive.setObjectName(_fromUtf8("menubar_main_Xlive"))
        self.menuFile = QtGui.QMenu(self.menubar_main_Xlive)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar_main_Xlive)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        main_Xlive.setMenuBar(self.menubar_main_Xlive)
        self.statusbar_main_Xlive = QtGui.QStatusBar(main_Xlive)
        self.statusbar_main_Xlive.setObjectName(_fromUtf8("statusbar_main_Xlive"))
        main_Xlive.setStatusBar(self.statusbar_main_Xlive)
        self.actionExit = QtGui.QAction(main_Xlive)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar_main_Xlive.addAction(self.menuFile.menuAction())
        self.menubar_main_Xlive.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_Xlive)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_Xlive)

    def retranslateUi(self, main_Xlive):
        main_Xlive.setWindowTitle(QtGui.QApplication.translate("main_Xlive", "Xlive", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_BeamlineStatus), QtGui.QApplication.translate("main_Xlive", "Beamline status", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ExperimentDesign), QtGui.QApplication.translate("main_Xlive", "Experiment design", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_DataAcquisition), QtGui.QApplication.translate("main_Xlive", "Data acquisition", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("main_Xlive", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("main_Xlive", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("main_Xlive", "Exit", None, QtGui.QApplication.UnicodeUTF8))

