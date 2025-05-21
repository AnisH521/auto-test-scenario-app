# An official Python runtime as a parent image
# Using slim reduces image size
FROM python:3.10-slim

# working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Python dependencies from requirements.txt
# --no-cache-dir reduces image size
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]