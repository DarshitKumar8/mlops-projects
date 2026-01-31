# Model-as-a-Service (Reproducible Training & Inference)

A fully Dockerized machine learning service designed for reproducibility, isolation, and operational discipline.

This project demonstrates:

- Reproducible Docker builds
- Deterministic training setup
- Config-driven architecture
- Versioned model artifacts (no overwrites)
- Isolated inference service
- Cross-platform reliability

---

## Quickstart (5 Minutes)

### 1. Clone Repository

git clone https://github.com/DarshitKumar8/mlops-projects.git
cd mlops-projects/model-as-a-service

---

### 2. Build Docker Image

docker build -t model-service .

---

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

No local Python installation required for container execution.

---

## Training

Training is deterministic, config-driven, and automatically versioned.

Each training run creates:

models/v1/
models/v2/
models/v3/

Models are never overwritten.

---

### Train Locally (With Virtual Environment)

Create virtual environment (first time only):

python -m venv venv

Activate:

source venv/Scripts/activate

Install dependencies:

pip install -r requirements.txt

Run training:

./scripts/train.sh

---

### Train Inside Docker (Containerized)

Build image:

docker build -t model-service .

Run training:

docker run --rm model-service bash scripts/train.sh

This runs training inside an isolated container.

---

### Persist Model Artifacts From Docker

By default, container files are ephemeral.

To persist models to your host machine:

docker run --rm \
  -v $(pwd)/models:/app/models \
  model-service bash scripts/train.sh

Now versioned models are saved locally.

---

### Training Configuration

Training behavior is fully config-driven:

configs/train_config.yaml

Modify parameters such as:

- model_name
- seed
- output paths

No hardcoded parameters exist inside training logic.

---

## Service Details

- Default Port: 8000
- Environment: dev
- Model Directory: models/vX (auto-versioned)
- Framework: FastAPI + Uvicorn

---

### Custom Port Example

docker run -p 9000:9000 -e PORT=9000 model-service

---

## Project Structure

model-as-a-service/
│
├── Dockerfile
├── README.md
├── requirements.txt
│
├── configs/
│   └── train_config.yaml
│
├── models/
│   └── v1/, v2/, ...
│
├── scripts/
│   └── train.sh
│
├── src/
│
└── tests/

---

## Design Principles

This project emphasizes:

- Reproducible builds
- Deterministic training
- Automatic model versioning
- Config-driven architecture
- Environment isolation via Docker
- Explicit dependency management
- Cross-platform consistency
- Operational clarity over ML complexity

The model itself is intentionally simple.  
The system design is the focus.

---

## Running Tests (Optional)

To run tests inside container:

docker run model-service pytest tests/

---

## Stopping the Service

If running in foreground:

CTRL + C

If running in background:

docker ps
docker stop <container_id>

---

## What This Project Proves

If the system builds and runs successfully from a fresh machine, it demonstrates:

- No hidden local dependencies
- Proper dependency declaration
- Docker layering discipline
- Operational reproducibility
- Deterministic training behavior
- Version-controlled model artifacts
- Cross-platform compatibility