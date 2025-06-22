FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY db.sql .
COPY api/ api/

RUN apt-get update && apt-get install -y sqlite3 && \
    rm -rf /var/lib/apt/lists/*

RUN sqlite3 infra.db < db.sql

WORKDIR api/
CMD ["../.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["bash"]
