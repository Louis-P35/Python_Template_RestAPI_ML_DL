# Python_Template_RestAPI_ML_DL
This is a template of a Python Rest API project for machine learning / deep learning

## Installation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
    ex: pip install "fastapi[satadard]"


# Build and run both backend & frontend
docker-compose up --build

# Build the api docker
cd src/api
docker build -t docker_api .                    # Build the Docker image
docker images                                   # check if the image is available locally

# Run the Docker image with port mapping to expose the API outside the container
docker run -it --rm -p 8000:8000 docker_api

# Build the frontend docker
cd src/frontend
docker build -t streamlit_frontend .

# Run the frontend (streamlit app) without docker
streamlit run app_streamlit.py
# Run the frontend (streamlit app) docker
docker run -it --rm -p 8501:8501 streamlit_frontend


```
project/
│
├── notebooks/                      # Contains Jupyter notebooks
│   └── example.ipynb               # Notebook
│
├── src/                            # Main project source code
│   ├── __init__.py
│   ├── models/                     # Saved trained models
│   │   └── model_loader.py         # Script to load models
│   │
│   ├── api/                        # REST API
│   │   ├── __init__.py
│   │   ├── app.py                  # Main API code (FastAPI/Flask)
│   │   ├── utils.py                # Utility functions for the API
│   │   ├── models/                 # Model-specific utilities
│   │   │   │── trained_model.h5    # Example trained model file
│   │   │   └── model_loader.py         # Script to load models
│   │   ├── requirements.txt        # Dependencies for the API
│   │   └── Dockerfile              # Dockerfile for the API service
│   │
│   ├── frontend/                   # User interface (Streamlit/Gradio)
│   │   ├── __init__.py
│   │   ├── app_streamlit.py        # Main Streamlit/Gradio app
│   │   ├── requirements.txt        # Dependencies for the frontend
│   │   └── Dockerfile              # Dockerfile for the frontend service
│   │
│   └── configs/                    # Project configuration
│       ├── config.yaml             # Configuration file
│       └── settings.py             # Python configuration
│
├── data/                           # Folder for training data
│   ├── raw/                        # Raw data
│   └── processed/                  # Preprocessed data
│
├── tests/                          # Unit and integration tests
│   ├── test_api.py                 # Tests for the API
│   ├── test_models.py              # Tests for models
│   └── test_utils.py               # Tests for utility functions
│
├── .gitlab-ci.yml                  # GitLab CI/CD pipeline
├── requirements.txt                # Project Python dependencies
├── README.md                       # Main documentation
├── setup.py                        # Project installation script
│
└── docker-compose.yml              # Docker Compose to manage containers
```
