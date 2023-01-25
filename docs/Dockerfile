FROM node:19

WORKDIR /docs
COPY package.json .

RUN npm install
RUN npm i -g @redocly/cli@latest
EXPOSE 8080

ENTRYPOINT ["npm","start"]