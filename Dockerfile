# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala las dependencias
RUN pip install -r requirements.txt --no-cache-dir

# Ejecuta app.py
CMD ["python", "app.py"]
