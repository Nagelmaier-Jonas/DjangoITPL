FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY . /my_app_dir
WORKDIR /my_app_dir
RUN python -m pip install -r requirements
RUN python manage.py makemigrations