# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qgistilemillexport.ui'
#
# Created: Mon Apr  9 12:18:48 2012
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
        QGISTileMillExport.resize(325, 335)
        self.widget = QtGui.QWidget(QGISTileMillExport)
        self.widget.setGeometry(QtCore.QRect(10, 40, 300, 280))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.layerInput = QtGui.QComboBox(self.widget)
        self.layerInput.setObjectName(_fromUtf8("layerInput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.layerInput)
        self.label = QtGui.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.mssTextBox = QtGui.QPlainTextEdit(self.widget)
        self.mssTextBox.setObjectName(_fromUtf8("mssTextBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.mssTextBox)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(QGISTileMillExport)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QGISTileMillExport.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QGISTileMillExport.reject)
        QtCore.QMetaObject.connectSlotsByName(QGISTileMillExport)

    def retranslateUi(self, QGISTileMillExport):
        QGISTileMillExport.setWindowTitle(QtGui.QApplication.translate("QGISTileMillExport", "QGISTileMillExport", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("QGISTileMillExport", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("QGISTileMillExport", "MSS", None, QtGui.QApplication.UnicodeUTF8))

