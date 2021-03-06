from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import sys
import os
import json
import pprint as pp
from UI.simulation_widget import Ui_SimulationWindow
from UI.logs_widget import Ui_MainWindow
from main import Simulation


def load_countries():
    s = "data" + os.sep + "parsed_countries"
    d = open(s, 'r')
    return json.loads(d.read())


def load_provinces():
    s = "data" + os.sep + "parsed_provinces"
    d = open(s, 'r')
    return json.loads(d.read(), encoding='utf-8')


#region Provinces
name_provinces = [
    "Pinar del Río",
    "La Habana",
    "Matanzas",
    "Artemisa",
    "Mayabeque",
    "Cienfuegos",
    "Villa Clara",
    "Sancti Spíritus",
    "Ciego de Ávila",
    "Camagüey",
    "Las Tunas",
    "Granma",
    "Holguín",
    "Santiago de Cuba",
    "Guantánamo",
    "Isla de la Juventud"
]
short_provinces = [
    "Tot",
    "PRI",
    "LHA",
    "MTZ",
    "ART",
    "MAY",
    "CFG",
    "VCL",
    "SSP",
    "CAV",
    "CMG",
    "LTU",
    "GRM",
    "HOL",
    "SCU",
    "GTM",
    "IJV"
]
#endregion


