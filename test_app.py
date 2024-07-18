import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from PIL import Image
from app import App  # Asumiendo que el código original está en un archivo llamado app.py

class TestApp(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la aplicación
        self.app = App()
        self.app.root.withdraw()  # Ocultar la ventana principal durante las pruebas

    @patch('tkinter.filedialog.askopenfilename')
    @patch('PIL.Image.open')
    def test_load_img_file(self, mock_open, mock_askopenfilename):
        # Configurar los mocks
        mock_askopenfilename.return_value = 'test_image.jpg'
        mock_image = MagicMock(spec=Image.Image)
        mock_open.return_value = mock_image

        # Llamar a la función de carga de imagen
        self.app.load_img_file()

        # Verificar que la imagen se ha cargado correctamente
        mock_open.assert_called_once_with('test_image.jpg')
        self.assertTrue(self.app.button1['state'] == 'normal')

    @patch('tensorflow.keras.models.load_model')
    @patch('numpy.expand_dims')
    @patch('numpy.array')
    def test_run_model(self, mock_array, mock_expand_dims, mock_load_model):
        # Configurar el mock del modelo
        mock_model = MagicMock()
        mock_load_model.return_value = mock_model
        mock_model.predict.return_value = [[0.7]]  # Supongamos que la predicción es 0.7

        # Cargar una imagen falsa
        self.app.image = Image.new('RGB', (150, 150))

        # Llamar a la función de predicción
        self.app.run_model()

        # Verificar la predicción
        mock_model.predict.assert_called_once()
        self.assertEqual(self.app.text2.get("1.0", tk.END).strip(), "Neumonía")
        self.assertEqual(self.app.text3.get("1.0", tk.END).strip(), "0.70")

if __name__ == '__main__':
    unittest.main()
