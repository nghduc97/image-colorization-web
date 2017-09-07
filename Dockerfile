FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN apt-get -y update
COPY ./server /app
COPY ./client/dist /template
WORKDIR /app
