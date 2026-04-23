# -------- build stage --------
FROM python:3.11-slim AS builder
WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- runtime stage --------
FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

USER appuser

CMD ["python", "worker.py"]

# Worker health = can reach Redis
HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD python -c "import os,redis; r=redis.from_url(os.getenv('REDIS_URL')); r.ping()" || exit 1