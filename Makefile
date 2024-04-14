.PHONY: help setup setup-dev venv lint start

help:
	@echo "Comandos disponibles:"
	@echo "  setup      - Crea el entorno virtual e instala dependencias de producción."
	@echo "  setup-dev  - Instala dependencias de desarrollo adicionalmente."
	@echo "  venv       - Crea un entorno virtual en .venv."
	@echo "  lint       - Ejecuta pylint para verificar el estilo del código."
	@echo "  start      - Ejecuta la aplicación usando el entorno virtual."

# Crea el entorno virtual y instala las dependencias de producción
setup: venv
	@./.venv/bin/pip install -r requirements.txt
	@echo "Setup de producción completo. Activa tu entorno con 'source .venv/bin/activate'"

# Instala las dependencias de desarrollo
setup-dev: setup
	@./.venv/bin/pip install -r dev-requirements.txt
	@echo "Setup de desarrollo completo. Activa tu entorno con 'source .venv/bin/activate'"

# Crea un entorno virtual en .venv
venv:
	@python3 -m venv .venv

# Ejecuta pylint para verificar el estilo del código
lint:
	@pylint app

# Ejecuta la aplicación usando el entorno virtual
start:
	@./.venv/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
