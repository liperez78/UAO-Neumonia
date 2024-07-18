import csv

# Lee la salida de las pruebas desde el archivo de texto
with open('test_results.txt', 'r') as f:
    lines = f.readlines()

# Filtra las líneas que contienen errores y otros mensajes importantes
error_lines = []
capture = False
for line in lines:
    if "ERROR:" in line or capture:
        error_lines.append(line.strip())
        capture = True if "Traceback" in line else False
    if capture and line.strip() == "":
        capture = False

# Escribe las líneas filtradas en un archivo CSV
with open('test_errors.csv', 'w', newline='') as csvfile:
    fieldnames = ['Error']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for line in error_lines:
        writer.writerow({'Error': line})
