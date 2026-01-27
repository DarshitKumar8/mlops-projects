FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY scripts/ scripts/
COPY models/ models/
COPY configs/ configs/
RUN chmod +x scripts/*.sh

EXPOSE 8000

VOLUME ["/app/models", "/app/logs"]

CMD ["bash", "scripts/serve.sh"]
