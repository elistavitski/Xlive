# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_ExperimentDesign.ui'
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

class Ui_widget_ExperimentDesign(object):
    def setupUi(self, widget_ExperimentDesign):
        widget_ExperimentDesign.setObjectName(_fromUtf8("widget_ExperimentDesign"))
        widget_ExperimentDesign.resize(918, 654)
        self.treeWidget = QtGui.QTreeWidget(widget_ExperimentDesign)
        self.treeWidget.setGeometry(QtCore.QRect(30, 10, 181, 621))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))

        self.retranslateUi(widget_ExperimentDesign)
        QtCore.QMetaObject.connectSlotsByName(widget_ExperimentDesign)

    def retranslateUi(self, widget_ExperimentDesign):
        widget_ExperimentDesign.setWindowTitle(QtGui.QApplication.translate("widget_ExperimentDesign", "Form", None, QtGui.QApplication.UnicodeUTF8))

