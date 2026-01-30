# Model-as-a-Service (Reproducible Training & Inference)

A fully Dockerized machine learning service designed for reproducibility, isolation, and operational discipline.

This project demonstrates:

- Reproducible Docker builds
- Isolated inference service
- Versioned model artifacts
- Deterministic training setup
- Cross-platform reliability

---

## Quickstart (5 Minutes)

### 1. Clone Repository

git clone https://github.com/DarshitKumar8/mlops-projects.git
cd mlops-projects/model-as-a-service

### 2. Build Docker Image

docker build -t model-service .

### 3. Run Service

docker run -p 8000:8000 model-service

The service will start at:

http://localhost:8000

---

### 4. Test Inference (Open New Terminal)

curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"feature1": 1, "feature2": 2}'

---

### Expected Response

{
  "input": {
    "feature1": 1,
    "feature2": 2
  },
  "prediction": "dummy_output",
  "model_version": 1
}

If you see this response, the system has been successfully rebuilt from zero.

---

## Requirements

- Docker installed
- Git installed

No local Python installation required.

---

## Service Details

- Default Port: 8000
- Environment: dev
- Model Directory: models/latest
- Framework: FastAPI + Uvicorn

---

## Project Structure

model-as-a-service/
│
├── Dockerfile
├── README.md
├── requirements.txt
├── auth.py
│
├── configs/
├── models/
├── scripts/
├── src/
└── tests/

---

## Design Principles

This project emphasizes:

- Reproducible builds
- Environment isolation via Docker
- Explicit dependency management
- Cross-platform consistency (Linux container runtime)
- Operational clarity over ML complexity

The model itself is intentionally simple.  
The system design is the focus.

---

## Running Tests (Optional)

To run tests inside container:

docker run model-service pytest tests/

---

## Training (If Implemented)

If a training script exists:

docker run model-service bash scripts/train.sh

Training outputs versioned model artifacts under the `models/` directory.

---

## Stopping the Service

Press:

CTRL + C

Or if running in background:

docker ps
docker stop <container_id>

---

## What This Project Proves

If the system builds and runs successfully from a fresh machine, it demonstrates:

- No hidden local dependencies
- Proper dependency declaration
- Docker layering discipline
- Operational reproducibility
- Cross-platform compatibility