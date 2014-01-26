# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indicator_pv_status_vertical.ui'
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

class Ui_indicator_PVstatus_vertical(object):
    def setupUi(self, indicator_PVstatus_vertical):
        indicator_PVstatus_vertical.setObjectName(_fromUtf8("indicator_PVstatus_vertical"))
        indicator_PVstatus_vertical.resize(94, 42)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(indicator_PVstatus_vertical.sizePolicy().hasHeightForWidth())
        indicator_PVstatus_vertical.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        indicator_PVstatus_vertical.setFont(font)
        self.verticalLayoutWidget = QtGui.QWidget(indicator_PVstatus_vertical)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 71, 44))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_PVname = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_PVname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PVname.setObjectName(_fromUtf8("label_PVname"))
        self.verticalLayout.addWidget(self.label_PVname)
        self.label_PVstatus = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_PVstatus.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_PVstatus.sizePolicy().hasHeightForWidth())
        self.label_PVstatus.setSizePolicy(sizePolicy)
        self.label_PVstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PVstatus.setObjectName(_fromUtf8("label_PVstatus"))
        self.verticalLayout.addWidget(self.label_PVstatus)

        self.retranslateUi(indicator_PVstatus_vertical)
        QtCore.QMetaObject.connectSlotsByName(indicator_PVstatus_vertical)

    def retranslateUi(self, indicator_PVstatus_vertical):
        indicator_PVstatus_vertical.setWindowTitle(QtGui.QApplication.translate("indicator_PVstatus_vertical", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_PVname.setText(QtGui.QApplication.translate("indicator_PVstatus_vertical", "PV name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_PVstatus.setText(QtGui.QApplication.translate("indicator_PVstatus_vertical", "PV status", None, QtGui.QApplication.UnicodeUTF8))

