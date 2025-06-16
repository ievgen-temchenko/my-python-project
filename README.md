# My Python Project

A FastAPI-based Python project with a clean, modular structure.

## Features

- FastAPI framework for building APIs
- Modular project structure
- Pydantic models for data validation
- Built-in testing with pytest
- Development and production configurations

## Project Structure

```
my-python-project/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       └── items.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   └── __init__.py
│   └── services/
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── main.py
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install development dependencies (optional):
```bash
pip install -r requirements-dev.txt
```

## Running the Application

Start the development server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

The API will be available at:
- Main application: http://localhost:8000
- API documentation: http://localhost:8000/docs
- Alternative docs: http://localhost:8000/redoc

## Public Endpoints

- `GET /` - Root endpoint (health check)
- `GET /api/v1/items/` - Get all items (main public endpoint)
- `GET /api/v1/items/{item_id}` - Get specific item
- `POST /api/v1/items/` - Create new item

## Testing

Run tests with pytest:
```bash
pytest
```

Run with coverage:
```bash
pytest --cov=app
```

## Environment Variables

- `SECRET_KEY` - Secret key for security
- `DATABASE_URL` - Database connection string
- `ENVIRONMENT` - Environment (development/production)
- `DEBUG` - Debug mode (True/False)