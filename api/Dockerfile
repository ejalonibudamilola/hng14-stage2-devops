# -------- build stage --------
FROM python:3.11-slim AS builder
WORKDIR /app

# Install deps into a venv to keep runtime clean
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# -------- runtime stage --------
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy venv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy app code
COPY . .

# Install curl for healthcheck (small and fine)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

USER appuser

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD curl -f http://localhost:8000/health || exit 1