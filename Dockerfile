FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN apt-get -y update && \
    pip install -U flask-cors && \
    pip install -U pymongo
WORKDIR /app
