#!/bin/bash
set -e

echo "Starting service..."

# -------- Environment variables --------
export MODEL_DIR=models/latest
export LOG_DIR=logs
export APP_ENV=dev
export PYTHONPATH=/app

echo "MODEL_DIR = $MODEL_DIR"
echo "APP_ENV   = $APP_ENV"
echo "PYTHONPATH = $PYTHONPATH"

# -------- Enforce serving rule --------
if [ ! -d "$MODEL_DIR" ]; then
  echo "MODEL_DIR does not exist. Run training first."
  exit 1
fi

echo "Launching service..."
python -m src.model_service.serve