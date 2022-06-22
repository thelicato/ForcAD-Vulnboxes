FROM python:3.9.13-slim

WORKDIR /usr/src/app

COPY api.py flags.py main.py requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 5005

CMD ["python", "main.py"]