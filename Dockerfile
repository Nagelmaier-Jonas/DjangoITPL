FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /my_app_dir
RUN pip freeze > requirements
RUN pip install --upgrade pip
COPY ./requirements /my_app_dir
WORKDIR /my_app_dir
RUN python -m pip install -r requirements
COPY . /my_app_dir
RUN python manage.py makemigrations
CMD ["./start.sh"]
