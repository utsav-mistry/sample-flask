# Use a lightweight Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_APP=run.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

# Set working directory
WORKDIR /app

# Install dependencies FIRST (better cache layer)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code LAST (changes here don't invalidate pip cache)
COPY . .

EXPOSE 5000

CMD ["python", "run.py"]