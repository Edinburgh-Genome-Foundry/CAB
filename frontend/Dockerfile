FROM node:wheezy

RUN npm install spa-http-server -g
RUN mkdir /code
ADD . /code
WORKDIR /code
RUN npm install
RUN npm run build
