# Multi-stage Dockerfile for CivicLaw Enterprise Platform
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Copy project files
COPY . .

# Run migrations and collect static
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["python", "main.py", "runserver", "0.0.0.0:8000"]
