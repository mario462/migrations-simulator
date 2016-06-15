from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import sys
import os
import json
import random
import pprint as pp
from UI.simulation_widget import Ui_SimulationWindow
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
    "STG",
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

        #region Buttons
        self.worldMapBtn.clicked.connect(self.mapa_mundi)
        self.cubaMapBtn.clicked.connect(self.mapa_cuba)
        self.initialPopulationBtn.clicked.connect(self.on_initial_population_clicked)
        self.nextStepBtn.clicked.connect(self.on_next_step_clicked)
        self.simBtn.clicked.connect(self.on_sim_clicked)
        self.stopBtn.clicked.connect(self.on_stop_clicked)
        #endregion

        self.fill_header_table(self.tableWidget1)
        self.fill_header_table(self.tableWidget2)

    def fill_header_table(self, table):
        table.setRowCount(len(name_provinces))
        table.setVerticalHeaderLabels(name_provinces)

        table.setColumnCount(len(name_provinces))
        table.setHorizontalHeaderLabels(short_provinces)

    def fill_table(self, table, data):
        for i, name in enumerate(name_provinces):
            d_name = data[name]
            for j, name in enumerate(name_provinces):
                value = d_name[name]
                item = QTableWidgetItem(str(value))
                table.setItem(i, j, item)

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
        self.iteration = 0
        self.label.setText("paso:" + str(self.iteration))
        population = self.sim.population()
        self.iter = self.sim.simulate(10)
                # pp.pprint(population)

        self.mapa_cuba()

        self.print_population(population)

        self.print_arrow()

    def print_arrow(self):
        coord_1 = self.prov["La Habana"]
        coord_2 = self.prov["Guantánamo"]

        x, y = self.m([coord_1[1], coord_2[1]], [coord_1[0], coord_2[0]])



        plt.annotate("", xytext=(x[0], y[0]), xy=(x[1], y[1]), arrowprops=dict(arrowstyle='fancy'))
        plt.draw()

    def on_next_step_clicked(self):
        self.iteration += 1
        self.label.setText("paso: " + str(self.iteration))

        population, migration, living_place = next(self.iter)
        pp.pprint(population)
        self.mapa_cuba()

        self.print_population(population)

        self.fill_table(self.tableWidget1, migration)
        self.fill_table(self.tableWidget2, living_place)

    def print_population(self, population):
        lons = []
        lats = []
        labels = []
        for par in population.items():
            lons.append(self.prov[par[0].name][1])
            lats.append(self.prov[par[0].name][0])
            labels.append(par[1])

        x, y = self.m(lons, lats)
        # m.plot(x, y, '#000000', markersize=10)

        labels = [x for x in population.values()]
        for label, xpt, ypt in zip(labels, x, y):
            plt.text(xpt, ypt, label)

        # plt.show()
        plt.draw()

    def mapa_mundi(self):
        plt.close()
        m = Basemap(projection='cyl', resolution='l', area_thresh=1000.0)
        m.drawcoastlines()
        m.fillcontinents(color=self.colorEarth, lake_color=self.colorWater)
        m.drawmapboundary(fill_color=self.colorWater)
        m.drawcountries()
        m.drawparallels(np.linspace(-90, 90, 7), labels=[1, 0, 0, 0])
        m.drawmeridians(np.linspace(0, 360, 9), labels=[0, 0, 1, 0])

        selected_countries = ["Jamaica", "Cuba", "Puerto Rico", "Estados Unidos de América", "Canadá", "España", "Francia", "Venezuela", "Brasil", "Argentina"]

        lons = [self.countries[x][1] for x in selected_countries]
        lats = [self.countries[x][0] for x in selected_countries]
        x, y = m(lons, lats)
        m.plot(x, y, 'bo', markersize=10)

        labels = selected_countries
        for label, xpt, ypt in zip(labels, x, y):
            plt.text(xpt-0.3, ypt+0.1, label, color='b')

        # plt.show()

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
        lons = [x[1] for x in self.prov.values()]
        lats = [x[0] for x in self.prov.values()]
        x, y = self.m(lons, lats)
        self.m.plot(x, y, 'bo', markersize=6)

        labels = self.prov.keys()
        for label, xpt, ypt in zip(labels, x, y):
            self.ax.text(xpt-0.3, ypt+0.1, label, color='w')

        if not self.is_plot:
            self.is_plot = True
            plt.show()
        # return m
        # plt.show()


class Aux:
    def __init__(self):
        pass

    def initial_population(self):
        prov = load_provinces()
        d = {}
        for i in prov.items():
            d[i[0]] = random.randint(1000, 10000)
        return d

    def step(self):
        return self.initial_population()

    def tabla1(self):
        dic = {x: random.randint(1, 10) for x in name_provinces}
        res = {x: dic.copy() for x in name_provinces}
        pp.pprint(res)
        return res

    def tabla2(self):
        dic = {x: random.randint(1, 10) for x in name_provinces}
        res = {x: dic.copy() for x in name_provinces}
        return res



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SimWidget()
    w.show()
    app.exec_()
