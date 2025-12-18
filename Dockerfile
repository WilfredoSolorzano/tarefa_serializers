FROM python:3.12-slim as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
        libpq-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN pip install --upgrade pip \
    && pip install poetry==1.8.3

# Copiar arquivos do projeto
COPY pyproject.toml poetry.lock* ./

# Instalar dependências (se não tiver poetry.lock, ignore-o)
RUN if [ -f poetry.lock ]; then poetry install --no-dev --no-root; else poetry install --no-dev; fi

# Copiar o restante do projeto
COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]