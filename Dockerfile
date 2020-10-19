FROM python:3.8

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y vim less

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Uncomment for building images that will be pushed to repo
# COPY app/ /usr/src/app

# python manage.py runserver 0.0.0.0:8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
