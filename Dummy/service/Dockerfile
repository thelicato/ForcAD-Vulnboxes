FROM node:alpine3.16

WORKDIR /usr/src/app

COPY package.json yarn.lock ./
COPY src ./src
RUN yarn install
EXPOSE 5001

CMD ["node", "src/server.js"]