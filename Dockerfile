# Use a minimal Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY pdf_joiner.py .

# Default command to run the script
ENTRYPOINT ["python", "pdf_joiner.py"]
