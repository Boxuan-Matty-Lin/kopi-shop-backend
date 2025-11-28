import os
from pathlib import Path

import psycopg

ENV_FILE = Path(__file__).resolve().parent.parent / ".env.dev"


def load_env_file() -> None:
    """Load .env.dev into os.environ without overriding existing values."""
    if not ENV_FILE.exists():
        return

    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key, value.strip().strip("'\""))


def build_dsn() -> str:
    """Return a psycopg-friendly DSN from env, normalizing prefixes if needed."""
    load_env_file()
    raw = os.getenv("DATABASE_URL", "postgresql://dev:dev@localhost:5432/kopi_dev")
    if raw.startswith("postgresql+psycopg"):
        raw = raw.replace("postgresql+psycopg", "postgresql", 1)
    return raw


def test_db_connection():
    """Smoke test: connect and execute a trivial query to confirm DB reachability."""
    dsn = build_dsn()
    with psycopg.connect(dsn, connect_timeout=5) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
            assert cur.fetchone() == (1,)
