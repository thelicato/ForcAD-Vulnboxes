FROM alpine/socat:1.7.4.4

WORKDIR /usr/src/app

COPY hashme.py requirements.txt ./
RUN apk update && apk add python3 py3-pip && pip install -r requirements.txt
EXPOSE 5002

ENTRYPOINT ["socat", "TCP-LISTEN:5002,fork", "EXEC:'python3 hashme.py'"]