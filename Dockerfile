FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN apt-get -y update && \
    pip install -U PyJWT && \
    pip install -U pymongo
WORKDIR /app
