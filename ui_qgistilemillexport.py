# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qgistilemillexport.ui'
#
# Created: Mon Apr  9 12:54:18 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QGISTileMillExport(object):
    def setupUi(self, QGISTileMillExport):
        QGISTileMillExport.setObjectName(_fromUtf8("QGISTileMillExport"))
        QGISTileMillExport.resize(432, 336)
        self.mssTextBox = QtGui.QPlainTextEdit(QGISTileMillExport)
        self.mssTextBox.setGeometry(QtCore.QRect(53, 81, 341, 192))
        self.mssTextBox.setObjectName(_fromUtf8("mssTextBox"))
        self.label = QtGui.QLabel(QGISTileMillExport)
        self.label.setGeometry(QtCore.QRect(19, 81, 26, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.layerComboBox = QtGui.QComboBox(QGISTileMillExport)
        self.layerComboBox.setGeometry(QtCore.QRect(50, 40, 171, 26))
        self.layerComboBox.setObjectName(_fromUtf8("layerComboBox"))
        self.label_3 = QtGui.QLabel(QGISTileMillExport)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 34, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.buttonBox = QtGui.QDialogButtonBox(QGISTileMillExport)
        self.buttonBox.setGeometry(QtCore.QRect(47, 289, 164, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(QGISTileMillExport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QGISTileMillExport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QGISTileMillExport.reject)
        QtCore.QMetaObject.connectSlotsByName(QGISTileMillExport)

    def retranslateUi(self, QGISTileMillExport):
        QGISTileMillExport.setWindowTitle(QtGui.QApplication.translate("QGISTileMillExport", "Generate TileMill MSS", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QGISTileMillExport", "MSS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("QGISTileMillExport", "Layer", None, QtGui.QApplication.UnicodeUTF8))

