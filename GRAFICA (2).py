import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, windows
from scipy.fft import fft
from scipy import stats

# Abrir el archivo y leer los datos
with open('datos_grafica_ax.txt', 'r') as f:
    datos = [linea.strip().split(',') for linea in f.readlines()]

# Inicializar listas vacías para almacenar los valores de x y y
x = []
y = []

# Iterar sobre los datos y convertir a valores flotantes
for fila in datos:
    if len(fila) >= 2:  # Verificar si la fila tiene al menos dos valores
        x.append(float(fila[0]))
        y.append(float(fila[1].strip()))  # Eliminar coma trailing

# Gráfica 1: Señal original
plt.figure(figsize=(12, 12))

plt.subplot(4, 1, 1)
plt.plot(x, y, label="Original", color="blue")
plt.xlabel('Tiempo (s)')  # Cambiar etiqueta del eje X
plt.ylabel('Frecuencia (Hz)')  # Cambiar etiqueta del eje Y
plt.title('Señal Original')
plt.xlim(0, 10)
plt.grid(True)

# Función para el filtro Butterworth paso banda
def butter_bandpass(lowcut, highcut, fs, order=7):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    if low < 0:
        low = 0
    if high > 1:
        high = 1
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=7):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

fs = 1000.0  # Frecuencia de muestreo
lowcut = 50  # Frecuencia de corte baja
highcut = 450  # Frecuencia de corte alta

# Gráfica 2: Señal filtrada con Butterworth (sin modificaciones adicionales)
y_filtered = butter_bandpass_filter(y, lowcut, highcut, fs)

plt.subplot(4, 1, 2)
plt.plot(x, y_filtered, label="Filtrada Butterworth", color="green")
plt.xlabel('Tiempo (s)')  # Cambiar etiqueta del eje X
plt.ylabel('Frecuencia (Hz)')  # Cambiar etiqueta del eje Y
plt.title('Señal Filtrada con Butterworth (sin ventanas)')
plt.xlim(0, 10)
plt.grid(True)

# Gráfica 3: Aplicación de ventana Hamming a la señal filtrada en ventanas de 1000ms
window_size_ms = 1000  # Tamaño de la ventana en milisegundos
window_size_samples = int(fs * (window_size_ms / 1000))  # Convertir a muestras

plt.subplot(4, 1, 3)

# Colores personalizados para las diferentes ventanas
colors = plt.cm.viridis(np.linspace(0, 1, 10))  # Utilizar un colormap para más colores

# Lista para almacenar las métricas de cada ventana
metrics = []

# Crear la gráfica de ventanas Hamming
for i in range(0, len(y_filtered), window_size_samples):
    ventana = y_filtered[i:i + window_size_samples]
    if len(ventana) == window_size_samples:
        hamming_window = windows.hamming(window_size_samples)
        y_hamming = ventana * hamming_window
        
        # Calcular la FFT de la ventana
        fft_result = fft(y_hamming)
        freqs = np.fft.fftfreq(len(fft_result), d=1/fs)

        # Obtener magnitudes
        magnitudes = np.abs(fft_result)

        # Filtrar frecuencias positivas
        positive_freqs = freqs[freqs >= 0]
        positive_magnitudes = magnitudes[freqs >= 0]

        # Calcular métricas
        freq_dominante = positive_freqs[np.argmax(positive_magnitudes)]

        # Calcular la frecuencia mediana utilizando la magnitud
        cumulative_sum = np.cumsum(positive_magnitudes)
        median_index = np.searchsorted(cumulative_sum, cumulative_sum[-1] / 2)
        freq_mediana = positive_freqs[median_index]

        std_dev = np.std(ventana)

        metrics.append((freq_dominante, freq_mediana, std_dev))

        # Graficar la ventana Hamming
        plt.plot(x[i:i + window_size_samples], y_hamming, color=colors[i // window_size_samples % 10])  # Color cíclico

# Gráfica 3: Señal filtrada con Butterworth + Ventanas Hamming coloreadas
plt.xlabel('Tiempo (s)')  # Cambiar etiqueta del eje X
plt.ylabel('Frecuencia (Hz)')  # Cambiar etiqueta del eje Y
plt.title('Señal Filtrada con Ventana Hamming (Ventanas de 1000 ms)')
plt.xlim(0, 10)
plt.grid(True)

# Gráfica 4: Espectro de la señal filtrada (potencia)
plt.subplot(4, 1, 4)

# Calcular la FFT de la señal filtrada completa
fft_result_full = fft(y_filtered)
freqs_full = np.fft.fftfreq(len(fft_result_full), d=1/fs)

# Obtener magnitudes
magnitudes_full = np.abs(fft_result_full)

# Calcular la potencia
potencia_full = magnitudes_full ** 2

# Filtrar frecuencias positivas
positive_freqs_full = freqs_full[freqs_full >= 0]
positive_potencia_full = potencia_full[freqs_full >= 0]

plt.plot(positive_freqs_full, positive_potencia_full, color='orange')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Potencia')
plt.title('Espectro de la Señal Filtrada (Potencia)')
plt.grid(True)

# Guardar las gráficas en un archivo PNG
plt.tight_layout()
plt.savefig('graficas_señal.png')  # Guardar el archivo como PNG
plt.show()

# Imprimir métricas de cada ventana (sin frecuencia media)
for index, (f_dominante, f_mediana, std) in enumerate(metrics):
    print(f"Ventana {index + 1}: Frecuencia Dominante = {f_dominante:.2f} Hz, Frecuencia Mediana = {f_mediana:.2f} Hz, Desviación Estándar = {std:.2f}")

# Calcular promedios de las métricas
promedios = np.mean(metrics, axis=0)

print(f"\nPromedios:\nFrecuencia Dominante Promedio = {promedios[0]:.2f} Hz, Frecuencia Mediana Promedio = {promedios[1]:.2f} Hz, Desviación Estándar Promedio = {promedios[2]:.2f}")

# --- PRUEBA DE HIPÓTESIS ---

# Extraer las frecuencias dominantes de las métricas
frecuencias_dominantes = [f_dominante for f_dominante, f_mediana, std in metrics]

# Establecer un valor de referencia para la prueba de hipótesis (por ejemplo, 100 Hz)
valor_referencia = 170

# Realizar la prueba t de una muestra
t_stat, p_value = stats.ttest_1samp(frecuencias_dominantes, valor_referencia)

# Definir el nivel de significancia
alpha = 0.05

# Mostrar resultados
print(f"\nPrueba de Hipótesis:")
print(f"Media de las frecuencias dominantes: {np.mean(frecuencias_dominantes):.2f} Hz")
print(f"Desviación estándar: {np.std(frecuencias_dominantes):.2f} Hz")
print(f"Estadístico t: {t_stat:.2f}")
print(f"Valor p: {p_value:.4f}")

if p_value < alpha:
    print("Rechazamos la hipótesis nula (H₀). La media de las frecuencias dominantes es significativamente diferente a 100 Hz.")
else:
    print("No podemos rechazar la hipótesis nula (H₀). La media de las frecuencias dominantes no es significativamente diferente a 100 Hz.")
