FROM python:3.12

WORKDIR /app

COPY src/python_app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/python_app/titanic_model.py .

# Copy data folder from one level up (src/data → /app/data)
COPY src/data ./data

CMD ["python", "titanic_model.py"]
