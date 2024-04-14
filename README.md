# Estandar FastAPI

Proyecto base para iniciar un proyecto con FastAPI.

## Comenzando 🚀
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas. Mira Instalación para conocer cómo instalar el proyecto.

### Pre-requisitos 📋
- Python 3.11: Asegúrate de tener Python 3.11 instalado. Puedes descargarlo desde la [página oficial](https://www.python.org/downloads/release/python-3110/).
- Pip: Viene instalado con Python 3.4 y superior.
- Virtualenv: Recomendado para crear entornos aislados. Instalar con `pip install virtualenv`.

### Instalación 🔧
Para el entorno de desarrollo
```bash
make setup-dev
```

Para el entorno de producción
```bash
make setup
```

### Variables de entorno 📦
Copia el archivo `.env.template` y renómbralo a `.env`. Llena las variables de entorno con los valores correspondientes.

### Iniciar el proyecto 🚀
Para el entorno de desarrollo
```bash
make start
```

Para el entorno de producción
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Linting 🧐
```bash
make lint
```

## Construido con 🛠️
- [FastAPI](https://fastapi.tiangolo.com/) - Framework web
- [Pydantic](https://docs.pydantic.dev/latest/) - Validación de datos
- [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para la base de datos
- [SlowAPI](https://slowapi.readthedocs.io/en/latest/) - Rate Limiting para FastAPI



