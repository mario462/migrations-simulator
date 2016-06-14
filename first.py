import sys
import os
import json

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from PyQt4.QtGui import *
import numpy as np

from UI.simulation_widget import Ui_SimulationWindow


class SimWidget(QMainWindow, Ui_SimulationWindow):
    def __init__(self, parent=None):
        super(SimWidget, self).__init__(parent)
        self.setupUi(self)
        self.colorEarth = '#009900'
        self.colorWater = '#27b6e9'

        self.cubaMapBtn.clicked.connect(self.mapa_cuba)
        self.worldMapBtn.clicked.connect(self.mapa_mundi)
        self.load_provincias()
        self.load_countries()

    def on_show_map_btn_clicked(self):
        # self.mapa_mundi()
        self.mapa_cuba()

    def mapa_mundi(self):
        plt.close()
        m = Basemap(projection='cyl', resolution='l', area_thresh=1000.0)
        m.drawcoastlines()
        m.fillcontinents(color=self.colorEarth, lake_color=self.colorWater)
        m.drawmapboundary(fill_color=self.colorWater)
        m.drawcountries()
        m.drawparallels(np.linspace(-90, 90, 7), labels=[1, 0, 0, 0])
        m.drawmeridians(np.linspace(0, 360, 9), labels=[0, 0, 1, 0])

        selected_countries = ["Cuba", "Puerto Rico", "Estados Unidos de América", "Canadá", "España", "Francia", "Venezuela", "Brasil", "Argentina"]

        lons = [self.countries[x][1] for x in selected_countries]
        lats = [self.countries[x][0] for x in selected_countries]
        x, y = m(lons, lats)
        m.plot(x, y, 'bo', markersize=10)

        labels = selected_countries
        for label, xpt, ypt in zip(labels, x, y):
            plt.text(xpt-0.3, ypt+0.1, label, color='b')
        plt.show()

    def mapa_cuba(self):
        plt.close()
        c_lon, c_lat = -79.5, 21.5
        delta_lon, delta_lat = 6, 2.5

        m = Basemap(projection='cyl', resolution='i', area_thresh=0.1, lat_0=c_lat, lon_0=c_lon,
                    llcrnrlat=c_lat-delta_lat, llcrnrlon=c_lon-delta_lon, urcrnrlat=c_lat+delta_lat, urcrnrlon=c_lon+delta_lon)
        m.drawcoastlines()
        m.fillcontinents(color=self.colorEarth, lake_color=self.colorWater)
        m.drawmapboundary(fill_color=self.colorWater)
        m.drawparallels(np.linspace(c_lat-delta_lat, c_lat+delta_lat, 7), labels=[1, 0, 0, 0], fmt='%.2f')
        m.drawmeridians(np.linspace(c_lon-delta_lon, c_lon+delta_lon, 9), labels=[0, 0, 1, 0])
        lons = [x[1] for x in self.prov.values()]
        lats = [x[0] for x in self.prov.values()]
        x, y = m(lons, lats)
        m.plot(x, y, 'bo', markersize=10)

        labels = self.prov.keys()
        for label, xpt, ypt in zip(labels, x, y):
            plt.text(xpt-0.3, ypt+0.1, label, color='w')

        plt.show()

    def load_provincias(self):
        s = "Core" + os.sep + "provincias"
        d = open(s, 'r')
        self.prov = json.loads(d.read())
        print("load_prov")

    def load_countries(self):
        s = "Core" + os.sep + "paises"
        d = open(s, 'r')
        self.countries = json.loads(d.read())
        print("load_countries")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SimWidget()
    w.show()
    app.exec_()