# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indicator_pv_status_horizontal.ui'
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

class Ui_indicator_pv_status_horizontal(object):
    def setupUi(self, indicator_pv_status_horizontal):
        indicator_pv_status_horizontal.setObjectName(_fromUtf8("indicator_pv_status_horizontal"))
        indicator_pv_status_horizontal.resize(205, 24)
        self.horizontalLayoutWidget = QtGui.QWidget(indicator_pv_status_horizontal)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 23))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_pv_name = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_pv_name.setObjectName(_fromUtf8("label_pv_name"))
        self.horizontalLayout.addWidget(self.label_pv_name)
        self.label_pv_value = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_pv_value.setObjectName(_fromUtf8("label_pv_value"))
        self.horizontalLayout.addWidget(self.label_pv_value)

        self.retranslateUi(indicator_pv_status_horizontal)
        QtCore.QMetaObject.connectSlotsByName(indicator_pv_status_horizontal)

    def retranslateUi(self, indicator_pv_status_horizontal):
        indicator_pv_status_horizontal.setWindowTitle(QtGui.QApplication.translate("indicator_pv_status_horizontal", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pv_name.setText(QtGui.QApplication.translate("indicator_pv_status_horizontal", "---", None, QtGui.QApplication.UnicodeUTF8))
        self.label_pv_value.setText(QtGui.QApplication.translate("indicator_pv_status_horizontal", "---", None, QtGui.QApplication.UnicodeUTF8))

