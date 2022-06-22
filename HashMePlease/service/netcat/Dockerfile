FROM alpine/socat:1.7.4.3-r0

WORKDIR /usr/src/app

COPY hashme.py requirements.txt ./
RUN apk update && apk add python3 py3-pip && pip install -r requirements.txt
EXPOSE 9600

ENTRYPOINT ["socat", "TCP-LISTEN:9600,fork", "EXEC:'python3 hashme.py'"]