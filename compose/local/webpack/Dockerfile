FROM node:14-slim 

COPY ./compose/local/webpack/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/start"]
