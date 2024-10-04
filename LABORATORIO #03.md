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

**Figura #02.Principio de la Técnica Electromiografía (EMG). Extraida de Cleveland**

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

**Figura #03.Electrodos de Superficie para Electromiográfia (EMG). Extraida de Oxdea**

2. **Microcontrolador STM32:** El uso del microcontrolador stm32, fue útil ya que mediante este se  toma la adquisición de la señal es aqui donde se  configuraron los pines necesarios  para leer datos del sensor AD8232 de electromiográfia, logrando la comunicación entre la respuesta y la interfaz.

![image](https://github.com/user-attachments/assets/3ed47807-bcd5-4c81-9b78-a7f8dc9c021c)

**Figura #04.Periferico Programado desde la STM32. Extraida de CUBEID**

3. **Sensor AD8232:** El AD8232 es un amplificador operacional de instrumentación especialmente diseñado para la adquisición de señales EMG, el cual fue util debido a que la  EMG es una señal muy débil y está rodeada de ruido. El AD8232 utiliza una configuración diferencial para amplificar la diferencia de voltaje entre dos electrodos colocados en la piel. Esto permite rechazar el ruido común presente en ambos electrodos, mejorando significativamente la relación señal-ruido, pues cuando este realiza la tarea de amplificar lo hace en una amplia banda de frecuencias, lo que permite capturar los diferentes componentes de la señal EMG, desde las frecuencias bajas hasta las altas.

![image](https://github.com/user-attachments/assets/bcd1edc9-e59e-4703-a961-0cc06f443f42)

**Figura #05. Sensor AD8232 . Extraida de Componentes101**

**Nota Importante:** Tenga en cuenta que en el siguiente enlace encontrara  el Datasheet del Sensor AD8232 https://www.alldatasheet.com/datasheet-pdf/pdf/527942/AD/AD8232.html

A continuación, se muestra el sistema de adquisición haciendo uso de los componentes anteriores:

![image](https://github.com/user-attachments/assets/7615366a-d0e6-4720-8827-5e1d109d464a)

**Figura #06. Sistema de Adquisición de EMG. Elaboración propia**

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

**Figura #07.Programación de la STM32. Elaboración propia**

Estos datos de la señal EMG, adquiridos por la STM32 se procesan en tiempo real y como se decia anteriormente son enviados a una interfaz gráfica desarrollada mediante el lenguaje de  Python que se encarga de visualizarlos. Esta interfaz, creada con la librería PyQt, presenta la señal EMG en forma de una gráfica que se actualiza constantemente, permitiendo al monitorear la actividad muscular durante la contracción muscular hasta que llega a fatigarse.

Para comprender mas la señal en la interfaz, se debe entender que la fatiga muscular es una respuesta natural del cuerpo a un esfuerzo físico prolongado o intenso, lo que permitiria visualizar en la toma de la señal son los puntos de contracción de manera más ruidosa, con la aparición de componentes de baja frecuencia y un aumento en la variabilidad de la señal.



**Figura #08. Interfaz realizada por Q-Designer. Elaboración propia**

![image](https://github.com/user-attachments/assets/dc538107-6fbc-42ab-927f-9b93760bb08b)

**Figura #09.Señal EMG Secuencia Contracción Relajación . Extraida de Literatura**


**Figura #10.Señal EMG Obtenida Por Sistema de Adquisición en Interfaz Q- Designer . Elaboración Propia**


**4.5 Filtrado de la Señal:**

En el ámbito de las señales, el filtrado consiste en la modificación intencional del espectro de frecuencia de una señal. Esto implica alterar la amplitud de las diferentes componentes frecuenciales que conforman la señal original. Es decir, se seleccionan o eliminar ciertas frecuencias de una señal, con el objetivo de resaltar o atenuar determinadas características.

Para este apartado se hizo uso de dos tipos de filtros, los cuales se explican acontinuación:

* **Filtro Pasa Altos:** Un filtro pasa altos es un sistema que permite el paso de las componentes de frecuencia por encima de una determinada frecuencia de corte (fc), atenuando o bloqueando las componentes de frecuencia por debajo de esa frecuencia. Es decir, este tipo de filtro deja pasar las altas frecuencias y bloquea las bajas.



**Figura #11. Código en Python Donde Se Emplea Filtro Pasa Alto. Elaboración Propia**

* **Filtro Pasa Bajos:** Un filtro pasabajos es el complemento del filtro pasaaltos. Permite el paso de las componentes de frecuencia por debajo de una determinada frecuencia de corte (fc), atenuando o bloqueando las componentes de frecuencia por encima de esa frecuencia. Es decir, este tipo de filtro deja pasar las bajas frecuencias y bloquea las altas.



**Figura #12. Código en Python Donde Se Emplea Filtro Pasa Bajos. Elaboración Propia**

Teniendo en cuenta el uso de los filtros, se muestra a continuación la interfaz y el apartado de las graficas donde se observa la señal con ruido y la señal ya filtrada

![image](https://github.com/user-attachments/assets/91a29ec1-9b68-45ef-8782-f39151db86c6)

**Figura #13. Relación Señal sin Filtrar - Señal ya Filtrada . Elaboración Propia**


**4.6 División de la Señal Registrada en Ventanas de Tiempo "Hanning" :**

Para este apartado se hace uso de la técnica de las ventanas Hanning, que explica como desde una función matemática que se aplica a una señal se logra suavizar sus extremos. Esto es especialmente útil en el análisis espectral de señales, donde los abruptos inicios y finales de una señal pueden introducir artefactos en el espectro de frecuencia. Cuando se analiza una señal larga, es común dividirla en segmentos más cortos y aplicar una ventana de Hanning a cada segmento.

La función que se utiliza en el procesamiento de señales para suavizar las discontinuidades en los bordes de un segmento de señal, con la siguiente formula

![image](https://github.com/user-attachments/assets/93532c2b-9d85-4f11-a1f2-ede9cf525705)

Donde:
* w(n), Representa el valor de la ventana en el tiempo n
* N, Es la longitud total de la ventana
* n, Indice que varia desde 0 hasta N-1

![image](https://github.com/user-attachments/assets/8e987acd-9333-4d6a-8ad3-535e5b223d56)

**Figura #14. Código en Python Donde Se Emplea las Ventanas Hanning . Elaboración Propia**

![image](https://github.com/user-attachments/assets/8c9d6c20-b0a9-454c-88fe-3cdf56b276b0)

**Figura #15. Gráfica obtenida al  Emplear las Ventanas Hanning . Elaboración Propia**


**4.7 Análisis Espectral utilizando la Transformada de Fourier (FFT) :**

El análisis espectral de señales electromiográficas (EMG) es una herramienta fundamental para estudiar la actividad muscular. La Transformada de Fourier Rápida (FFT) es una técnica ampliamente utilizada para descomponer una señal en sus componentes de frecuencia, lo que permite obtener información valiosa sobre la actividad muscular.

La función de la transformada de Fourier, permite identificar las frecuencias dominantes en la señal EMG, que están relacionadas con el tipo de fibra muscular activada y el nivel de contracción, pues al analizar el espectro de la señal EMG, se pueden identificar diferentes patrones de activación muscular asociados a distintos movimientos o condiciones.

![image](https://github.com/user-attachments/assets/42c50df5-8097-4b20-b1cc-6935125cd0f5)

**Figura #15. Código en Python Donde Se Emplea la FFT . Elaboración Propia**

![image](https://github.com/user-attachments/assets/7609921f-3b90-44b6-b4a6-f3c35d3d2f45)

**Figura #16. Frecuencia de Ventanas EMG con FFT . Elaboración Propia**

**5. Análisis de Datos**

Para el análisis de datos, en primer lugar se logra comprender como la tecnica de la electromiografía (EMG) es una herramienta indispensable para evaluar la función del bíceps y otros músculos. Al medir la actividad eléctrica generada durante la contracción muscular, la EMG permite obtener información precisa sobre la fuerza de contracción, la fatiga muscular, lo que nos permite analizar directamente que la señal obtenida  mediante EMG sin filtrar tiene gran cantidad de ruido de alta frecuencia que dificulta la identificación clara de los eventos musculares de contracción y relajación, presentando fluctuaciones de amplitud que en su mayoría no corresponden a actividad muscular real. Este ruido puede ser causado por interferencias externas de los electrodos o del medio, lo que enmascara los patrones relevantes de la señal. Al aplicar un filtrado Butterworth, el ruido se reduce considerablemente, lo que permite visualizar la señal de manera más limpia y estructurada, facilitando la detección de eventos musculares importantes en nuestro caso de estudio contracciones o activaciones que generaban fatiga en el musculo. Sin embargo, el filtrado también puedo haber eliminado componentes de alta frecuencia que podrían contener información útil sobre la información adquirida de los movimientos rápidos, lo que resalta la importancia de ajustar el filtro.

Otro factor que es importante fue el sistema de adquisición de datos (DAQ) ya que fue fundamental en la técnica de electromiografía (EMG) porque permitio la captura, digitalización y procesamiento de la señal eléctrica generada por el biceps que  capta las débiles señales eléctricas generadas en la contracción muscular, asi mismo permitio llevar acabo una amplificación, un correcto filtrao y conversión  de datos entre el sistema y la interfaz, si no se hubiera hecho uso de este se hubieran limitado considerablemente evaluar la función muscular. 

En cuanto al proceso de filtrado, el uso del filtro Butterworth se hizo con el proposito de  eliminar el ruido y las interferencias que pueden contaminar la señal original, permitiendo así obtener una señal más limpia y precisa, Al suavizar la respuesta en frecuencia, este filtro permite aislar la información relevante de la actividad muscular, mejorando significativamente la calidad de la señal que fue mejorado un poco despues se aplica  el uso de la tecnica de aventamiento con la teçnica  de Hanning a la señal. Esta ventana suaviza las discontinuidades en los extremos de los segmentos de datos, enfatizando los componentes centrales que corresponden a los potenciales de acción musculares tras la fatiga del musculo y asi poder reducir las fugas espectrales y mejorar la resolución frecuencial que facilito la identificación de las diferentes componentes de frecuencia presentes en la señal EMG

El análisis para las graficas # - #

El análisis de las 37 ventanas de señal EMG revela una variabilidad considerable en las frecuencias dominantes y medianas, sugiriendo una actividad muscular dinámica y cambiante. La alta desviación estándar en muchas ventanas indica una amplia distribución de frecuencias, posiblemente debido a la presencia de diferentes tipos de fibras musculares o a ruido en la señal. Los valores atípicos en la frecuencia dominante podrían indicar eventos transitorios o artefactos. En general, los resultados sugieren una actividad muscular de baja intensidad con momentos de mayor activación. Sin embargo, para una interpretación más precisa, se requiere un análisis más profundo considerando el contexto experimental y el tipo de músculo estudiado.

**6. Conclusiones**
*


*


*

**7. Bibliografía**
[1]. 
[2]. 
