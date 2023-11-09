FROM mysql:5.7
ARG DEBIAN_FRONTEND=noninteractive

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_USER=code
ENV MYSQL_PASSWORD=maze
ENV MYSQL_DATABASE=codemaze

COPY default-users.sql /docker-entrypoint-initdb.d