# Guía de configuración para Modulo LED 

## Materiales Necesarios

- Raspberry Pi, versión 3 o superior.
- Hat de conexión HUB75
- Paneles LED P4 con I/O HUB75
- Fuente de alimentación con salida 5V/3A
- Cables de Alimentación 4-pin 5V/3A
- Cables de datos con conexión HUB75

## Configuración inicial

### Conexionado

Para las conexiones de datos, se utilizan cables hembra HUB75 de 16-pines, estos se conectan en un extremo al HAT HUB75 para Raspberry PI. En caso de tener un HAT con multiples conexiones de HUB75, siempre utilizar la salida TOP para la primera fila del conjunto de paneles, y usar el resto de las salidas para las filas inferiores. El extremo opuesto del cable de datos debe conectarse en el "input" del panel, estos modulos tienen etiquetada su entrada y salida en la parte posterior. Ver las imagenes mostradas como referencia visual. 

Para la conexión electrica, cada uno de los paneles LED tiene una entrada de cuatro pines para cables de alimentación. Es necesario tener una fuente de poder con salida de 5V y un minimo de 3A, para cumplir con los criterios de alimentación en los modulos LED.

![HUB75 conector](https://github.com/diegoalrv/pantallas-led/assets/148826389/5c03ffe1-eca1-42b8-bd50-4efc3d170ed7) ![HUB75 input](https://github.com/diegoalrv/pantallas-led/assets/148826389/f153e6ce-ce5e-4b19-8e2d-45ffa2d77037) ![Raspi HAT](https://github.com/diegoalrv/pantallas-led/assets/148826389/8b40b730-42ae-4416-929d-cd32de8903ee)


A continuación, se presenta un diagrama de conexiones, tanto para los datos como para la alimentación. Notar que la referencia (0,0) corresponde a la orientación superior izquierda de las gráficas que se deseen desplegar en el módulo, también se señala la orientación de las entradas y salidas de cada panel en la configuración.

![conexionModLED](https://github.com/diegoalrv/pantallas-led/assets/148826389/782bac34-8173-4207-a9f7-df2b5422b9ca.png)

### Configuración de Raspberry Pi

Luego de haber descargado los datos almancenados en este reposotorio. En el directorio ModuloLED, encontrará un script llamado MenuPantalla.sh, en este menú se puede hacer dos acciones en concreto:
- Configurar parámetros de la implementación, modificando variables del codigo base.
- Desplegar una imagen a partir de un archivo imagen jpg o png almacenada en el sistema.


