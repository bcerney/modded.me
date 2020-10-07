# https://learndjango.com/tutorials/django-docker-and-postgresql-tutorial
# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setup venv
# ENV VENV_PATH=/opt/venv
# RUN python3 -m venv $VENV_PATH
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set work directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project
COPY . /app/
