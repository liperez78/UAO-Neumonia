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

Este conjunto de pruebas verifica el comportamiento del método load_img_file de la clase App bajo diferentes condiciones:

Cuando se pasa una imagen válida ('Torax.jpg' y 'otra_imagen.jpg').
Cuando se pasa un valor nulo (None).
Cuando se pasa una imagen inexistente ('imagen_inexistente.jpg').
Cada prueba utiliza aserciones (self.assertTrue y self.assertFalse) para verificar si el método retorna el valor esperado, mostrando un mensaje de error específico si la prueba falla.

Con el archivo  test_app.py: Se define las variables y se ejecuta las pruebas unitarias


## Pruebas de usuabilidad para el código detector_neumonia
pruebas unitarias en la interfaz de usuario (UI) de una aplicación Tkinter, con pytest junto con herramientas de simulación y verificación.
Se debe crear el siguiente archivo de prueba "test_ui.py" y así mismo se debe ejecutar. Este archivo se encargará de simular las interacciones con la UI y verificar que los botones y otros elementos funcionen como se espera.




