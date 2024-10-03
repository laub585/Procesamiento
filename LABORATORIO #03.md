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
**Figura #02.Principio de la electromiografía (EMG). Extraida de Cleveland**







**4.1 Preparación del Sujeto:** Antes de comenzar el registro de señales electromiográficas (EMG), es crucial preparar adecuadamente al sujeto para garantizar la calidad de los datos obtenidos. Esta etapa incluye una serie de paso a paso que se muestra acontinuación:

* **Limpieza de la piel:** La piel se limpia con alcohol para eliminar suciedad que puedan interferir con la señal.

* **Colocación de electrodos:** Los electrodos se colocan sobre la piel de acuerdo a la ubicación de los músculos a evaluar. La posición de los electrodos es crucial para obtener una señal de calidad.
  
* **Fijación:** Los electrodos se fijan a la piel con cinta adhesiva o gel conductor para asegurar un buen contacto eléctrico.

**Nota Importante:** La preparación del paciente es un aspecto fundamental para garantizar la calidad de los datos obtenidos en una EMG. Un buen protocolo de preparación minimizará el ruido y las interferencias en la señal, lo que permitirá obtener resultados más precisos y confiables.

Ballesteros en su tesis "Diseño de una plataforma multicanal para el registro de señales EMG"[6]expone los primeros pasos para lograr la adquisición de señales electromiográficas del musculo desde alternativas de fácil acondicionamiento que permita conocer información relevante y automatizada de la señal respecto al tiempo de prueba, de la forma en como se origina y el tipo de clasificación y cuantificación que esta conlleva para obtener el resultado.
**4.2 Sistema de Adquisición de Datos DAQ:**
