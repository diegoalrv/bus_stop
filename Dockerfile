# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el archivo de configuración de Jupyter
COPY jupyter_notebook_config.py /root/.jupyter/

# Expone el puerto 8888 para Jupyter Notebook
EXPOSE 8888

# Ejecuta Jupyter Notebook cuando el contenedor se inicie
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
