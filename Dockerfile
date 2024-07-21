# Usa una imagen base de Python
FROM python:3.12.4

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al directorio de trabajo
COPY . .

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto si la aplicación usa uno (opcional)
# EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
