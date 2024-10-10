# Data Collector

Este proyecto es un recolector de datos que captura imágenes de la pantalla y las guarda en un directorio especificado. También detecta entradas de teclado y de un controlador Xbox (o cualquiera).

## Requisitos

1. **Instalar Python 3.12.7**:
Asegúrate de tener Python 3.12.7 instalado en tu sistema y que el PATH esté correctamente configurado.
Puedes descargarlo desde [python.org](https://www.python.org/downloads/release/python-3127/).

2. **Instalar las dependencias**:
Ejecuta el archivo `install_requirements.bat` para instalar todas las dependencias necesarias listadas en `requirements.txt`.

## Ejecución

1. **Definir parametros de grabación**:
El programa grabará por defecto con resolucion 1920 x 1080 en pantalla completa. Se pueden ajustar en las primeras lineas de DataCollectorController.py en
"Parametros de entrada", se puede editar con un editor de texto cualquiera.


2. **Ejecutar el script de grabación**:
Haz doble clic en el archivo `RUN.bat` para iniciar el script de grabación. Las imagenes quedarán guardadas en la carpeta "collected_images".

## Comandos

    Presione 'Q' para detener la captura de datos.
    Presione 'P' para pausar la captura de datos.
    Presione 'E' para eliminar las últimas 100 imágenes capturadas (En caso de error).
