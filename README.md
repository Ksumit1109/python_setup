# Python FastAPI Project

A simple FastAPI web application with file upload functionality and multiple API endpoints.

## Project Structure

```
python_setup/
├── main.py              # Main FastAPI application
├── venv/                # Virtual environment
├── README.md            # This file
├── requirements.txt     # Project dependencies
└── __pycache__/         # Python cache files
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd python_setup

# Or simply navigate to the project directory
cd path/to/your/python_setup/project
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install required packages
pip install fastapi uvicorn python-multipart

# Or install from requirements.txt
pip install -r requirements.txt
```

**Note**: The project already includes a virtual environment with dependencies installed. If you're using the existing venv, you can skip this step.

### 4. Run the Application

```bash
# Run the FastAPI application
python main.py

# Or using uvicorn directly
uvicorn main:app --reload
```

The application will be available at: `http://localhost:8000`

## API Endpoints

### GET /
- **Description**: Root endpoint - Welcome page
- **Method**: GET
- **Response**: 
  ```json
  {
    "message": "Welcome to Main "
  }
  ```

### GET /contact
- **Description**: Contact page endpoint
- **Method**: GET
- **Response**: 
  ```json
  {
    "Message": "Welcome to Contact page"
  }
  ```

### POST /upload
- **Description**: File upload endpoint for handling multiple files
- **Method**: POST
- **Content-Type**: `multipart/form-data`
- **Parameters**: 
  - `files`: List of uploaded files (multiple files supported)
- **Response**: 
  ```json
  {
    "status": "File received"
  }
  ```
- **Note**: Currently prints file information to console for debugging

## Code Structure

### main.py Overview

The application is built using FastAPI and consists of:

```python
from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()
```

**Key Components:**
- **FastAPI**: Modern web framework for building APIs
- **UploadFile**: Special type for handling file uploads
- **uvicorn**: ASGI server for running the application

### Application Runner

```python
if __name__ == "__main__":
    uvicorn.run("main:app")
```

This pattern ensures:
- Server starts only when running the script directly (`python main.py`)
- Allows importing the app in other modules without starting the server
- Uses uvicorn to serve the FastAPI application on `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- **Interactive API docs (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative API docs (ReDoc)**: `http://localhost:8000/redoc`

## Testing the API

### Using Browser
- Visit `http://localhost:8000` for the root endpoint
- Visit `http://localhost:8000/contact` for the contact endpoint

### Using curl
```bash
# Test root endpoint
curl http://localhost:8000/

# Test contact endpoint
curl http://localhost:8000/contact

# Test file upload
curl -X POST "http://localhost:8000/upload" \
     -H "Content-Type: multipart/form-data" \
     -F "files=@path/to/your/file.txt"
```

### Using the Interactive Docs
1. Start the server: `python main.py`
2. Open `http://localhost:8000/docs` in your browser
3. Use the "Try it out" buttons to test each endpoint
4. For file upload, use the file picker in the Swagger UI

## Development

### Virtual Environment Management

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Deactivate virtual environment
deactivate

# Remove virtual environment (if needed)
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows
```

### Adding New Dependencies

```bash
# Install new package
pip install package-name

# Save dependencies to requirements.txt
pip freeze > requirements.txt
```

### Running in Development Mode

```bash
# Run with auto-reload for development
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Troubleshooting

### Common Issues

1. **Command not found error when activating venv**
   - Make sure you're using the correct path separator (`\` for Windows, `/` for Unix)
   - Ensure you're in the correct directory

2. **Module not found errors**
   - Make sure the virtual environment is activated
   - Install required dependencies with `pip install`

3. **Port already in use**
   - Change the port: `uvicorn main:app --reload --port 8001`
   - Or kill the process using the port

### Getting Help

- Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Review the [Uvicorn documentation](https://www.uvicorn.org/)

## License

This project is open source and available under the [MIT License](LICENSE).
