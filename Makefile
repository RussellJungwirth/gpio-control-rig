VENV_DIR=.venv

setup:
	@if [ ! -d "${VENV_DIR}" ]; then \
		echo "creating virtual environment in ${VENV_DIR}/"; \
		python3 -m venv ${VENV_DIR}; \
		echo "installing requirements"; \
		${VENV_DIR}/bin/pip install -qq --upgrade pip; \
		${VENV_DIR}/bin/pip install -qq --upgrade poetry; \
		${VENV_DIR}/bin/poetry install; \
	fi

lock: setup
	${VENV_DIR}/bin/poetry lock --no-update

install: setup
	${VENV_DIR}/bin/poetry install
