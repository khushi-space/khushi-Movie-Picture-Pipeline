FROM python:3.10-slim-bookworm

ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Ensure Python treats /app as the root module search path
ENV PYTHONPATH=/app

WORKDIR /app

# Install system dependencies needed to build uwsgi on Linux
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and uwsgi inside the container
RUN pip install --no-cache-dir pipenv uwsgi

# Copy dependency files
COPY Pipfile Pipfile.lock* ./

# Install Python packages
RUN pipenv install --system --deploy --ignore-pipfile || pipenv install --system

# Copy application code
COPY . .

EXPOSE 5000

CMD ["uwsgi", "--http", "0.0.0.0:5000", "--module", "app:app", "--callable", "app"]