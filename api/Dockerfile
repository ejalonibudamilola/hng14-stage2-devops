# build stage
FROM python:3.11-slim AS builder
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# runtime stage
FROM python:3.11-slim

# install curl (lint-safe version)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# create non-root user
RUN addgroup --system app && adduser --system --ingroup app appuser

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY . .

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=10 \
  CMD curl -f http://127.0.0.1:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]