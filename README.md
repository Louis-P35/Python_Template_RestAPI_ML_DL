# Python_Template_RestAPI_ML_DL
This is a template of a Python Rest API project for machine learning / deep learning

## Installation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```
project/
│
├── notebooks/                      # Contains Jupyter notebooks
│   └── example.ipynb               # Notebook
│
├── src/                            # Main project source code
│   ├── __init__.py
│   ├── models/                     # Saved trained models
│   │   ├── model.pkl               # Model serialized with pickle
│   │   └── model_loader.py         # Script to load models
│   │
│   ├── api/                        # REST API
│   │   ├── __init__.py
│   │   ├── app.py                  # Main API code (FastAPI/Flask)
│   │   └── utils.py                # Utility functions for the API
│   │
│   ├── frontend/                   # User interface (Streamlit/Gradio)
│   │   ├── __init__.py
│   │   └── app_streamlit.py        # Application with Gradio or Streamlit
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
├── Dockerfile                      # Dockerfile for building the application
└── docker-compose.yml              # Docker Compose to manage containers
```
