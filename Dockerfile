# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app ./app

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI using Uvicorn
# Note: 'app.main:app' = app/main.py contains "app = FastAPI()"
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
