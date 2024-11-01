import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtCore import *
import serial.tools.list_ports
import serial
import numpy as np
import struct
import threading
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.signal import butter, filtfilt  # procesamiento digital de señales 
from scipy.signal import windows

class principal(QMainWindow):
    def __init__(self):
        super(principal, self).__init__()
        uic.loadUi("interfazproyectointegrador.ui", self)
        self.puertos_disponibles()
        self.ser = None
        self.connect.clicked.connect(self.conectar)
        
        self.enviar_2.clicked.connect(self.guardar_datos_grafica)
        
        self.x = np.linspace(0, 10, 1000)  # Eje x para 10 segundos
        self.y = np.zeros(1000)  # Inicializa la señal en cero

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-1500, 1500)
        self.ax.set_xlabel("Tiempo (s)")  # Título del eje X
        self.ax.set_ylabel("Amplitud")  # Título del eje Y
        self.canvas = FigureCanvas(self.fig)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.graficaWidget.setLayout(layout)

        self.fig1 = Figure()
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.set_xlim(0, 10)
        self.ax1.set_ylim(-100, 10000)
        self.ax1.set_xlabel("Tiempo (s)")  # Título del eje X
        self.ax1.set_ylabel("Amplitud Normalizada")  # Título del eje Y
        self.canvas1 = FigureCanvas(self.fig1)
        layout1 = QVBoxLayout()
        layout1.addWidget(self.canvas1)
        self.FILTRO.setLayout(layout1)

        self.fm = 1000  # Frecuencia de muestreo (muestras por segundo)
        self.fc_alta = 50  # Frecuencia de corte alta
        self.fc_baja = 450  # Frecuencia de corte baja
        self.fn_alta = self.fc_alta / (0.5 * self.fm)
        self.fn_baja = self.fc_baja / (0.5 * self.fm)
        self.orden = 4
        
        self.b, self.a = butter(self.orden, self.fn_alta, btype='high', analog=False)
        self.c, self.d = butter(self.orden, self.fn_baja, btype='low', analog=False)

        self.data_storage = []  # Almacena las últimas 60 segundos de datos
        self.time_counter = 0  # Contador de tiempo acumulado
        self.time_precision = 7  # Cifras significativas para evitar repeticiones en los tiempos

    def puertos_disponibles(self):
        p = serial.tools.list_ports.comports()
        for port in p:
            self.puertos.addItem(port.device)
            
    def conectar(self):
        estado = self.connect.text()
        self.stop_event_ser = threading.Event()
        if estado == "CONECTAR":
            com = self.puertos.currentText()
            try:
                self.ser = serial.Serial(com, 115200)
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
            
    def guardar_datos_grafica(self):
        """Guardar los datos de la gráfica ax (x e y) en un archivo .txt."""
        if self.data_storage:  # Verificar si hay datos para guardar
            try:
                with open("datos_grafica_ax.txt", "w") as archivo:
                    for (x_val, y_val) in self.data_storage:
                        # Guardar x y y en el archivo, limitando las cifras significativas de x
                        archivo.write(f"{x_val:.{self.time_precision}f}, {y_val:.1f}\n")
                
                # Mensaje de confirmación
                QMessageBox.information(self, "Guardado", "Datos de la gráfica ax (x, y) guardados correctamente.")
                print("Datos guardados correctamente.")
        
            except Exception as e:
                print(f"Error al guardar los datos: {e}")
                QMessageBox.warning(self, "Error", f"Error al guardar los datos: {e}")
        else:
            print("No hay datos disponibles para guardar.")
            QMessageBox.warning(self, "Error", "No hay datos disponibles para guardar.")

    
    def periodic_thread(self):
        if self.ser is not None and self.ser.is_open:
            data = self.ser.read(50)
            if len(data) == 50:
                data = struct.unpack('50B', data)
                for i in range(0, len(data), 2):
                    self.y = np.roll(self.y, -1)
                    self.y[-1] = (data[i] * 100 + data[i + 1])

                    # Actualizar el contador de tiempo acumulado
                    self.time_counter += 1 / self.fm  # Incrementa por la frecuencia de muestreo

                    # Redondear el valor de tiempo a las cifras significativas especificadas
                    time_rounded = round(self.time_counter, self.time_precision)

                    # Agregar el último valor a data_storage con tiempo no repetido
                    self.data_storage.append((time_rounded, self.y[-1]))

                    # Mantener solo los últimos 300 segundos de datos
                    if len(self.data_storage) > 300 * self.fm:  # 300 segundos
                        self.data_storage.pop(0)  # Elimina el más antiguo
                    
                dfH = filtfilt(self.b, self.a, self.y)
                dfL = filtfilt(self.c, self.d, self.y)

                if dfL is not None:
                    dfL_normalizada = (dfL - np.min(dfL)) / (np.max(dfL) - np.min(dfL))
                    self.dfL_normalizada = dfL_normalizada  # Almacenar los datos de la gráfica en una variable de instancia
                    
                    self.ax.clear()
                    self.ax.plot(self.x, dfH)
                    self.ax.set_xlim(0, 10)  # Establecer los límites del eje x
                    self.ax.set_ylim(-1500, 1500)  # Establecer los límites del eje y
                    self.ax.set_xlabel("Tiempo (s)")  # Título del eje X
                    self.ax.set_ylabel("Amplitud")  # Título del eje Y
                    self.ax.grid(True)
                    self.canvas.draw()

                    self.ax1.clear()
                    self.ax1.plot(self.x, dfL_normalizada)
                    self.ax1.set_xlim(0, 10)  # Establecer los límites del eje x
                    self.ax1.set_ylim(0, 2)  # Establecer los límites del eje y
                    self.ax1.set_xlabel("Tiempo (s)")  # Título del eje X
                    self.ax1.set_ylabel("Amplitud Normalizada")  # Título del eje Y
                    self.ax1.grid(True)
                    self.canvas1.draw()
              

            if not self.stop_event_ser.is_set():
                threading.Timer(1e-3, self.periodic_thread).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec())

