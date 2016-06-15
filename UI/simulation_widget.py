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
        SimulationWindow.resize(754, 559)
        self.centralwidget = QtGui.QWidget(SimulationWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cubaMapBtn = QtGui.QPushButton(self.tab)
        self.cubaMapBtn.setObjectName(_fromUtf8("cubaMapBtn"))
        self.gridLayout.addWidget(self.cubaMapBtn, 1, 0, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidget1 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget1.setAlternatingRowColors(True)
        self.tableWidget1.setCornerButtonEnabled(False)
        self.tableWidget1.setRowCount(17)
        self.tableWidget1.setColumnCount(17)
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.tableWidget1.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget1.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget1.horizontalHeader().setStretchLastSection(False)
        self.tableWidget1.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_3.addWidget(self.tableWidget1)
        self.tabWidget_2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tableWidget2 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget2.setAlternatingRowColors(True)
        self.tableWidget2.setCornerButtonEnabled(False)
        self.tableWidget2.setRowCount(17)
        self.tableWidget2.setColumnCount(17)
        self.tableWidget2.setObjectName(_fromUtf8("tableWidget2"))
        self.tableWidget2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget2.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget2.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_4.addWidget(self.tableWidget2)
        self.tabWidget_2.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget_2, 0, 1, 2, 1)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.initialPopulationBtn = QtGui.QPushButton(self.groupBox)
        self.initialPopulationBtn.setObjectName(_fromUtf8("initialPopulationBtn"))
        self.verticalLayout_2.addWidget(self.initialPopulationBtn)
        self.nextStepBtn = QtGui.QPushButton(self.groupBox)
        self.nextStepBtn.setObjectName(_fromUtf8("nextStepBtn"))
        self.verticalLayout_2.addWidget(self.nextStepBtn)
        self.simBtn = QtGui.QPushButton(self.groupBox)
        self.simBtn.setObjectName(_fromUtf8("simBtn"))
        self.verticalLayout_2.addWidget(self.simBtn)
        self.stopBtn = QtGui.QPushButton(self.groupBox)
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.verticalLayout_2.addWidget(self.stopBtn)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SimulationWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SimulationWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SimulationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SimulationWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SimulationWindow)

    def retranslateUi(self, SimulationWindow):
        SimulationWindow.setWindowTitle(_translate("SimulationWindow", "MainWindow", None))
        self.cubaMapBtn.setText(_translate("SimulationWindow", "Mapa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("SimulationWindow", "Tabla 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("SimulationWindow", "Tabla 2", None))
        self.groupBox.setTitle(_translate("SimulationWindow", "General", None))
        self.initialPopulationBtn.setText(_translate("SimulationWindow", "Poblacion inicial", None))
        self.nextStepBtn.setText(_translate("SimulationWindow", "Siguiente paso", None))
        self.simBtn.setText(_translate("SimulationWindow", "Simulacion", None))
        self.stopBtn.setText(_translate("SimulationWindow", "Parar", None))
        self.label.setText(_translate("SimulationWindow", "paso:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SimulationWindow", "Migraciones Internas", None))
        self.worldMapBtn.setText(_translate("SimulationWindow", "Mapa del Mundo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SimulationWindow", "Migraciones Externas", None))

