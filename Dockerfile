# Use Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    zlib1g-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy code
COPY . .

# Install Python dependencies
RUN pip install -r requirements_all.txt

# Run test suite
CMD ["pytest"]
