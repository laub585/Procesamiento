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

![WhatsApp Image 2024-10-30 at 9 46 06 PM (1)](https://github.com/user-attachments/assets/dc2b6b27-e341-49bc-96ec-86a33d42c2a2)

**Figura #03. Representación esquemática de un intervalo R­R Tomado de: Maud PJ. , Foster C. Physiological assessment of human fitness.
Second Edition. 2006; (41)"**

* **¿Cómo Se Mide La Variabilidad de la Frecuencia Cardiaca (HRV)?**
  
Para medir la variabilidad de la frecuencia cardiaca (HRV), se puede realizar diferentes métodos de medidas. Entre ellos encontramos medidas estáticas que se dan en el análisis del tiempo dominante, o también se puede emplear métodos geométricos y análisis espectral que se da mediante el análisis de la frecuencia dominante.

**Análisis del Tiempo Dominante:**

El análisis del tiempo dominio en la variabilidad de la frecuencia cardíaca (HRV) es una herramienta fundamental al analizar directamente los intervalos RR (tiempo entre dos latidos consecutivos), se pueden obtener diversas variables que proporcionan información valiosa sobre la dinámica cardíaca:

* **Promedio R­R (ms)**: Es la media de los intervalos R­R, este dato se obtiene dividiendo la sumatoria de todos los intervalos entre el total de intervalos.
  
* **SDNN (ms):**  Es la desviación estándar de todos los intervalos R­R. Esta variable muestra la variación en cortos y largos periodos en cuanto a la variación en los intervalos R­R (HRV).

Para realizar los cálculos de HRV, es recomendado utilizar no menos de 6 intervalos para comprenderme a mayor profundidad las  diferencias significativas (Task Force of the European Society of Cardiology & the North American Society of Pacing and Electrophysiology, 1996)

**Análisis Espectral:**

El análisis espectral se da mediante las frecuencias arrojadas por la técnica del Electrocardiograma (ECG),Este método de análisis se conoce como el espectro permite entender aún más los efectos de los sistemas nervioso simpático y parasimpático sobre la HRV (Akselrod,
1985). Los principales parámetros de medida en el análisis espectral son:

* **Muy baja frecuencia (VLF):** Está alimentado por frecuencias menores a 0.04 Hz.

* **Baja frecuencia (LF):** Son componentes que están alrededor de 0.1 Hz.
  
* **Alta frecuencia (HF):** Componente sincronizado con la frecuencia de respiración. Está sobre un rango de 0.2 a 0.5 Hz dependiendo de la frecuencia respiratoria.





----

**Bibliografía:**

[1].Báez, M. E. (2007). Visión clásica del sistema nervioso autónomo. Universidad de La Habana.

[2].Frecuencia cardiaca. (s/f). Fundación Española del Corazón. Recuperado el 31 de octubre de 2024, de https://fundaciondelcorazon.com/prevencion/marcadores-de-riesgo/frecuencia-cardiaca.html

[3]. Medicus, H. (2024, junio 22). Efecto de la estimulación simpática y parasimpática sobre la frecuencia cardíaca. Homo medicus. https://homomedicus.com/efecto-de-la-estimulacion-simpatica-y-parasimpatica-sobre-la-frecuencia-cardiaca/

[4].

