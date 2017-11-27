FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install -U \
    flask-jwt-extended \
    sqlalchemy \
    pygresql
COPY ./client/dist /template
WORKDIR /server
