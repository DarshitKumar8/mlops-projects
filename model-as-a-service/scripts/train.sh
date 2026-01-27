#!/bin/bash
set -e

echo "Bootstrapping training environment..."

# -------- Environment variables --------
export MODEL_DIR=models/latest
export LOG_DIR=logs
export APP_ENV=dev
export PYTHONPATH=/app

echo "MODEL_DIR = $MODEL_DIR"
echo "APP_ENV   = $APP_ENV"
echo "PYTHONPATH = $PYTHONPATH"

mkdir -p "$MODEL_DIR"
mkdir -p "$LOG_DIR"

echo "Running training..."
python -m src.model_service.train

echo "Training finished."