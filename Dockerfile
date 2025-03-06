# Use an official Python 3.13 runtime as a parent image
FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools

RUN pip install --no-cache-dir --upgrade pip

USER root

# Set the working directory in the container
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 3111
ENV LISTEN_PORT=3111

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3111"]