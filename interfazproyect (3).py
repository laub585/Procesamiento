import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import cv2 as cv
import mediapipe as mp
from math import atan2, pi


import serial.tools.list_ports
import serial
import numpy as np
import struct


import threading

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.signal import butter, filtfilt  # procesamiento digital de señales 

class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        uic.loadUi("interfazproyectointegrador.ui",self)
        self.puertos_disponibles()
        self.ser = None
        self.connect.clicked.connect(self.conectar)
        
        self.x = np.linspace(0,10,1000)
        self.y = np.linspace(0,0,1000)

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.graficaWidget.setLayout(layout)

        self.fig1 = Figure()
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.set_xlim(0, 10)  # Fijar los límites del eje x
        self.ax1.set_ylim(-1000, 1000)  # Fijar los límites del eje y (ajusta según sea necesario)        
        self.canvas1 = FigureCanvas(self.fig1)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas1)
        self.FILTRO.setLayout(layout1)

        self.fm = 100 #100 muestras por segundo
        #Definir la frecuencia de corte del filtro (en Hz)
        self.fc = 5 # eliminar señal que se cola del sensor 
        self.fn = self.fc / (0.5* self.fm)
        self.orden = 4

        self.b, self.a = butter(self.orden, self.fn, btype='high',analog=False)
        self.c, self.d = butter(self.orden, self.fn, btype='low',analog=False)
        
        
    def puertos_disponibles(self):
        p = serial.tools.list_ports.comports()
        for port in p:
            self.puertos.addItem(port.device)
            
    def conectar(self):
        estado = self.connect.text()
        self.stop_event_ser= threading.Event()
        if estado =="CONECTAR":
            com = self.puertos.currentText()
            try:
                self.ser = serial.Serial(com,115200)
                self.hilo_ser = threading.Thread(target=self.periodic_thread)
                self.hilo_ser.start()
                print("Puerto serial Conectado")
                self.connect.setText("DESCONECTAR")
            except serial.SerialException as e:
                print("Error en el puerto serial:", e)
        else:
            self.ser.close()
            self.stop_event_ser.set()
            self.hilo_ser.join()
            print("Puerto serial Desconectado")
            self.connect.setText("CONECTAR")

            
    def periodic_thread(self):
        if self.ser is not None and self.ser.is_open:
            data = self.ser.read(50)
            if len(data) ==50:
                data = struct.unpack('50B',data)
                for i in range(0,len(data),2):
                    self.y = np.roll(self.y,-1)
                    self.y[-1] =  (data[i]*100+data[i+1])

                dfH = filtfilt(self.b, self.a, self.y)
                dfL = filtfilt(self.c, self.d, self.y)
                
                self.ax.clear()
                self.ax.plot(self.x,dfH)
                self.ax.grid(True)
                self.canvas.draw()

                self.ax1.clear()
                self.ax1.plot(self.x,dfL)
                self.ax1.grid(True)
                self.canvas1.draw()
                
        if not self.stop_event_ser.is_set():
            print("datos")
            threading.Timer(1e-3,self.periodic_thread).start()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec())

