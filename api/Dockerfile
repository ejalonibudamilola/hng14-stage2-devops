# build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# runtime
FROM python:3.11-slim

RUN addgroup --system app && adduser --system --ingroup app appuser

WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY . .

USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]