# Generación de Póster de Bus
En el directorio raiz del respositorio pasamos al carpeta:

```bash
cd GenPoster
```

## Construir la Imagen Docker
Primero, construye la imagen Docker que contiene todas las dependencias necesarias:

```bash
docker build -t bus_poster .
```

## Ejecutar el Contenedor Docker
Utiliza el script ```run_container.sh``` para ejecutar el contenedor. Este script monta las carpetas locales necesarias y inicia el contenedor. El contenedor se eliminará automáticamente después de su ejecución debido al parámetro ```--rm```.

```bash
./run_container.sh
```

Nota: Asegúrate de que el script ```run_container.sh``` tenga permisos de ejecución. Si no es así, ejecuta:
```bash
chmod +x run_container.sh
```

## Generación y Almacenamiento del Póster
Al ejecutar el contenedor, el script ```app.py``` se iniciará automáticamente y realizará lo siguiente:

- Calcula el tiempo restante hasta la llegada del autobús.
- Genera visualizaciones con los detalles del autobús y el tiempo restante.
- Guarda la imagen generada en una carpeta local mapeada al contenedor.

Por el momento esta funcionando con datos de prueba, eventualmente se usará como datos de entrada las respuestas del endpoint.

## Acceso a la Imagen Generada
La imagen del póster se guardará en la carpeta local especificada en el script ```run_container.sh```. Puedes acceder a ella directamente desde esta carpeta en tu máquina local.