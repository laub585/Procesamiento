import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks, cwt, morlet
import pywt

# Calcular el intervalo de tiempo entre cada muestra
n_muestras = 40761
intervalo = 300 / n_muestras  # Tiempo en segundos entre muestras
frecuencia_muestreo = 1000  # Frecuencia de muestreo en Hz
frecuencia_corte_inferior = 65  # Frecuencia de corte inferior para el filtro pasa-banda en Hz
frecuencia_corte_superior = 200  # Frecuencia de corte superior para el filtro pasa-banda en Hz

# Inicializar listas para los datos
x = []
y = []

# Leer los datos del archivo
with open("datos_grafica_ax.txt", "r") as file:
    for line in file:
        values = line.strip().replace(',', '').split()
        x.append(float(values[0]))  # Si la columna x es la primera
        y.append(float(values[1]))  # Si la columna y es la segunda

# Normalizar los valores de y entre -1 y 1
y_min = min(y)
y_max = max(y)
y_normalized = [(2 * (val - y_min) / (y_max - y_min)) - 1 for val in y]  # Normalización entre -1 y 1

# Definir filtro pasa-banda
def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

# Aplicar el filtro pasa-banda a los datos normalizados
y_filtered = butter_bandpass_filter(y_normalized, frecuencia_corte_inferior, frecuencia_corte_superior, frecuencia_muestreo, order=4)

# Eliminar valores que sean mayores a 0.25
y_filtered_clipped = np.where(y_filtered > 0.25, np.nan, y_filtered)  # Sustituir valores mayores a 0.25 por NaN

# Generar el eje x como el tiempo en segundos
x_tiempo = np.arange(0, len(y) * intervalo, intervalo)

# Graficar la señal filtrada
plt.figure(figsize=(12, 6))
plt.plot(x_tiempo, y_filtered_clipped, color='b')
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Valor Normalizado Filtrado")
plt.title("Gráfica de datos filtrados con pasa-banda de 65 a 200 Hz (Valores > 0.25 eliminados)")
plt.xlim([0, 300])  # Limitar el eje X a 300 segundos
plt.ylim(-1, 1)  # Asegurar que el eje Y esté entre -1 y 1
plt.xticks(np.arange(0, 300, 10))  # Marcas en el eje X cada 10 segundos
plt.grid(True)
plt.show()  # Mostrar la gráfica de la señal filtrada

# Encontrar picos en los datos filtrados
mask = np.isfinite(y_filtered_clipped)  # Crear una máscara para los valores finitos
picos, _ = find_peaks(y_filtered_clipped[mask], height=0.15)
picos_indices = np.where(mask)[0][picos]  # Obtener los índices originales de los picos

# Calcular intervalos R-R (en segundos)
intervalos_rr = np.diff(picos_indices) * intervalo  # Convertir de índice a tiempo

# Calcular media y desviación estándar de los intervalos R-R
media_rr = np.mean(intervalos_rr)
desviacion_std_rr = np.std(intervalos_rr)

# Imprimir los valores de los intervalos R-R
for i, rr in enumerate(intervalos_rr):
    print(f"Intervalo R-R {i + 1}: {rr:.3f} segundos")

# Calcular la transformada wavelet continua usando la wavelet de Morlet
fs = 1 / np.mean(intervalos_rr)  # Frecuencia de muestreo basada en intervalos R-R
frecuencias = np.linspace(0.04, 0.15, 300)  # Rango LF y HF Hz
escalas = pywt.scale2frequency('cmor', 1) / (frecuencias * fs)

coeficientes, _ = pywt.cwt(intervalos_rr, escalas, 'cmor')

# Graficar el espectrograma
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(coeficientes), extent=[0, len(intervalos_rr), frecuencias[-1], frecuencias[0]], 
           cmap='jet', aspect='auto')
plt.colorbar(label='Magnitud')
plt.title('Espectrograma de HRV usando Wavelet Continua (Morlet)')
plt.xlabel('Número de intervalo')
plt.ylabel('Frecuencia (Hz)')
plt.gca().invert_yaxis()  # Invertir el eje Y para que las frecuencias más bajas estén en la parte inferior
plt.xlim([0, 300])  # Limitar el eje X al número de intervalos R-R

plt.show()

# Crear subgráficas de 10 en 10 segundos (opcional)
for start in range(0, 300, 10):
    plt.figure(figsize=(12, 6))
    end = start + 10

    # Filtrar datos del intervalo actual
    mask = (x_tiempo >= start) & (x_tiempo < end)
    x_intervalo = x_tiempo[mask]
    y_intervalo = y_filtered_clipped[mask]

    # Graficar los datos del intervalo
    plt.plot(x_intervalo, y_intervalo, color='b')

    # Encontrar picos en el intervalo actual, ignorando los NaN
    mask_intervalo = np.isfinite(y_intervalo)
    picos_intervalo, _ = find_peaks(y_intervalo[mask_intervalo], height=0.15)
    picos_tiempo = x_intervalo[mask_intervalo][picos_intervalo]

    # Resaltar picos en la subgráfica
    plt.scatter(picos_tiempo, y_intervalo[mask_intervalo][picos_intervalo], color='red', label='Picos', zorder=5)

    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Valor Normalizado Filtrado")
    plt.title(f"Detalle de {start} a {end} segundos")
    plt.xlim([start, end])
    plt.ylim(-1, 1)  # Asegurar que el eje Y esté entre -1 y 1
    plt.xticks(np.arange(start, end + 0.5, 0.5))
    plt.grid(True)
    plt.legend()
    plt.show()  # Mostrar la subgráfica actual

print(f"Media de intervalos R-R: {media_rr:.3f} segundos")
print(f"Desviación estándar de intervalos R-R: {desviacion_std_rr:.3f} segundos")

