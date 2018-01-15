FROM node:wheezy

RUN npm install spa-http-server -g
RUN mkdir /code
WORKDIR /code
ADD package.json .
RUN yarn install
ADD . .
WORKDIR .
RUN npm run build
