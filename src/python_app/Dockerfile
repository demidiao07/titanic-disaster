# Use a lightweight official Python image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt from the root of your project
COPY ../../requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code into the container
COPY . .

# Command to run your script
CMD ["python", "run.py"]