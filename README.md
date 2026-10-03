# Jupyter Biodataeng env

Practical JupyterLab Environment for Biological Data Engineering


## Tech Stack & Versions

|Tech Stack|Version|
|:---:|:---:|
|PostgreSQL|18-bookworm|
|Pixi|0.81.0|


- Python 3.12
- JupyterLab
- Scikit-learn
- PyTorch
- BioPython
- ScanPy
- RDKit
- Tidyverse
- dbplyr
- WGCNA
- DESeq2
- edgeR



## Directory Structure

```
jupyter-biodataeng-env/
├── compose.yaml                  # Docker Compose configuration
├── dockerfiles/                  # Dockerfiles for each service
│   ├── jupyter/
│   │   └── Dockerfile
│   └── postgres/
│       └── Dockerfile
├── notebooks/                    # JupyterLab environment and notebooks
│   ├── pixi.toml                 # Pixi environment definition
│   ├── pyproject.toml            # Dev tool settings (tox, mypy, etc.)
│   ├── pixi.lock                 # Pixi lock file
│   ├── data/                     # Data storage
│   │   ├── raw/                  # Original, unmodified data as received from the source
│   │   ├── interim/              # Intermediate data produced during cleaning or transformation
│   │   └── processed/            # Final, analysis-ready datasets
│   ├── src/                      # Shared Python modules
│   │   └── db/
│   │       ├── session.py        # Database session management
│   │       └── .env.example
│   └── tests/                    # Tests
└── postgres/                     # PostgreSQL configuration
    ├── .env.example
    └── initdb/
        └── 01_create_app_user.sh # Initialization script on first startup
```

## Quick Start

初めて利用するときは、`docker compose build`でdocker imageを作成します。

```bash
docker compose up -d
```

コンテナが正常に起動すると、`http://localhost:8888`でJupyterLabを利用できます。

```bash
docker compose down
```

## Design Philosophy
