FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code and data into the image
COPY src/ ./src/

CMD ["python", "src/python_app/run.py"]
