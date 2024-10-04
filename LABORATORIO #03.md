![image](https://github.com/user-attachments/assets/f2941758-b04d-4603-869f-310db10e2c8d)
**Informe #03, “Señales Electromiográficas EMG ” :**

Lauren Blanco, Sofía Suárez – 5600585 (est.lauren.blanco@unimilitar.edu.co)

Oscar Acero, David Sarmiento – 5600602(est.oscar.acero@unimilitar.edu.co)

Laboratorio de Procesamiento Digítal de Señales

Doc. Andrea Carolina Corredor Bedoya

04 de Octubre 2024

---
**1.	Resumen:**  A lo largo del desarrollo práctico el presente laboratorio, busca analizar la detección de la fatiga muscular a través del análisis de señales electromiográficas (EMG). Se adquirieron señales EMG de músculos en diferentes estados de fatiga y se sometieron a un proceso de limpieza y filtrado para eliminar el ruido. Posteriormente, se realizó un análisis espectral para identificar patrones característicos asociados con la fatiga. Al extraer características relevantes del espectro de potencia y entrenar modelos de aprendizaje automático, se buscó desarrollar un sistema capaz de clasificar las señales EMG en estados de fatiga y no fatiga. Los resultados de este estudio podrían tener aplicaciones en diversas áreas, como la fisioterapia, el entrenamiento deportivo y la ergonomía, permitiendo una evaluación más objetiva y temprana de la fatiga muscular.

  **Palabras Claves:** Caracterización, Electrodos, Espectro de la Señal, Fatiga Muscular, Filtrado, FFT (Transformada Rápida de Fourier), Señales EMG, Ventana Hanning.
  
---  

**2.Objetivo de la Práctica:** Aplicar el filtrado de señales continuas para procesar una señal electromigráfica y detectar la fatiga muscular a través del análisis espectral de la misma. 

--- 
**3. Introducción:** El electromiograma (EMG) es una grabación de la actividad eléctrica de los músculos, también llamada actividad mioeléctrica. Existen dos tipos de EMG, el de superficie y el intramuscular o de aguja.  Para poder realizar la captura de las señales mioeléctricas se utilizan dos electrodos activos y un electrodo de tierra. En el caso de los electrodos de superficie, deben ser ubicados en la piel sobre el músculo a estudiar, mientras que el electrodo de tierra se conecta a una parte del cuerpo eléctricamente activa. La señal EMG será la diferencia entre las señales medidas por los electrodos activos.   La respuesta impulsiva puede ser calculada relacionando la corriente generada en un punto de la fibra muscular y algunas variables relacionadas con la posición de los electrodos (Devasahayam, 2013). La ecuación (1) muestra la forma de calcular la respuesta impulsiva del potencial de acción medido con electrodos de superficie. 

