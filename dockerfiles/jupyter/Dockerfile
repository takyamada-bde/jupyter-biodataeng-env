FROM ghcr.io/prefix-dev/pixi:latest AS build

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN groupadd -r appgroup && useradd -r -m -d /home/appuser -g appgroup appuser

WORKDIR /app
RUN chown appuser:appgroup /app

USER appuser

COPY --chown=appuser:appgroup pixi.toml pixi.lock ./

RUN pixi install --frozen --no-hard-links

FROM ubuntu:24.04

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        gcc \
        g++ \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

RUN groupadd -r appgroup && useradd -r -m -d /home/appuser -g appgroup appuser

USER appuser

COPY --from=build /usr/local/bin/pixi /usr/local/bin/pixi
COPY --from=build --chown=appuser:appgroup /app/.pixi /app/.pixi
COPY --chown=appuser:appgroup pixi.toml pixi.lock ./
COPY --chown=appuser:appgroup . .

EXPOSE 8888

CMD ["pixi", "run", "lab"]
