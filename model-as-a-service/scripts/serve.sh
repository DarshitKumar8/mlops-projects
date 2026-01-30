#!/bin/bash
set -e

echo "Starting service..."

# -------- Configurable environment variables --------
MODEL_DIR=${MODEL_DIR:-models/latest}
LOG_DIR=${LOG_DIR:-logs}
APP_ENV=${APP_ENV:-dev}
PORT=${PORT:-8000}

export MODEL_DIR
export LOG_DIR
export APP_ENV
export PYTHONPATH=/app

echo "MODEL_DIR  = $MODEL_DIR"
echo "APP_ENV    = $APP_ENV"
echo "PORT       = $PORT"
echo "PYTHONPATH = $PYTHONPATH"

# -------- Enforce serving rule --------
if [ ! -d "$MODEL_DIR" ]; then
  echo "MODEL_DIR does not exist. Run training first."
  exit 1
fi

echo "Launching service on port $PORT..."

python -m src.model_service.serve --port $PORT