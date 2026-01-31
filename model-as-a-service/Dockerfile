FROM python:3.10-slim

WORKDIR /app

# ---------- Install dependencies ----------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Copy project files ----------
COPY src/ src/
COPY scripts/ scripts/
COPY models/ models/
COPY configs/ configs/

RUN chmod +x scripts/*.sh

# ---------- Environment Variables ----------
ENV MODEL_DIR=models
ENV LOG_DIR=logs
ENV APP_ENV=dev
ENV PORT=8000
ENV PYTHONPATH=/app

# ---------- Expose port ----------
EXPOSE 8000

# ---------- Volume mounts ----------
VOLUME ["/app/models", "/app/logs"]

# ---------- Start service ----------
CMD ["bash", "scripts/serve.sh"]