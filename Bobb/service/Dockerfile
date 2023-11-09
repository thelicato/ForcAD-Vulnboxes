FROM node:16.18-alpine3.16 as build-frontend
WORKDIR /usr/src/app
COPY frontend ./
RUN npm install
RUN npm run build

FROM python:3.11.6-slim-bullseye

WORKDIR /app
COPY backend ./
# Copy frontend
COPY --from=build-frontend /usr/src/app/dist ./bobb/ui
RUN pip install . && rm -rf ./**

ENTRYPOINT ["bobb"]