FROM imagecolorizationweb_client AS client

FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install -U \
    flask-jwt-extended \
    sqlalchemy \
    pygresql
WORKDIR /app
COPY . /app
COPY --from=client /app/dist /app/static
