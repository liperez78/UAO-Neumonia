import pytest
from unittest.mock import MagicMock, patch
from tkinter import Tk
from detector_neumoniacopia import App  # Cambia 'your_app_file' por el nombre de tu archivo

@pytest.fixture
def app():
    app = App()
    app.root.withdraw()  # Ocultar la ventana principal durante las pruebas
    yield app
    app.root.destroy()

def test_button_states_after_load_image(app):
    # Simula la carga de una imagen
    with patch('your_app_file.filedialog.askopenfilename', return_value='test_image.jpg'):
        with patch('your_app_file.Image.open') as mock_open:
            app.load_img_file()

            # Verifica que el botón "Predecir" está habilitado
            assert app.button1['state'] == 'normal'

def test_button_states_after_delete(app):
    # Simula la carga de una imagen para habilitar el botón "Predecir"
    with patch('your_app_file.filedialog.askopenfilename', return_value='test_image.jpg'):
        with patch('your_app_file.Image.open') as mock_open:
            app.load_img_file()
    
    # Simula hacer clic en el botón "Borrar"
    app.delete()
    
    # Verifica que el botón "Predecir" está deshabilitado
    assert app.button1['state'] == 'disabled'
