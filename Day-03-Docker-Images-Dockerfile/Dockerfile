# Base image - slim = smaller size
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (smart caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ .

# Open this port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