![image](https://github.com/user-attachments/assets/aabcc808-b96d-45d1-aea5-ff30afa3efd0)

Donde 𝐼0 es la corriente en un punto de la fibra, 𝜎 es la conductividad de la piel, 𝑑 es la distancia entre la superficie de la piel y la fibra muscular, 𝑤 es la distancia entre los electrodos y 𝑥 es la distancia desde el punto medio de los electrodos, hasta el punto por el que pasa la corriente; como este punto es variable; se puede considerar que la fuente de corriente inicia en el punto 𝑧 y se mueve con una velocidad 𝑢 en un tiempo 𝑡; por lo tanto 𝑥 = 𝑧−𝑢𝑡. Los parámetros mencionados son descritos en la Figura 1. 

![image](https://github.com/user-attachments/assets/f7ec16b9-11f2-4679-9a20-96460996192d)

---
**4.Procedimiento, Desarrollo y Análisis:**

**¿Qué es la Técnica de Electromiográfia (EMG)?**
La electromiografía (EMG) es una prueba médica que permite evaluar la salud de los músculos y los nervios que los controlan. Esta técnica consiste en registrar la actividad eléctrica que genera los músculos, tanto en reposo como durante la contracción. 

![image](https://github.com/user-attachments/assets/f0fd69e1-e9a6-4a96-9010-560b07003865)

**Figura #03.Principio de la Técnica Electromiografía (EMG). Extraida de Cleveland**

Para desarrollar la técnica en mención, se tienen en cuenta los siguientes factores que resultan importantes para los resultados:

**4.1 Preparación del Sujeto:** 

Antes de comenzar el registro de señales electromiográficas (EMG), es crucial preparar adecuadamente al sujeto para garantizar la calidad de los datos obtenidos. Esta etapa incluye una serie de paso a paso que se muestra acontinuación:

* **Limpieza de la piel:** La piel se limpia con alcohol para eliminar suciedad que puedan interferir con la señal.

* **Colocación de electrodos:** Los electrodos se colocan sobre la piel de acuerdo a la ubicación de los músculos a evaluar. La posición de los electrodos es crucial para obtener una señal de calidad.
  
* **Fijación:** Los electrodos se fijan a la piel con cinta adhesiva o gel conductor para asegurar un buen contacto eléctrico.

**Nota Importante:** La preparación del paciente es un aspecto fundamental para garantizar la calidad de los datos obtenidos en una EMG. Un buen protocolo de preparación minimizará el ruido y las interferencias en la señal, lo que permitirá obtener resultados más precisos y confiables.

Ballesteros en su tesis "Diseño de una plataforma multicanal para el registro de señales EMG" expone los primeros pasos para lograr la adquisición de señales electromiográficas del musculo desde alternativas de fácil acondicionamiento que permita conocer información relevante y automatizada de la señal respecto al tiempo de prueba, de la forma en como se origina y el tipo de clasificación y cuantificación que esta conlleva para obtener el resultado.

**4.2 Sistema de Adquisición de Datos DAQ:**

Un sistema de adquisición de datos (DAQ) es esencial para capturar, procesar y analizar las señales eléctricas generadas por los músculos durante una electromiografía (EMG). Este sistema actúa como un puente entre los electrodos colocados en el cuerpo y la programación donde se almacenan y analizan los datos.

* **Componentes Clave de un Sistema DAQ para la Electromiográfia (EMG):**

1. **Electrodos:** El electrodo es usado como el  conductor eléctrico que establece contacto con un material no metálico en un circuito. Es como un puente que permite que la corriente eléctrica fluya entre un circuito eléctrico y otro medio.
En la técnica de la electromiografía (EMG) se utilizan electrodos para detectar señales eléctricas del musculo en estudio, para esto se utilizaron electrodos de superficie por que son menos invasivos, es decir, no necesitan ajugas y reducen el riesgo de infección, ademas de que son fáciles de posicionar en el musculo, su función principal es detectar y registrar la actividad eléctrica producida por los músculos.

![image](https://github.com/user-attachments/assets/0d821206-7057-4073-a13c-fdc07d94a1d0) 

**Figura #04.Electrodos de Superficie para Electromiográfia (EMG). Extraida de Oxdea**

2. **Microcontrolador STM32:** El uso del microcontrolador stm32, fue útil ya que mediante este se  toma la adquisición de la señal es aqui donde se  configuraron los pines necesarios  para leer datos del sensor AD8232 de electromiográfia, logrando la comunicación entre la respuesta y la interfaz.

![image](https://github.com/user-attachments/assets/3ed47807-bcd5-4c81-9b78-a7f8dc9c021c)

**Figura #05.Periferico Programado desde la STM32. Extraida de CUBEID**

3. **Sensor AD8232:** El AD8232 es un amplificador operacional de instrumentación especialmente diseñado para la adquisición de señales EMG, el cual fue util debido a que la  EMG es una señal muy débil y está rodeada de ruido. El AD8232 utiliza una configuración diferencial para amplificar la diferencia de voltaje entre dos electrodos colocados en la piel. Esto permite rechazar el ruido común presente en ambos electrodos, mejorando significativamente la relación señal-ruido, pues cuando este realiza la tarea de amplificar lo hace en una amplia banda de frecuencias, lo que permite capturar los diferentes componentes de la señal EMG, desde las frecuencias bajas hasta las altas.

![image](https://github.com/user-attachments/assets/bcd1edc9-e59e-4703-a961-0cc06f443f42)

**Figura #06. Sensor AD8232 . Extraida de Componentes101**

**Nota Importante:** Tenga en cuenta que en el siguiente enlace encontrara  el Datasheet del Sensor AD8232 https://www.alldatasheet.com/datasheet-pdf/pdf/527942/AD/AD8232.html

A continuación, se muestra el sistema de adquisición haciendo uso de los componentes anteriores:

![image](https://github.com/user-attachments/assets/7615366a-d0e6-4720-8827-5e1d109d464a)

**Figura #07. Sistema de Adquisición de EMG. Elaboración propia**

**4.3 Selección del Musculo "Biceps" y Calculo de Frecuencia de Muestreo:** 
Para este laboratorio, se hizo selección del musculo del Biceps debido a que es de los mas comparados en la tecnica de electromiografía (EMG), ya que juega un papel clave en la flexión del codo y otros movimientos del brazo. Para estudiar su actividad electromiográfica de manera adecuada, es esencial capturar y analizar correctamente las señales EMG, y un aspecto crucial de este proceso es determinar la frecuencia de muestreo adecuada. La señal EMG es el resultado de la actividad eléctrica generada por los potenciales de acción de las fibras musculares durante la contracción muscular. La señal EMG del bíceps, al igual que en otros músculos, está compuesta por una mezcla de frecuencias que representan la actividad eléctrica del músculo. 

Para capturar adecuadamente una señal EMG, es necesario aplicar el teorema de muestreo de Nyquist el cual explica el principio de establecer que la frecuencia de muestreo debe ser al menos el doble de la frecuencia máxima presente en la señal:

![image](https://github.com/user-attachments/assets/29df32c4-3ded-429f-b518-a31e3095ac46)

Donde:

* fs es la frecuencia de muestreo.
* 𝑓max es la frecuencia máxima de la señal.

En el caso del bíceps, si la señal EMG tiene componentes de frecuencia de hasta 500 Hz, la frecuencia de muestreo mínima que debe

![image](https://github.com/user-attachments/assets/ef3ecbd3-5a53-4272-9422-7f30bfe4e7fa)

Esto significa que la frecuencia de muestreo mínima recomendada para capturar adecuadamente la señal EMG del músculo bíceps es de 1000 Hz.
  
**4.4 Registro de la señal Electromiográfica EMG:**

Para el registro de la señal Electromiográfica, se captura la actividad eléctrica muscular (EMG) de manera continua a lo largo de toda la prueba. Esta señal biológica es adquirida por la STM32 y los datos recolectados son enviados en tiempo real a una interfaz gráfica desarrollada en Python utilizando Qt Designer. Esta interfaz visual permite al usuario observar instantáneamente las variaciones en la señal EMG, facilitando así el análisis y la interpretación de los resultados durante el experimento.

A continuación, se muestra una parte del codigo de la STM32, donde se implementa un sistema básico de adquisición de señales EMG. En este apartado, se configuran varios periféricos que se encarga de registrar datos del sensor mediante un ADC (Convertidor Analógico-Digital) y transmitirlos a través de USB utilizando la clase CDC (Communication Device Class). Se definen variables para manejar el ADC, DMA y un temporizador, que genera interrupciones a intervalos definidos y asi se envía periódicamente a una computadora a través de una interfaz de comunicación realizada por Q- designer.

![image](https://github.com/user-attachments/assets/3b883070-9047-4fc5-bddc-fefccfd1420a)

**Figura #08.Programación de la STM32. Elaboración propia**

Estos datos de la señal EMG, adquiridos por la STM32 se procesan en tiempo real y como se decia anteriormente son enviados a una interfaz gráfica desarrollada mediante el lenguaje de  Python que se encarga de visualizarlos. Esta interfaz, creada con la librería PyQt, presenta la señal EMG en forma de una gráfica que se actualiza constantemente, permitiendo al monitorear la actividad muscular durante la contracción muscular hasta que llega a fatigarse.

Para comprender mas la señal en la interfaz, se debe entender que la fatiga muscular es una respuesta natural del cuerpo a un esfuerzo físico prolongado o intenso, lo que permitiria visualizar en la toma de la señal son los puntos de contracción de manera más ruidosa, con la aparición de componentes de baja frecuencia y un aumento en la variabilidad de la señal.

![image](https://github.com/user-attachments/assets/f5fb884e-da83-4348-872f-8b20eb7e9a65)

**Figura #09. Interfaz realizada por Q-Designer. Elaboración propia**

![image](https://github.com/user-attachments/assets/dc538107-6fbc-42ab-927f-9b93760bb08b)

**Figura #10.Señal EMG Secuencia Contracción Relajación . Extraida de Literatura**

![image](https://github.com/user-attachments/assets/26cb5ef5-8a32-4328-9417-e9716bac6c20)

**Figura #11.Señal EMG Obtenida Por Sistema de Adquisición en Interfaz Q- Designer . Elaboración Propia**


**4.5 Filtrado de la Señal:**

En el ámbito de las señales, el filtrado consiste en la modificación intencional del espectro de frecuencia de una señal. Esto implica alterar la amplitud de las diferentes componentes frecuenciales que conforman la señal original. Es decir, se seleccionan o eliminar ciertas frecuencias de una señal, con el objetivo de resaltar o atenuar determinadas características.

Para este apartado se hizo uso de dos tipos de filtros, los cuales se explican acontinuación:

* **Filtro Pasa Altos:** Un filtro pasa altos es un sistema que permite el paso de las componentes de frecuencia por encima de una determinada frecuencia de corte (fc), atenuando o bloqueando las componentes de frecuencia por debajo de esa frecuencia. Es decir, este tipo de filtro deja pasar las altas frecuencias y bloquea las bajas.

* **Filtro Pasa Bajos:** Un filtro pasabajos es el complemento del filtro pasaaltos. Permite el paso de las componentes de frecuencia por debajo de una determinada frecuencia de corte (fc), atenuando o bloqueando las componentes de frecuencia por encima de esa frecuencia. Es decir, este tipo de filtro deja pasar las bajas frecuencias y bloquea las altas.

Teniendo en cuenta el uso de los filtros, se muestra a continuación las graficas donde se observa la señal con ruido y la señal ya filtrada:

![image](https://github.com/user-attachments/assets/91a29ec1-9b68-45ef-8782-f39151db86c6)

**Figura #12. Relación Señal sin Filtrar - Señal ya Filtrada . Elaboración Propia**



**4.6 División de la Señal Registrada en Ventanas de Tiempo "Hanning" :**

Para este apartado se hace uso de la técnica de las ventanas Hanning, que explica como desde una función matemática que se aplica a una señal se logra suavizar sus extremos. Esto es especialmente útil en el análisis espectral de señales, donde los abruptos inicios y finales de una señal pueden introducir artefactos en el espectro de frecuencia. Cuando se analiza una señal larga, es común dividirla en segmentos más cortos y aplicar una ventana de Hanning a cada segmento.

La función que se utiliza en el procesamiento de señales para suavizar las discontinuidades en los bordes de un segmento de señal, con la siguiente formula

![image](https://github.com/user-attachments/assets/93532c2b-9d85-4f11-a1f2-ede9cf525705)

Donde:
* w(n), Representa el valor de la ventana en el tiempo n
* N, Es la longitud total de la ventana
* n, Indice que varia desde 0 hasta N-1

![image](https://github.com/user-attachments/assets/8e987acd-9333-4d6a-8ad3-535e5b223d56)

**Figura #13. Código en Python Donde Se Emplea las Ventanas Hanning . Elaboración Propia**

![image](https://github.com/user-attachments/assets/8c9d6c20-b0a9-454c-88fe-3cdf56b276b0)

**Figura #14. Gráfica obtenida al  Emplear las Ventanas Hanning . Elaboración Propia**


**4.7 Análisis Espectral utilizando la Transformada de Fourier (FFT) :**

El análisis espectral de señales electromiográficas (EMG) es una herramienta fundamental para estudiar la actividad muscular. La Transformada de Fourier Rápida (FFT) es una técnica ampliamente utilizada para descomponer una señal en sus componentes de frecuencia, lo que permite obtener información valiosa sobre la actividad muscular.

La función de la transformada de Fourier, permite identificar las frecuencias dominantes en la señal EMG, que están relacionadas con el tipo de fibra muscular activada y el nivel de contracción, pues al analizar el espectro de la señal EMG, se pueden identificar diferentes patrones de activación muscular asociados a distintos movimientos o condiciones.

![image](https://github.com/user-attachments/assets/42c50df5-8097-4b20-b1cc-6935125cd0f5)

**Figura #15. Código en Python Donde Se Emplea la FFT . Elaboración Propia**

![image](https://github.com/user-attachments/assets/7609921f-3b90-44b6-b4a6-f3c35d3d2f45)

**Figura #16. Frecuencia de Ventanas EMG con FFT . Elaboración Propia**

**4.8 Cambio del espectro de la señal en cada ventana conforme se acerca la fatiga muscular, Disminución de la frecuencia mediana**

En este estudio, analizaremos cómo la fatiga muscular se manifiesta en cambios específicos de las señales electromiográficas (EMG). En particular, nos centraremos en dos indicadores clave: la evolución del espectro de la señal en ventanas de tiempo sucesivas y la disminución de la frecuencia mediana a medida que el músculo se fatiga.

Ventana 1: Frecuencia Dominante = 391.00 Hz, Frecuencia Mediana = 252.00 Hz, Desviación Estándar = 162.54

Ventana 2: Frecuencia Dominante = 391.00 Hz, Frecuencia Mediana = 247.00 Hz, Desviación Estándar = 97.72

Ventana 3: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 306.00 Hz, Desviación Estándar = 100.21

Ventana 4: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 249.00 Hz, Desviación Estándar = 579.37

Ventana 5: Frecuencia Dominante = 59.00 Hz, Frecuencia Mediana = 137.00 Hz, Desviación Estándar = 268.79

Ventana 6: Frecuencia Dominante = 67.00 Hz, Frecuencia Mediana = 175.00 Hz, Desviación Estándar = 156.32

Ventana 7: Frecuencia Dominante = 58.00 Hz, Frecuencia Mediana = 164.00 Hz, Desviación Estándar = 272.67

Ventana 8: Frecuencia Dominante = 63.00 Hz, Frecuencia Mediana = 158.00 Hz, Desviación Estándar = 198.68

Ventana 9: Frecuencia Dominante = 68.00 Hz, Frecuencia Mediana = 154.00 Hz, Desviación Estándar = 275.74

Ventana 10: Frecuencia Dominante = 74.00 Hz, Frecuencia Mediana = 150.00 Hz, Desviación Estándar = 212.18

Ventana 11: Frecuencia Dominante = 65.00 Hz, Frecuencia Mediana = 150.00 Hz, Desviación Estándar = 263.76

Ventana 12: Frecuencia Dominante = 79.00 Hz, Frecuencia Mediana = 174.00 Hz, Desviación Estándar = 235.63

Ventana 13: Frecuencia Dominante = 66.00 Hz, Frecuencia Mediana = 151.00 Hz, Desviación Estándar = 281.04

Ventana 14: Frecuencia Dominante = 68.00 Hz, Frecuencia Mediana = 148.00 Hz, Desviación Estándar = 319.10

Ventana 15: Frecuencia Dominante = 64.00 Hz, Frecuencia Mediana = 148.00 Hz, Desviación Estándar = 323.87

Ventana 16: Frecuencia Dominante = 49.00 Hz, Frecuencia Mediana = 166.00 Hz, Desviación Estándar = 310.07

Ventana 17: Frecuencia Dominante = 72.00 Hz, Frecuencia Mediana = 168.00 Hz, Desviación Estándar = 334.60

Ventana 18: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 180.00 Hz, Desviación Estándar = 316.85

Ventana 19: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 178.00 Hz, Desviación Estándar = 257.94

Ventana 20: Frecuencia Dominante = 77.00 Hz, Frecuencia Mediana = 181.00 Hz, Desviación Estándar = 261.25

Ventana 21: Frecuencia Dominante = 391.00 Hz, Frecuencia Mediana = 207.00 Hz, Desviación Estándar = 320.56

Ventana 22: Frecuencia Dominante = 81.00 Hz, Frecuencia Mediana = 151.00 Hz, Desviación Estándar = 358.03

Ventana 23: Frecuencia Dominante = 53.00 Hz, Frecuencia Mediana = 145.00 Hz, Desviación Estándar = 429.80

Ventana 24: Frecuencia Dominante = 70.00 Hz, Frecuencia Mediana = 158.00 Hz, Desviación Estándar = 462.85

Ventana 25: Frecuencia Dominante = 61.00 Hz, Frecuencia Mediana = 171.00 Hz, Desviación Estándar = 441.30

Ventana 26: Frecuencia Dominante = 86.00 Hz, Frecuencia Mediana = 169.00 Hz, Desviación Estándar = 355.48

Ventana 27: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 242.00 Hz, Desviación Estándar = 246.18

Ventana 28: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 248.00 Hz, Desviación Estándar = 252.73

Ventana 29: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 189.00 Hz, Desviación Estándar = 224.02

Ventana 30: Frecuencia Dominante = 64.00 Hz, Frecuencia Mediana = 147.00 Hz, Desviación Estándar = 296.30

Ventana 31: Frecuencia Dominante = 52.00 Hz, Frecuencia Mediana = 172.00 Hz, Desviación Estándar = 284.43

Ventana 32: Frecuencia Dominante = 52.00 Hz, Frecuencia Mediana = 211.00 Hz, Desviación Estándar = 257.59

Ventana 33: Frecuencia Dominante = 64.00 Hz, Frecuencia Mediana = 163.00 Hz, Desviación Estándar = 228.97

Ventana 34: Frecuencia Dominante = 391.00 Hz, Frecuencia Mediana = 184.00 Hz, Desviación Estándar = 238.91

Ventana 35: Frecuencia Dominante = 392.00 Hz, Frecuencia Mediana = 226.00 Hz, Desviación Estándar = 268.57

Ventana 36: Frecuencia Dominante = 53.00 Hz, Frecuencia Mediana = 151.00 Hz, Desviación Estándar = 224.38

Ventana 37: Frecuencia Dominante = 55.00 Hz, Frecuencia Mediana = 136.00 Hz, Desviación Estándar = 235.08


**Promedios:**

**Frecuencia Dominante Promedio** = 170.81 Hz

**Frecuencia Mediana Promedio** = 181.24 Hz

**Desviación Estándar Promedio** = 279.82


**Implementación de  una prueba de hipótesis para verificar si el cambio en la mediana es significativo estadísticamente:**



**5. Análisis de Datos**

Para el análisis de datos, en primer lugar se logra comprender como la tecnica de la electromiografía (EMG) es una herramienta indispensable para evaluar la función del bíceps y otros músculos. Al medir la actividad eléctrica generada durante la contracción muscular, la EMG permite obtener información precisa sobre la fuerza de contracción, la fatiga muscular, lo que nos permite analizar directamente que la señal obtenida  mediante EMG sin filtrar tiene gran cantidad de ruido de alta frecuencia que dificulta la identificación clara de los eventos musculares de contracción y relajación, presentando fluctuaciones de amplitud que en su mayoría no corresponden a actividad muscular real. Este ruido puede ser causado por interferencias externas de los electrodos o del medio, lo que enmascara los patrones relevantes de la señal. Al aplicar un filtrado Butterworth, el ruido se reduce considerablemente, lo que permite visualizar la señal de manera más limpia y estructurada, facilitando la detección de eventos musculares importantes en nuestro caso de estudio contracciones o activaciones que generaban fatiga en el musculo. Sin embargo, el filtrado también puedo haber eliminado componentes de alta frecuencia que podrían contener información útil sobre la información adquirida de los movimientos rápidos, lo que resalta la importancia de ajustar el filtro.

Otro factor que es importante fue el sistema de adquisición de datos (DAQ) ya que fue fundamental en la técnica de electromiografía (EMG) porque permitio la captura, digitalización y procesamiento de la señal eléctrica generada por el biceps que  capta las débiles señales eléctricas generadas en la contracción muscular, asi mismo permitio llevar acabo una amplificación, un correcto filtrao y conversión  de datos entre el sistema y la interfaz, si no se hubiera hecho uso de este se hubieran limitado considerablemente evaluar la función muscular. 

En cuanto al proceso de filtrado, el uso del filtro Butterworth se hizo con el proposito de  eliminar el ruido y las interferencias que pueden contaminar la señal original, permitiendo así obtener una señal más limpia y precisa, Al suavizar la respuesta en frecuencia, este filtro permite aislar la información relevante de la actividad muscular, mejorando significativamente la calidad de la señal que fue mejorado un poco despues se aplica  el uso de la tecnica de aventamiento con la teçnica  de Hanning a la señal. Esta ventana suaviza las discontinuidades en los extremos de los segmentos de datos, enfatizando los componentes centrales que corresponden a los potenciales de acción musculares tras la fatiga del musculo y asi poder reducir las fugas espectrales y mejorar la resolución frecuencial que facilito la identificación de las diferentes componentes de frecuencia presentes en la señal EMG

El análisis para las graficas #13 - #14 evidencia el cambio entre la señal filtrada con Butterworth ya que esta exhibe una forma de onda más limpia y regular, pero aún presenta algunas discontinuidades y fugas espectrales y el ventaneo de hannig que al ser aplicado la ventana de Hanning, se observa una mejora significativa en la suavidad de la señal y una reducción de las discontinuidades en los bordes de cada segmento. Esto se traduce en una estimación del espectro un poco más preciso, lo que facilita la identificación de las diferentes componentes de frecuencia presentes en la señal EMG.

Con lo anterior, se puede analizar que el espectro de potencia obtenido a través de la Transformada Rápida de Fourier (FFT) nos brinda una representación detallada de la composición frecuencial de la señal del musculo biceps, muestra cómo la potencia se distribuye a lo largo de distintas frecuencias. En las frecuencias bajas (<100 Hz), se observan picos significativos que representan la actividad muscular, ya que la mayor parte de la información útil en una señal EMG se encuentra en el rango de 10-150 Hz. Sin embargo, destaca un pico fuerte alrededor de los 400 Hz, que probablemente sea un artefacto o interferencia, como ruido eléctrico, que no fue completamente eliminado durante el filtrado. Después de los 100 Hz, la potencia disminuye rápidamente, lo que indica que las altas frecuencias no deseadas han sido en gran parte eliminadas, salvo por el pico en los 400 Hz, que es el resultado de descomponer la señal en sus componentes de frecuencia.

El análisis de las 37 ventanas de señal EMG revela una variabilidad considerable en las frecuencias dominantes y medianas, sugiriendo una actividad muscular dinámica y cambiante. La alta desviación estándar en muchas ventanas indica una amplia distribución de frecuencias, posiblemente debido a la presencia de diferentes tipos de fibras musculares o a ruido en la señal. Los valores atípicos en la frecuencia dominante podrían indicar eventos transitorios o artefactos. En general, los resultados sugieren una actividad muscular de baja intensidad con momentos de mayor activación. Sin embargo, para una interpretación más precisa, se requiere un análisis más profundo considerando el contexto experimental y el tipo de músculo estudiado.

**6. Conclusiones**
* El estudio demuestra de manera clara que el preprocesamiento de las señales EMG, mediante filtrado Butterworth y ventaneo de Hanning, es fundamental para obtener resultados, pues al eliminar el ruido y las interferencias, se logra una señal más limpia y estructurada, lo que facilita la identificación de los eventos musculares de interés como lo fue la fatiga del musculo.
  
* El uso de la Transformada Rápida de Fourier (FFT) demuestra ser una herramienta analitica para verificar  la composición frecuencial de la señal EMG, pues al descomponer la señal en sus componentes de frecuencia, se puedo identificar las bandas de frecuencia dominantes de concentración de energía en las frecuencias bajas y medias, lo que es típico para la actividad muscular. 

* La técnica de la electromiografía (EMG) si cumple con el hecho de evaluar la salud y función muscular como en nuestro caso fue el biceps, al medir la actividad eléctrica del músculo se lograron visualizar la eficacia de cada momento como lo fue la relajación y contracción mediante el procesamiento de señales.

**7. Bibliografía**

[1]. Corredor,A. (2024). Guia #03 Procesamiento de Señales. UMNG.

[2]. Miyara, F. (2004). Filtros activos. Cátedra de Electrónica III FCEIA-UNR. Rosario.

[3].de Señales usando ventanas, T. A. F. (s/f). Sistemas y Señales I. Edu.ar. Recuperado el 4 de octubre de 2024, de https://www.fceia.unr.edu.ar/tesys/html/Analisis_Frecuencial_usando_ventanas.pdf

[4]. Cortés, J. A., Medina, F. A., & Chaves, J. A. (2007). Del análisis de fourier a las wavelets análisis de fourier. Scientia et technica, 1(34).

[5].Báez, M. E., García, A. M., & Carrera, J. M. E. (2008). Análisis espectral mediante el uso de la FFT.

[6]. Mena, A. O., Yolanda, G., Cano, V., & Tizayuca-pachuca, F. (2014). Adquisición y procesamiento de una señal electromiográfica para control de una prótesis. Universidad Autónoma Del Estado de Hidalgo, XXIX, 2, 1-8.


