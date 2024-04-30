# Conéctese SIG 2024

Este repositorio almacena la información del Conéctese con SIG sobre geoprocesamiento.

## Configuración del entorno

1. **Abrir la terminal de VS Code**: Puedes hacer esto yendo a `View -> Terminal`, o presionando `Ctrl + ``.

2. **Ejecutar el script `set-location.ps1`**: Este script cambia el directorio de trabajo al directorio deseado.

3. **Ejecutar el script `Clonar_ambiente.ps1`**: Este script clona el ambiente base de conda y crea un nuevo ambiente llamado "geoprocesamiento". Si deseas cambiar el nombre del ambiente, puedes modificar el script.

4. **Seleccionar el ambiente "geoprocesamiento" en VS Code**: Esto permitirá que VS Code reconozca las dependencias instaladas en el ambiente "geoprocesamiento".

## FastAPI

FastAPI es un moderno y rápido (de alto rendimiento) framework web para construir APIs con Python 3.6+ basado en las anotaciones de tipo estándar de Python.

## Despliegue de FastAPI

Para desplegar una aplicación FastAPI, necesitarás un servidor ASGI, como Uvicorn o Hypercorn. Puedes iniciar tu aplicación con el comando `uvicorn main:app --reload`, donde `main` es el nombre de tu archivo que contiene FastAPI y `app` es el nombre de la instancia de la aplicación FastAPI.

Abre la terminal integrada en Visual Studio Code. Puedes hacer esto yendo a `View -> Terminal`, o presionando `Ctrl + ``.

Navega al directorio donde se encuentra tu archivo `main.py`. Puedes hacer esto con el comando:

```powershell
Set-Location -Path "C:\Users\ECETINA\OneDrive - Esri NOSA\conectese_sig_2024\conectese_sig_2024\my-fastapi-app\app"
```
Ejecuta tu aplicación con el siguiente comando:
```powershell
uvicorn main:app --reload
```

## Abrir la app

Una vez que tu aplicación esté en ejecución, puedes verla en tu navegador web. Por defecto, Uvicorn inicia el servidor en localhost en el puerto 8000. Por lo tanto, puedes ver tu aplicación yendo a la siguiente URL en tu navegador:

http://localhost:8000

## Ver documentación de fastapi
Además, FastAPI genera automáticamente una interfaz de usuario interactiva para tu API. Puedes ver esta interfaz yendo a:

http://localhost:8000/docs

En esta interfaz, puedes ver todos tus puntos finales de API, probarlos interactivamente, ver los parámetros requeridos y ver las respuestas esperadas.