# Visualización para Pantallas LED de Paradas de Bus

Este proyecto genera visualizaciones para pantallas LED en paradas de autobuses, mostrando información como tiempos de llegada y detalles de rutas.

### Paso 1: Clonar el Repositorio

Para comenzar, clona el repositorio y navega a su directorio:

```bash
git clone https://github.com/diegoalrv/pantallas-led
cd pantallas-led
```

## Tabla de Contenidos
1. [Montaje y Funcionamiento de Pantallas](#montaje-y-funcionamiento-de-pantallas)
2. [Generación de Póster de Bus](#generación-de-póster-de-bus)
3. [Comunicación y Configuración](#comunicación-y-configuración)

## Montaje y Funcionamiento de Pantallas
*Contenido pendiente.*

## Generación de Póster de Bus
En el directorio raiz del respositorio seguimos los siguientes pasos:

### Construir la Imagen Docker
Primero, construye la imagen Docker que contiene todas las dependencias necesarias:

```bash
docker build -t bus_poster .
```

### Ejecutar el Contenedor Docker
Utiliza el script run_container.sh para ejecutar el contenedor. Este script monta las carpetas locales necesarias y inicia el contenedor. El contenedor se eliminará automáticamente después de su ejecución debido al parámetro --rm.

```bash
./run_container.sh
```

Nota: Asegúrate de que el script ```run_container.sh``` tenga permisos de ejecución. Si no es así, ejecuta:
