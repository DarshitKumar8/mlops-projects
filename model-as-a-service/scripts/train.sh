#!/bin/bash

# Exit immediately if a command fails
set -euo pipefail

echo "======================================="
echo "🚀 Starting Model Training Pipeline"
echo "======================================="

# -------- Resolve project root --------
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "Project root: $PROJECT_ROOT"

# -------- Environment variables --------
export MODEL_DIR="${MODEL_DIR:-models/latest}"
export LOG_DIR="${LOG_DIR:-logs}"
export APP_ENV="${APP_ENV:-dev}"
export PYTHONPATH="$PROJECT_ROOT"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="$LOG_DIR/train_$TIMESTAMP.log"

echo "Environment Configuration:"
echo "MODEL_DIR   = $MODEL_DIR"
echo "LOG_DIR     = $LOG_DIR"
echo "APP_ENV     = $APP_ENV"
echo "PYTHONPATH  = $PYTHONPATH"
echo "Log file    = $LOG_FILE"

# -------- Create required directories --------
mkdir -p "$MODEL_DIR"
mkdir -p "$LOG_DIR"

echo "---------------------------------------"
echo "Running training..."
echo "---------------------------------------"

# -------- Run training with logging --------
python -m src.model_service.train 2>&1 | tee "$LOG_FILE"

echo "---------------------------------------"
echo "✅ Training completed successfully."
echo "Logs saved to $LOG_FILE"
echo "======================================="