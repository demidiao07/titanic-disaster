FROM python:3.12

# Set working directory in the container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script into the container
COPY titanic_model.py .

# Command to run your script
CMD ["python", "titanic_model.py"]