class SimWidget(QMainWindow, Ui_SimulationWindow):
    def __init__(self, parent=None):
        super(SimWidget, self).__init__(parent)
        self.setupUi(self)
        self.colorEarth = '#009900'
        self.colorWater = '#27b6e9'

        self.timer = QTimer()
        self.time = 500
        self.running = False

        fig = plt.figure()
        self.ax = fig.add_subplot(111)
        self.is_plot = False

        self.sim = Simulation()

        self.prov = load_provinces()
        self.countries = load_countries()

        aux = name_provinces.copy()
        aux.insert(0, "None")
        self.comboBoxProv.addItems(aux)
        self.comboBoxProv.currentIndexChanged.connect(self.on_comboBoxProv_indexChanged)

        self.comboBoxEvProv.addItems(name_provinces)
        self.parameters = ["Cant de viviendas", "Salario medio", "Desempleo"]
        self.comboBoxEvPar.addItems(self.parameters)
        self.comboBoxEvProv.setCurrentIndex(1)
        self.comboBoxEvPar.setCurrentIndex(1)

        self.logs = []

        #region Buttons
        self.worldMapBtn.clicked.connect(self.mapa_mundi)
        # self.cubaMapBtn.clicked.connect(self.mapa_cuba)
        self.initialPopulationBtn.clicked.connect(self.on_initial_population_clicked)
        self.nextStepBtn.clicked.connect(self.on_next_step_clicked)
        self.simBtn.clicked.connect(self.on_sim_clicked)
        self.stopBtn.clicked.connect(self.on_stop_clicked)
        self.updateEventBtn.clicked.connect(self.on_update_event_clicked)
        self.logsBtn.clicked.connect(self.on_logsBtn)
        #endregion

        self.fill_header_table(self.tableWidget1)
        self.fill_header_table(self.tableWidget2)

    def fill_header_table(self, table):
        table.setRowCount(len(name_provinces))
        table.setVerticalHeaderLabels(name_provinces)

        table.setColumnCount(len(short_provinces))
        table.setHorizontalHeaderLabels(short_provinces)

    def fill_table(self, table, data):
        for i, name in enumerate(name_provinces):
            d_name = data[name]
            total = 0
            for j, name in enumerate(name_provinces):
                if name in d_name:
                    value = d_name[name]
                    total += value
                    item = QTableWidgetItem(str(value))
                    table.setItem(i, j+1, item)
            item = QTableWidgetItem(str(total))
            table.setItem(i, 0, item)

    def on_stop_clicked(self):
        self.running = False

    def on_sim_clicked(self):
        self.running = True
        self.simulate()

    def simulate(self):
        if self.running:
            self.on_next_step_clicked()
            self.timer.singleShot(self.time, self.simulate)

    def on_initial_population_clicked(self):
        self.nextStepBtn.setEnabled(True)
        self.stopBtn.setEnabled(True)
        self.simBtn.setEnabled(True)
        self.groupBoxEventos.setEnabled(True)

        self.iteration = 0
        self.label.setText("paso:" + str(self.iteration))
        population = self.sim.population()
        self.iter = self.sim.simulate(10)

        self.mapa_cuba()

        self.print_population(population)
        # self.print_arrow()

    def on_next_step_clicked(self):
        self.groupBoxFlechas.setEnabled(True)
        self.comboBoxProv.setEnabled(True)

        self.iteration += 1
        self.label.setText("paso: " + str(self.iteration))

        try:
            self.population, self.migration, self.living_place = next(self.iter)
            # pp.pprint(self.population)
            self.fill_map()
            self.fill_tables()
        except StopIteration:
            self.running = False

    def fill_map(self):
        self.mapa_cuba()
        self.print_population(self.population)

    def fill_tables(self):
        self.fill_table(self.tableWidget1, self.migration)
        self.fill_table(self.tableWidget2, self.living_place)

    def print_population(self, population):
        lons = []
        lats = []
        labels = []
        for par in population.items():
            lons.append(self.prov[par[0]][1])
            lats.append(self.prov[par[0]][0])
            labels.append(par[1])

        x, y = self.m(lons, lats)
        # m.plot(x, y, '#000000', markersize=10)

        labels = [int(x) for x in population.values()]
        for label, xpt, ypt in zip(labels, x, y):
            plt.text(xpt-0.28, ypt-0.18, label)

        # plt.show()
        plt.draw()

    def mapa_mundi(self):
        plt.close()
        self.ax.clear()
        self.m = Basemap(projection='cyl', resolution='l', area_thresh=1000.0)
        self.m.drawcoastlines()
        self.m.fillcontinents(color=self.colorEarth, lake_color=self.colorWater)
        self.m.drawmapboundary(fill_color=self.colorWater)
        self.m.drawcountries()
        self.m.drawparallels(np.linspace(-90, 90, 7), labels=[1, 0, 0, 0])
        self.m.drawmeridians(np.linspace(0, 360, 9), labels=[0, 0, 1, 0])

        selected_countries = ["Cuba", "Estados Unidos de América", "España", "Venezuela", "Brasil", "Rusia"]


        lons = [self.countries[x][1] for x in selected_countries]
        lats = [self.countries[x][0] for x in selected_countries]
        x, y = self.m(lons, lats)
        # self.m.plot(x, y, 'bo', markersize=6)

        labels = selected_countries
        for label, xpt, ypt in zip(labels, x, y):
            plt.text(xpt-0.3, ypt+0.1, label, color='b')

        plt.show()
        # plt.draw()

    def mapa_cuba(self):
        # plt.close()
        self.ax.clear()
        c_lon, c_lat = -79.5, 21.5
        delta_lon, delta_lat = 6, 2.5

        self.m = Basemap(projection='cyl', resolution='i', area_thresh=0.1, lat_0=c_lat, lon_0=c_lon,
                    llcrnrlat=c_lat-delta_lat, llcrnrlon=c_lon-delta_lon, urcrnrlat=c_lat+delta_lat, urcrnrlon=c_lon+delta_lon)
        self.m.drawcoastlines()
        self.m.fillcontinents(color=self.colorEarth, lake_color=self.colorWater)
        self.m.drawmapboundary(fill_color=self.colorWater)
        self.m.drawparallels(np.linspace(c_lat-delta_lat, c_lat+delta_lat, 7), labels=[1, 0, 0, 0], fmt='%.2f')
        self.m.drawmeridians(np.linspace(c_lon-delta_lon, c_lon+delta_lon, 9), labels=[0, 0, 1, 0])
        lons = [self.prov[x][1] for x in name_provinces]
        lats = [self.prov[x][0] for x in name_provinces]
        x, y = self.m(lons, lats)
        self.m.plot(x, y, 'bo', markersize=6)

        labels = short_provinces[1:]
        for label, xpt, ypt in zip(labels, x, y):
            self.ax.text(xpt-0.15, ypt+0.1, label, color='w')

        if not self.is_plot:
            self.is_plot = True
            plt.show()
        # return m
        # plt.show()

    def on_comboBoxProv_indexChanged(self):
        prov = self.comboBoxProv.currentText()
        self.fill_map()
        if prov != "None":
            d = self.migration[prov]
            for i in d.items():
                self.print_arrow(prov, i[0], i[1])

    def print_arrow(self, origin, destiny, cant):
        if cant == 0:
            return

        coord_o = self.prov[origin]
        coord_d = self.prov[destiny]

        x, y = self.m([coord_o[1], coord_d[1]], [coord_o[0], coord_d[0]])

        plt.annotate("", xytext=(x[0], y[0]), xy=(x[1], y[1]), arrowprops=dict(arrowstyle='fancy'))

        coord_media = ((x[0] + x[1])/2, (y[0] + y[1])/2)
        plt.text(coord_media[0], coord_media[1], str(cant), color='w')
        plt.draw()

    def on_update_event_clicked(self):
        prov = self.comboBoxEvProv.currentIndex()
        param = self.comboBoxEvPar.currentIndex()
        per_cent = float(self.dSpinBoxPerCent.value())

        p = [x for x in self.sim.provinces if x.name == name_provinces[prov]][0]

        if param == 0:
            self.sim.change_housing(p, per_cent)
        if param == 1:
            self.sim.change_salary(p, per_cent)
        # if param == 2:
        #     self.sim.change_population(p, per_cent)
        if param == 2:
            self.sim.change_unemployment(p, per_cent)

        s = "El parametro %s cambio a un %.2f porciento en la provincia %s" % (self.parameters[param], per_cent, name_provinces[prov])
        QMessageBox.warning(QMessageBox(), "Nuevo evento", s)
        self.logs.append(s)

    def on_logsBtn(self):
        print("jose")
        log_wid = LogWidget(self.logs, self)
        log_wid.show()


class LogWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, logs, parent=None):
        super(LogWidget, self).__init__(parent)
        self.setupUi(self)
        self.listWidget.addItems(logs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SimWidget()
    w.show()
    app.exec_()
