FROM python:3.8-slim

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

RUN groupadd --gid 1000 dev-user \
  && useradd --uid 1000 --gid 1000 --shell /bin/sh --create-home dev-user \
  && chown -R dev-user:dev-user ${APP_HOME}

RUN apt-get update && apt-get install -y \
    curl \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install uv

ENV DOCKERIZE_VERSION=v0.6.1

RUN curl -fSL https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz \
    | tar -C /usr/local/bin -xzv

USER dev-user

ENV PATH="${APP_HOME}/.venv/bin:$PATH"

COPY --chown=dev-user:dev-user pyproject.toml uv.lock ${APP_HOME}/

RUN uv sync --no-install-project

COPY --chown=dev-user:dev-user . ${APP_HOME}

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]