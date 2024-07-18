import unittest
import sys

# Redirigir la salida estándar y la salida de errores estándar a un archivo
with open('test_results.txt', 'w') as f:
    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
