FROM node:latest
RUN npm install -g npm-run-all
WORKDIR /usr/share/src
COPY src/. .
RUN npm install
WORKDIR /usr/share/src/client
RUN npm install
RUN npm run build
WORKDIR /usr/share/src
CMD npm run dev