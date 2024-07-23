## Hola! Bienvenido a la herramienta para la detección rápida de neumonía

Deep Learning aplicado en el procesamiento de imágenes radiográficas de tórax en formato DICOM con el fin de clasificarlas en 3 categorías diferentes:

1. Neumonía Bacteriana

2. Neumonía Viral

3. Sin Neumonía

Aplicación de una técnica de explicación llamada Grad-CAM para resaltar con un mapa de calor las regiones relevantes de la imagen de entrada.

---

## Uso de la herramienta:

A continuación le explicaremos cómo empezar a utilizarla.

Requerimientos necesarios para el funcionamiento:
1.  Instale Anaconda para Windows siguiendo las siguientes instrucciones:
  https://docs.anaconda.com/anaconda/install/windows/

- Abra Anaconda Prompt y ejecute las siguientes instrucciones:

  conda create -n tf tensorflow

  conda activate tf

  cd UAO-Neumonia

  pip install -r requirements.txt

  python detector_neumonia.py
  
2. Importar las siguientes bibliotecas:
tkinter: Biblioteca estándar de Python para crear interfaces gráficas de usuario.
PIL: Biblioteca para abrir, manipular y guardar archivos de imagen.
numpy: Biblioteca para trabajar con matrices y realizar cálculos numéricos.
tensorflow.keras.models: Utilizado para cargar un modelo pre-entrenado de Keras.
reportlab: Biblioteca para generar documentos PDF.  

3. Uso de la Interfaz Gráfica:

- Ingrese la cédula del paciente en la caja de texto
- Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador (Imagenes de prueba en https://drive.google.com/drive/folders/1WOuL0wdVC6aojy8IfssHcqZ4Up14dy0g?usp=drive_link)
- Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados
- Presione el botón 'Guardar' para almacenar la información del paciente en un archivo excel con extensión .csv
- Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz
- Presión el botón 'Borrar' si desea cargar una nueva imagen
- Se adjunto evidencias de la ejecuçión archivo denominado "resultados ejecutados del detector_neumonia.pptx"

Versión Python 3.12.4
---

## Arquitectura de archivos propuesta.

## detector_neumonia.py

Este código crea una aplicación de escritorio para la detección de neumonía a partir de imágenes radiográficas. Permite cargar una imagen, ejecutar un modelo pre-entrenado para hacer una predicción, y generar un informe en PDF con los resultados. También incluye funcionalidades para borrar datos ingresados y guardar resultados en un archivo CSV 

## model.py

Script carga un modelo Keras previamente entrenado para la detección de neumonía, configura la función de pérdida de entropía cruzada binaria sin reducción, compila el modelo y define una función para predecir si una imagen muestra signos de neumonía

## mi_modelo_entrenado.H5

Permite realizar la carga y predicción de imegenes del módelo entrenado.
URL de acceso: https://drive.google.com/file/d/1-vwwTEc0VI8zoctUIi2A95rNnKZJ0vGy/view?usp=drive_link

---

## Pruebas unitarias para el código detector_neumonia
Para realizar pruebas unitarias en este código, se trabaja el módulo unittest de Python. Se crean dos pruebas unitarias para las funciones load_img_file y run_model
con el archivo  test_app.py

Resultados de las pruebas unitarias exitoso (test_results.cvs) y con errores en un (test.errors.cvs), para eso se necesita los siguientes códigos:

generate_csv.py
run_tests.py

## Pruebas de usuabilidad para el código detector_neumonia
pruebas unitarias en la interfaz de usuario (UI) de una aplicación Tkinter, con pytest junto con herramientas de simulación y verificación.
Se debe crear el siguiente codigo
test_ui.py
y se debe ejcutar pytest test_ui.py
El codigo va analizando cada boton de la aplicacion y genera los resultados de la prueba


## Acerca de Grad-CAM

Es una técnica utilizada para resaltar las regiones de una imagen que son importantes para la clasificación. Un mapeo de activaciones de clase para una categoría en particular indica las regiones de imagen relevantes utilizadas por la CNN para identificar esa categoría.

Grad-CAM realiza el cálculo del gradiente de la salida correspondiente a la clase a visualizar con respecto a las neuronas de una cierta capa de la CNN. Esto permite tener información de la importancia de cada neurona en el proceso de decisión de esa clase en particular. Una vez obtenidos estos pesos, se realiza una combinación lineal entre el mapa de activaciones de la capa y los pesos, de esta manera, se captura la importancia del mapa de activaciones para la clase en particular y se ve reflejado en la imagen de entrada como un mapa de calor con intensidades más altas en aquellas regiones relevantes para la red con las que clasificó la imagen en cierta categoría.


