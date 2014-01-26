# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_BeamlineStatus.ui'
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

class Ui_widget_BeamlineStatus(object):
    def setupUi(self, widget_BeamlineStatus):
        widget_BeamlineStatus.setObjectName(_fromUtf8("widget_BeamlineStatus"))
        widget_BeamlineStatus.resize(922, 656)
        self.label = QtGui.QLabel(widget_BeamlineStatus)
        self.label.setGeometry(QtCore.QRect(30, 130, 731, 351))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cantarell"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(widget_BeamlineStatus)
        self.pushButton.setGeometry(QtCore.QRect(240, 560, 95, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(widget_BeamlineStatus)
        QtCore.QMetaObject.connectSlotsByName(widget_BeamlineStatus)

    def retranslateUi(self, widget_BeamlineStatus):
        widget_BeamlineStatus.setWindowTitle(QtGui.QApplication.translate("widget_BeamlineStatus", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("widget_BeamlineStatus", "asdfasfdasdfasdfasdfasdf", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("widget_BeamlineStatus", "asdasdasda", None, QtGui.QApplication.UnicodeUTF8))

