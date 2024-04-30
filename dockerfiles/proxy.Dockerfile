FROM nginx:alpine
ENV TZ=Europe/Moscow
COPY ./nginx.conf /etc/nginx/nginx.conf