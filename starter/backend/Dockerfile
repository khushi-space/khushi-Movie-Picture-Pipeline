FROM python:3.10-slim

ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for uwsgi and pipenv
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libpcre3 \
    libpcre3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy dependency files first (better caching)
COPY Pipfile Pipfile.lock* ./

# Install dependencies
RUN pipenv install --system --deploy --ignore-pipfile || pipenv install --system

# Copy the rest of the application
COPY . .

# Create non-root user (optional but good practice)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 5000

CMD ["uwsgi", "--http", ":5000", "--master", "--enable-threads", "--manage-script-name", "--mount", "/=app:app"]