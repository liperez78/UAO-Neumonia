import unittest
from detector_neumonia import App

class Testload_img_file(unittest.TestCase):
    def test_1(self):
        resultado = App.load_img_file('Torax.jpg')
        self.assertTrue(resultado is not False, 'La imagen Torax.jpg no se cargó correctamente.')

    def test_2(self):
        resultado = App.load_img_file('otra_imagen.jpg')
        self.assertTrue(resultado is not False, 'La imagen otra_imagen.jpg no se cargó correctamente.')

    def test_3(self):
        resultado = App.load_img_file(None)
        self.assertFalse(resultado, 'El resultado debería ser False para una imagen nula.')

    def test_4(self):
        resultado = App.load_img_file('imagen_inexistente.jpg')
        self.assertFalse(resultado, 'El resultado debería ser False para una imagen inexistente.')

if __name__ == '__main__':
    unittest.main()
