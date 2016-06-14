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
        SimulationWindow.resize(753, 513)
        self.centralwidget = QtGui.QWidget(SimulationWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.cubaMapBtn = QtGui.QPushButton(self.tab)
        self.cubaMapBtn.setGeometry(QtCore.QRect(250, 20, 121, 31))
        self.cubaMapBtn.setObjectName(_fromUtf8("cubaMapBtn"))
        self.comboBoxProv = QtGui.QComboBox(self.tab)
        self.comboBoxProv.setGeometry(QtCore.QRect(360, 130, 141, 29))
        self.comboBoxProv.setObjectName(_fromUtf8("comboBoxProv"))
        self.initialPopulationBtn = QtGui.QPushButton(self.tab)
        self.initialPopulationBtn.setGeometry(QtCore.QRect(20, 90, 181, 31))
        self.initialPopulationBtn.setObjectName(_fromUtf8("initialPopulationBtn"))
        self.nextStepBtn = QtGui.QPushButton(self.tab)
        self.nextStepBtn.setGeometry(QtCore.QRect(20, 140, 111, 31))
        self.nextStepBtn.setObjectName(_fromUtf8("nextStepBtn"))
        self.simBtn = QtGui.QPushButton(self.tab)
        self.simBtn.setGeometry(QtCore.QRect(20, 190, 97, 31))
        self.simBtn.setObjectName(_fromUtf8("simBtn"))
        self.stopBtn = QtGui.QPushButton(self.tab)
        self.stopBtn.setGeometry(QtCore.QRect(20, 240, 97, 31))
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 290, 65, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.migrateFromBtn = QtGui.QPushButton(self.tab)
        self.migrateFromBtn.setGeometry(QtCore.QRect(370, 80, 111, 31))
        self.migrateFromBtn.setObjectName(_fromUtf8("migrateFromBtn"))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 27))
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
        self.cubaMapBtn.setText(_translate("SimulationWindow", "Mapa", None))
        self.initialPopulationBtn.setText(_translate("SimulationWindow", "Generar poblacion inicial", None))
        self.nextStepBtn.setText(_translate("SimulationWindow", "Siguiente paso", None))
        self.simBtn.setText(_translate("SimulationWindow", "Simulacion", None))
        self.stopBtn.setText(_translate("SimulationWindow", "Parar", None))
        self.label.setText(_translate("SimulationWindow", "paso:", None))
        self.migrateFromBtn.setText(_translate("SimulationWindow", "Emigran desde", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SimulationWindow", "Migraciones Internas", None))
        self.worldMapBtn.setText(_translate("SimulationWindow", "Mapa del Mundo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SimulationWindow", "Migraciones Externas", None))

