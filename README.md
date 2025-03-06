# Proyecto FastAPI con Base de Datos en MySQL

## Descripción

Este proyecto utiliza FastAPI para crear una API y Docker para gestionar la base de datos MySQL. La base de datos se ejecuta en un contenedor Docker debido a problemas para ejecutar XAMPP en la computadora de desarrollo.

## Requisitos

- Docker
- Docker Compose
- Python 3.8+

## Configuración del Entorno

1. **Clonar el repositorio**:

    ```sh
    git clone https://github.com/netfoor/AppInventarios.git
    cd AppInventarios
    ```

2. **Crear y activar un entorno virtual** (opcional pero recomendado):

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instalar las dependencias**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Ejecutar el contenedor con la base de datos**:

    ```sh
    docker-compose up --build
    ```

5. **Iniciar la aplicación FastAPI**:

    ```sh
    fastapi dev main.py
    ```

6. **Acceder a la API**:

    Abre tu navegador y ve a `http://localhost:8000` para ver la documentación interactiva de la API

    Si deseas ver la base de datos puedes correrla en `http://localhost:8080` con las siguientes credenciales:

    user: root
    password: root
    