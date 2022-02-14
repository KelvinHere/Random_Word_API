FROM python:3.8

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Allow django logs to be viewed in real time in terminal
ENV PYTHONUNBUFFERED=1

WORKDIR /restexample
COPY requirements.txt /restexample/
RUN pip install -r requirements.txt
RUN pip install djangorestframework
COPY . /restexample/