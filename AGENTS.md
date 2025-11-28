# Project Overview

## Version and Runtime
- Project: kopi-shop-backend
- App version: 0.1.0 (pyproject.toml)
- Python: 3.12 (.python-version), requires >=3.9

## Key Dependencies
- FastAPI [standard] >=0.122.0
- SQLAlchemy >=2.0.44
- Psycopg >=3.2.13
- Dev/test: uv (CI pins 0.9.13), ruff, pytest, httpx

## Database (docker-compose.dev.yml)
- Engine: PostgreSQL (image postgres:latest)
- Container: kopi_postgres
- Host/port: localhost:5432 (mapped 5432:5432)
- Credentials: user dev, password dev, database kopi_dev
- DSN example: postgresql://dev:dev@localhost:5432/kopi_dev
- Data volume: db_data -> /var/lib/postgresql/data

## API
- Healthcheck: GET /health -> {"ok": true}
