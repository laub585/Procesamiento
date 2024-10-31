![image](https://github.com/user-attachments/assets/866bb4ce-ad70-43a6-9a8e-6a584c5093f2)

Informe #04, “Variabilidad de la Frecuencia Cardiaca Usando la Transformada Wavelet ” :

Lauren Blanco, Sofía Suárez – 5600585 (est.lauren.blanco@unimilitar.edu.co)

Oscar Acero, David Sarmiento – 5600602(est.oscar.acero@unimilitar.edu.co)

Laboratorio de Procesamiento Digítal de Señales

Doc. Andrea Carolina Corredor Bedoya

01 de Noviembre 2024

----
**1. Resumen:** A lo largo del desarrollo práctico el presente laboratorio, busca analizar la utilidad de la Transformada Wavelet en el análisis de la variabilidad de la frecuencia cardíaca (VFC). Se registraron señales electrocardiográficas bajo diferentes condiciones fisiológicas para evaluar cómo la VFC refleja cambios en el estado fisiológico. Mediante la aplicación de la Transformada Wavelet, se descompuso la señal en diferentes escalas de tiempo y frecuencia, permitiendo una caracterización detallada de los patrones de variabilidad. Los resultados obtenidos sugieren que la VFC, analizada a través de Wavelets, puede ser un biomarcador sensible para detectar cambios en el estado autonómico, con potenciales aplicaciones en la evaluación del estrés, la recuperación física y la detección temprana de enfermedades cardiovasculares."

**Palabras Claves**: Condiciones fisiológicas, electrocardiograma, escalas de tiempo y frecuencia,  estado fisiológico, patrones de variabilidad, señales, Transformada Wavelet, Variabilidad de la Frecuencia Cardíaca (VFC).

----
**2.Objetivo de la Práctica:**
Analizar la variabilidad de la frecuencia cardíaca (HRV) utilizando la transformada wavelet para identificar cambios en las frecuencias características y analizar la dinámica temporal de la señal cardíaca. 

----
**3. Procedimiento, Desarrollo y Análisis:**
A continuación, se detallará la metodología empleada en la ejecución del presente experimento. Se describirá paso a paso el procedimiento seguido hasta la obtención y análisis de los datos:

**3.1 Fundamentación Teórica:**
   **3.1.1  Actividad Simpática y Parasimpática del Sistema Nervioso Autónomo y Relación con la Frecuencia Cardiaca:**

La bibliografía médica [1], subraya la importancia del sistema nervioso autónomo (SNA) como un componente fundamental del sistema nervioso, encargado de funciones regulares involuntarias que son esenciales para la supervivencia del ser humano. Este sistema opera de manera automática, gestionando procesos vitales como la frecuencia cardíaca, la respiración, la digestión y la respuesta al estrés, sin requerir la inteligencia.
 
El sistema nervioso autónomo se divide en dos ramas principales: **el sistema simpático y el sistema parasimpático**. El sistema simpático se activa en situaciones de peligro o estrés, desencadenando respuestas de "lucha o huida" que aumentan la frecuencia cardíaca que movilizan recursos energéticos para preparar al organismo ante posibles amenazas. En contraste, el sistema parasimpático promueve la relajación y la recuperación, reduciendo la frecuencia cardíaca y favoreciendo el descanso, contribuyendo así al mantenimiento del equilibrio.

![Sistema Simpático Y Parasimpatico (1)](https://github.com/user-attachments/assets/644976d9-8b50-456a-9c9e-6131b9b21c44)

**Figura #01. División del Sistema Nervioso Autónomo "Simpático y Parásimpatico"**

Con lo mencionado anteriormente, el sistema nervioso autónomo (SNA) juega un papel fundamental en la regulación de diversas funciones corporales, entre ellas la frecuencia cardíaca. Las dos divisiones ejercen efectos opuestos sobre el corazón.

Para iniciar con la explicación de como se relaciona el SNA con la Frecuencia Cardiaca, la Fundación Española del Corazón [2], explica que la frecuencia cardiaca es el número de veces que se contrae el corazón durante un minuto (latidos por minuto). Por tanto, la interacción del sistema recae cuando existen ciertas situaciones que afectan la neutralidad del ser humano, en el caso del sistema simpático reacciona en situaciones de estrés o peligro lo que desencadena efectos sobre la frecuencia cardiaca de la siguiente manera:

 * **Aumento de la frecuencia cardíaca:** Al activarse el sistema simpático, se liberan neurotransmisores como la noradrenalina, que actúan sobre el corazón aumentando la frecuencia de contracción. Esto permite un mayor bombeo de sangre hacia los músculos y órganos que necesitan más oxígeno y nutrientes durante una situación de estrés.

 * **Aumento de la fuerza de contracción:** Además de aumentar la frecuencia cardíaca, el sistema simpático también aumenta la fuerza con la que el corazón se contrae, lo que mejora el gasto cardíaco.

Mientras que en el sistema parásimpatico, lo que desencadena es la relajación y la conservación de energía, por tanto la frecuencia cardiaca tiende a presentar las siguientes caracteristicas:

* **Disminución de la frecuencia cardíaca:** El neurotransmisor principal del sistema parasimpático es la acetilcolina, que actúa sobre el corazón reduciendo la frecuencia de contracción. Esto permite al cuerpo descansar y recuperarse.

* **Disminución de la fuerza de contracción:** Al igual que con la frecuencia cardíaca, el sistema parasimpático también disminuye la fuerza de contracción del corazón.

<img width="395" alt="bgf-e1676736279720 (2)" src="https://github.com/user-attachments/assets/ce1748b2-99a1-4719-b636-18a2f33accab">

**Figura #02. Efecto de la estimulación simpática y parasimpática sobre la frecuencia cardíaca.Extraído de Homo Medicus"**

Lo que permite comprender la imágen anterior, es que el corazón recibe inervación tanto del sistema nervioso simpático como del parasimpático. Los nervios vagos (parasimpáticos) se concentran en los nódulos del corazón, mientras que los nervios simpáticos se distribuyen ampliamente por todo el músculo cardíaco[3].

 **3.1.2 Variabilidad de la Frecuencia Cardiaca (HRV) :**
 
La variabilidad de la frecuencia cardíaca (HRV) es una medida cuantitativa de las fluctuaciones inter-latido del corazón, reflejando la modulación autonómica del nodo sinoauricular. Estas variaciones, lejos de ser aleatorias, son el resultado de la compleja interacción entre el sistema nervioso simpático y parasimpático. La HRV es un biomarcador no invasivo que proporciona información sobre la homeostasis cardiovascular, la capacidad de respuesta al estrés y la regulación autonómica. Un análisis detallado de los componentes de frecuencia de la HRV permite inferir sobre la predominancia tónica simpática o parasimpática, así como sobre la flexibilidad de la modulación autonómica en respuesta a diferentes estímulos [4].

Para comprende esta variabilidaad, normalmente lo que se hace es hacer uso de la técnica del electrocardiograma (ECG) con el fin de de medir la actividad eléctrica del corazón y permite a su vez determinar el normal funcionamiento del mismo.  Para medir estas fluctuaciones cardiacas, se tiene en cuenta condiciones derivadas de  los procesos de los sistemas nerviosos simpático y parasimpático (Maud y Foster, 1991). Las fluctuaciones de la frecuencia cardiaca son comúnmente valoradas por las mediciones del intervalo R­R, mediante la variación del tiempo de este intervalo es comúnmente llamada Variabilidad de la Frecuencia Cardiaca (HRV) como se
muestran acontinuación:

![WhatsApp Image 2024-10-30 at 9 46 06 PM (1) (1)](https://github.com/user-attachments/assets/0bf7f50e-e55a-49ae-939d-ec358a6f9f59)

**Figura #03. Representación esquemática de un intervalo R­R Tomado de: Maud PJ. , Foster C. Physiological assessment of human fitness.
Second Edition. 2006; (41)"**

* **¿Cómo Se Mide La Variabilidad de la Frecuencia Cardiaca (HRV)?**
  
Para medir la variabilidad de la frecuencia cardiaca (HRV), se puede realizar diferentes métodos de medidas. Entre ellos encontramos medidas estáticas que se dan en el análisis del tiempo dominante, o también se puede emplear métodos geométricos y análisis espectral que se da mediante el análisis de la frecuencia dominante[4].

1. **Análisis del Tiempo Dominante:**

El análisis del tiempo dominio en la variabilidad de la frecuencia cardíaca (HRV) es una herramienta fundamental al analizar directamente los intervalos RR (tiempo entre dos latidos consecutivos), se pueden obtener diversas variables que proporcionan información valiosa sobre la dinámica cardíaca:

* **Promedio R­R (ms)**: Es la media de los intervalos R­R, este dato se obtiene dividiendo la sumatoria de todos los intervalos entre el total de intervalos.
  
* **SDNN (ms):**  Es la desviación estándar de todos los intervalos R­R. Esta variable muestra la variación en cortos y largos periodos en cuanto a la variación en los intervalos R­R (HRV).

Para realizar los cálculos de HRV, es recomendado utilizar no menos de 6 intervalos para comprenderme a mayor profundidad las  diferencias significativas (Task Force of the European Society of Cardiology & the North American Society of Pacing and Electrophysiology, 1996)

2. **Análisis Espectral:**

El análisis espectral se da mediante las frecuencias arrojadas por la técnica del Electrocardiograma (ECG),Este método de análisis se conoce como el espectro permite entender aún más los efectos de los sistemas nervioso simpático y parasimpático sobre la HRV (Akselrod,
1985). Los principales parámetros de medida en el análisis espectral son:

* **Muy baja frecuencia (VLF):** Está alimentado por frecuencias menores a 0.04 Hz.

* **Baja frecuencia (LF):** Son componentes que están alrededor de 0.1 Hz.
  
* **Alta frecuencia (HF):** Componente sincronizado con la frecuencia de respiración. Está sobre un rango de 0.2 a 0.5 Hz dependiendo de la frecuencia respiratoria.

 **3.1.3 Transformada Wavelet:**
 
La transformada wavelet es una técnica matemática que descompone una señal en una serie de funciones básicas llamadas wavelets. A diferencia de la transformada de Fourier, que descompone una señal en componentes sinusoidales de diferentes frecuencias, las wavelets ofrecen una representación más localizada en el tiempo y la frecuencia, lo que las hace particularmente útiles para analizar señales no estacionarias como las biológicas.

Las wavelets son funciones con una duración limitada y un valor promedio cercano a cero. Su forma puede variar, lo que permite adaptar el análisis a diferentes tipos de señales. Al descomponer una señal en wavelets, se obtiene una representación que revela tanto los componentes de baja frecuencia (tendencias a largo plazo) como los de alta frecuencia (detalles locales) [5].

En este laboratorio, haciendo uso de la tecnica del electrocardiograma(ECG) la transformada wavelet permite descomponer una señal compleja en diferentes frecuencias y localizaciones temporales, lo que facilita la identificación de características específicas y la detección de anomalías.

**Tipos de Wavelet para Señales Biologicas:**

* **Wavelet de Haar:** Una de las wavelets más simples, útil para detectar discontinuidades y cambios bruscos en la señal.

* **Wavelets de Daubechies:** Wavelets con diferentes niveles de regularidad, lo que las hace versátiles para una amplia gama de aplicaciones.

* **Wavelet de Morlet:** Wavelet compleja con una forma similar a una onda sinusoidal amortiguada, adecuada para analizar señales con componentes tanto sinusoidales como transitorios.

* **Wavelet de Symlet:** Similar a la wavelet de Daubechies, pero con simetría alrededor de cero.
  
* **Wavelet de Coiflet:*** Wavelet con un número de momentos nulos, lo que la hace útil para aproximar funciones suaves.



 **3.1.4 Diagrama de Flujo. :**
 
A continuación, se presenta un diagrama de flujo que ilustra de manera gráfica y secuencial el proceso practico del presente laboratorio.



**Figura #04. "**



**3.2   Adquisición de la señal ECG**

**¿Qué es la Técnica de Electrocardiografía (ECG)?**

Según la Fundación Española del Corazón[6], define que la técnica de electrocardiografía cumple el principio de  registrar la actividad eléctrica del corazón que se produce en cada latido cardiaco. Esta actividad eléctrica se registra desde la superficie corporal del paciente y se dibuja en un papel mediante una representación gráfica o trazado, donde se observan diferentes ondas que representan los estímulos eléctricos de las aurículas y los ventrículos.

Para esta técncia, se hace una segmentación por las siguientes fases que describe la actividad eléctrica del corazón:

* **Onda P:** Representa la despolarización de las aurículas, es decir, la contracción de las cámaras superiores del corazón para enviar sangre a los ventrículos.

* **Complejo QRS:** Representa la despolarización de los ventrículos, que son las cámaras inferiores del corazón. Esta es la contracción más fuerte y propulsa la sangre hacia el cuerpo y los pulmones.

* **Onda Q:** Primera deflexión negativa del complejo.

* **Onda R:** Primera deflexión positiva del complejo.
  
* **Onda S:** Segunda deflexión negativa del complejo (si existe).

* **Onda T:** Representa la repolarización de los ventrículos, es decir, el momento en que las células del corazón se relajan y se preparan para la siguiente contracción.

![image](https://github.com/user-attachments/assets/8a87aa5b-a163-4f87-a295-4ce85d43fe67)

**Figura #06. Representación esquemática de un Electrocardiograma y su composición por Complementos. (rodriguez. 2008.)"**

Para desarrollar la técnica en mención, se tienen en cuenta los siguientes factores que resultan importantes para los resultados:

**3.2.2  Preparación del Sujeto:**

Antes de comenzar el registro de señales ECG, es crucial preparar adecuadamente al sujeto para garantizar la calidad de los datos obtenidos. Esta etapa incluye una serie de paso a paso que se muestra acontinuación:

**1. Limpieza de la piel:** La piel se limpia con alcohol para eliminar suciedad que puedan interferir con la señal.

**2. Colocación de electrodos:** Los electrodos se colocan sobre la piel de acuerdo a la ubicación de las derivaciones a evaluar. La posición de los electrodos es crucial para obtener una señal de calidad.

**3.Fijación:** Los electrodos se fijan a la piel con cinta adhesiva o gel conductor para asegurar un buen contacto eléctrico.

**Nota Importante:** La preparación del paciente es un aspecto fundamental para garantizar la calidad de los datos obtenidos en una EMG. Un buen protocolo de preparación minimizará el ruido y las interferencias en la señal, lo que permitirá obtener resultados más precisos y confiables.

Para la realización de este laboratorio, se procedió a colocar los electrodos en las derivaciones precordiales V1 y V2, ubicadas en el cuarto espacio intercostal a la derecha e izquierda del esternón respectivamente, son fundamentales para explorar la activación eléctrica del septo interventricular. Esta zona, que separa los ventrículos izquierdo y derecho, es de gran importancia ya que cualquier alteración en su conducción puede manifestarse en estas derivaciones. La colocación precisa de V1 y V2 es crucial, y se utiliza el ángulo de Louis como punto de referencia que tiene como objetivo simular un electrocardiograma (ECG) estándar, permitiendo la medición individualizada de cada derivación, es importante recordar que el electrodo de tierra, colocado debajo de la costilla, sirve como referencia eléctrica, minimizando el ruido y asegurando una señal limpia y precisa. 

![WhatsApp Image 2024-10-31 at 7 38 18 AM (1)](https://github.com/user-attachments/assets/ac7fbca9-cca2-435b-b89a-6c75b13ba511)

**Figura #07. Representación esquemática de Posiciones de Electrodos V1, V2 , Tierra. Guiada de Neotecnia "**


**3.2.3 Sistema de Adquisición de Datos DAQ:**

Un sistema de adquisición de datos (DAQ) es esencial para capturar, procesar y analizar las señales eléctricas generadas por el corazón  durante una electrocardiografía (ECG). Este sistema actúa como un puente entre los electrodos colocados en el cuerpo y la programación donde se almacenan y analizan los datos [7].

* **Componentes Clave de un Sistema DAQ para la Electrocardiográfia (ECG):**

1. **Electrodos:** El electrodo es usado como el  conductor eléctrico que establece contacto con un material no metálico en un circuito. Es como un puente que permite que la corriente eléctrica fluya entre un circuito eléctrico y otro medio.

En la técnica del electrocardiograma (ECG) se utilizan electrodos para detectar las señales eléctricas producidas por el corazón. Estos electrodos se colocan en la superficie de la piel, haciendo de esta una técnica no invasiva y segura para el paciente. La colocación de estos electrodos es relativamente sencilla y permite registrar la actividad eléctrica del corazón desde diferentes ángulos, proporcionando así una imagen completa de su funcionamiento en nuestro caso de V1 y V2 .

La función principal de los electrodos en el ECG es captar y amplificar las débiles señales eléctricas generadas por el corazón y transmitirlas a un dispositivo que las registra en forma de ondas. Estas ondas, conocidas como trazado electrocardiográfico, proporcionan información valiosa sobre el ritmo cardíaco, la conducción eléctrica y la estructura del corazón

![image](https://github.com/user-attachments/assets/0d821206-7057-4073-a13c-fdc07d94a1d0) 

**Figura #08.Electrodos de Superficie. Extraida de Oxdea**

2. **Microcontrolador STM32:** El uso del microcontrolador stm32, fue útil ya que mediante este se  toma la adquisición de la señal es aqui donde se  configuraron los pines necesarios  para leer datos del sensor AD8232 de electromiográfia, logrando la comunicación entre la respuesta y la interfaz.

![image](https://github.com/user-attachments/assets/3ed47807-bcd5-4c81-9b78-a7f8dc9c021c)

**Figura #09.Periferico Programado desde la STM32. Extraida de CUBEID**

3. **Sensor AD8232:** El AD8232 es un amplificador operacional de instrumentación especialmente diseñado para la adquisición de señales ECG, Este  incorpora amplificadores de instrumentación, filtros y otras características que lo hacen ideal para amplificar y limpiar las señales eléctricas débiles del corazón. Al actuar como preprocesador, el AD8232 prepara la señal ECG para su digitalización y posterior análisis, permitiendo obtener información precisa sobre el ritmo cardíaco, la conducción eléctrica y la estructura del corazón. Su alta ganancia, alta impedancia de entrada y bajo ruido lo convierten en una elección popular para la construcción de circuitos de ECG.

![image](https://github.com/user-attachments/assets/bcd1edc9-e59e-4703-a961-0cc06f443f42)

**Figura #10. Sensor AD8232 . Extraida de Componentes101**

**Nota Importante:** Tenga en cuenta que en el siguiente enlace encontrara  el Datasheet del Sensor AD8232 https://www.alldatasheet.com/datasheet-pdf/pdf/527942/AD/AD8232.html

A continuación, se muestra el sistema de adquisición haciendo uso de los componentes anteriores:

![image](https://github.com/user-attachments/assets/7615366a-d0e6-4720-8827-5e1d109d464a)

**Figura #08. Sistema de Adquisición de ECG. Elaboración propia**


----

**Bibliografía:**

[1].Báez, M. E. (2007). Visión clásica del sistema nervioso autónomo. Universidad de La Habana.

[2].Frecuencia cardiaca. (s/f). Fundación Española del Corazón. Recuperado el 31 de octubre de 2024, de https://fundaciondelcorazon.com/prevencion/marcadores-de-riesgo/frecuencia-cardiaca.html

[3]. Medicus, H. (2024, junio 22). Efecto de la estimulación simpática y parasimpática sobre la frecuencia cardíaca. Homo medicus. https://homomedicus.com/efecto-de-la-estimulacion-simpatica-y-parasimpatica-sobre-la-frecuencia-cardiaca/

[4].Guzmán, J. E. O., & Romero, D. M. (2008). Variabilidad de la frecuencia cardiaca, una herramienta útil. Rev. Digital., Buenos Aires, 121.

[5].Montoya, J. R. A. (2001). La transformada wavelet. Revista de la Universidad de Mendoza.

[6].Electrocardiograma. (s/f). Fundación Española del Corazón. Recuperado el 31 de octubre de 2024, de https://fundaciondelcorazon.com/informacion-para-pacientes/metodos-diagnosticos/electrocardiograma.html

[7].Riaño-Ruiz, L. M., & Riveros-Mestre, J. S. (2023). Sistema de adquisición de señales electrocardiográficas para visualizar el comportamiento cardíaco en corredores de 100 mt.




