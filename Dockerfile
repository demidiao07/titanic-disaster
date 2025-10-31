FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your src folder
COPY src/ src/

# Default command to run your script
CMD ["python", "src/python_app/run.py"]
