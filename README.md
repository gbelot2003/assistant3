# Assistant3

## Descripción

**Assistant3** es un proyecto desarrollado en Python para manejar interacciones con usuarios a través de APIs. Está basado en Flask y diseñado con una arquitectura modular para facilitar la escalabilidad y el mantenimiento.

## Estructura del Proyecto

- **app.py**: Archivo principal para ejecutar la aplicación.
- **config.py**: Contiene la configuración general de la aplicación, como variables de entorno y rutas.
- **extensions.py**: Define extensiones y complementos utilizados en la aplicación, como bases de datos y otros servicios.
- **requirements.txt**: Archivo con las dependencias necesarias para ejecutar el proyecto.
- **src/**: Contiene el código fuente modular del proyecto, dividido en diferentes submódulos.
- **static/**: Archivos estáticos como CSS, JavaScript y recursos multimedia.
- **templates/**: Plantillas HTML utilizadas en la interfaz de usuario.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados:

- Python 3.8 o superior
- pip (Python package manager)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL del repositorio>
    cd assistant3-main
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    python -m spacy download es_core_news_sm
    ```

## Uso

1. Configura las variables de entorno necesarias en el archivo `config.py` o utilizando un archivo `.env`.
2. Ejecuta la aplicación:

    ```bash
    python app.py
    ```

3. La aplicación estará disponible en `http://127.0.0.1:5000/` por defecto.

## Estructura del Código

El proyecto sigue una estructura modular, organizada de la siguiente forma:

- **src/**: Módulos del proyecto.
- **static/**: Archivos estáticos.
- **templates/**: Plantillas HTML.

Cada módulo en `src/` representa una funcionalidad independiente del proyecto y se integra con la aplicación principal a través de `app.py`.

## Licencia

Este proyecto está bajo la licencia MIT. Para más información, consulta el archivo `LICENSE`.

