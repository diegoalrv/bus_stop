# Visualización para pantallas LED de paradas de bus

Este repositorio contiene los archivos necesarios para ejecutar una aplicación Jupyter Notebook con ciertas bibliotecas de visualización y procesamiento de imágenes.

## Contenido

- `Dockerfile`: Define cómo construir la imagen Docker para ejecutar la aplicación.
- `requirements.txt`: Lista las bibliotecas y dependencias necesarias para la aplicación.

## Dockerfile

### Descripción

El `Dockerfile` especifica cómo construir una imagen Docker basada en Python 3.8 que tiene todas las dependencias necesarias para ejecutar la aplicación.

### Instrucciones

1. **Imagen base**: Utiliza Python 3.8.
2. **Directorio de trabajo**: Establece `/app` como el directorio de trabajo en el contenedor.
3. **Instalación de dependencias**: Copia y utiliza `requirements.txt` para instalar las bibliotecas necesarias.
4. **Configuración de Jupyter**: Copia el archivo de configuración de Jupyter al contenedor.
5. **Puerto**: Expone el puerto 8888 para Jupyter Notebook.
6. **Comando de inicio**: Al iniciar el contenedor, se ejecuta Jupyter Notebook en el puerto 8888.

## requirements.txt


### Descripción

El archivo `requirements.txt` lista las bibliotecas y dependencias que se requieren para la aplicación.

### Bibliotecas y dependencias

- `matplotlib`: Biblioteca de visualización de datos.
- `seaborn`: Biblioteca de visualización de datos basada en matplotlib.
- `plotly`: Biblioteca para gráficos interactivos.
- `opencv-python`: Biblioteca de procesamiento de imágenes y visión por computadora.
- `jupyter`: Entorno de desarrollo interactivo.

## Cómo ejecutar

1. Construye la imagen Docker:

`docker build -t bus_stop_visualization .`

2. Ejecuta el contenedor:

`docker run -d --name bus_stop_vis -v /scripts:/app/scripts -p 8888:8888 bus_stop_visualization`

3. Abre un navegador y accede a `http://localhost:8888` para comenzar a usar Jupyter Notebook.