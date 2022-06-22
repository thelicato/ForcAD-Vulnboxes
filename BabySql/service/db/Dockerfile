FROM mysql:8.0.22
ARG DEBIAN_FRONTEND=noninteractive

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_USER=baby
ENV MYSQL_PASSWORD=sql
ENV MYSQL_DATABASE=babysql

COPY default-users.sql /docker-entrypoint-initdb.d