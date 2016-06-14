# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jose/python/proyecto_simulacion/simulacion/UI/simulation_widget.ui'
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
        SimulationWindow.resize(665, 475)
        self.centralwidget = QtGui.QWidget(SimulationWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.cubaMapBtn = QtGui.QPushButton(self.tab)
        self.cubaMapBtn.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.cubaMapBtn.setObjectName(_fromUtf8("cubaMapBtn"))
        self.comboBoxProv = QtGui.QComboBox(self.tab)
        self.comboBoxProv.setGeometry(QtCore.QRect(20, 70, 141, 29))
        self.comboBoxProv.setObjectName(_fromUtf8("comboBoxProv"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.worldMapBtn = QtGui.QPushButton(self.tab_2)
        self.worldMapBtn.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.worldMapBtn.setObjectName(_fromUtf8("worldMapBtn"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        SimulationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SimulationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SimulationWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SimulationWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SimulationWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SimulationWindow)

    def retranslateUi(self, SimulationWindow):
        SimulationWindow.setWindowTitle(_translate("SimulationWindow", "MainWindow", None))
        self.cubaMapBtn.setText(_translate("SimulationWindow", "Mapa de Cuba", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SimulationWindow", "Migraciones Internas", None))
        self.worldMapBtn.setText(_translate("SimulationWindow", "Mapa del Mundo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SimulationWindow", "Migraciones Externas", None))

