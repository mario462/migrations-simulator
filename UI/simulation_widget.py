# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jose/python/proyecto_simulacion/UI/simulation_widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SimulationWindow(object):
    def setupUi(self, SimulationWindow):
        SimulationWindow.setObjectName(_fromUtf8("SimulationWindow"))
        SimulationWindow.resize(346, 185)
        self.centralwidget = QtGui.QWidget(SimulationWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.worldMapBtn = QtGui.QPushButton(self.centralwidget)
        self.worldMapBtn.setObjectName(_fromUtf8("worldMapBtn"))
        self.verticalLayout.addWidget(self.worldMapBtn)
        self.cubaMapBtn = QtGui.QPushButton(self.centralwidget)
        self.cubaMapBtn.setObjectName(_fromUtf8("cubaMapBtn"))
        self.verticalLayout.addWidget(self.cubaMapBtn)
        SimulationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SimulationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SimulationWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SimulationWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SimulationWindow)
        QtCore.QMetaObject.connectSlotsByName(SimulationWindow)

    def retranslateUi(self, SimulationWindow):
        SimulationWindow.setWindowTitle(_translate("SimulationWindow", "MainWindow", None))
        self.worldMapBtn.setText(_translate("SimulationWindow", "World map", None))
        self.cubaMapBtn.setText(_translate("SimulationWindow", "Cuba map", None))

