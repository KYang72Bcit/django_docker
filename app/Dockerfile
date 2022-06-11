FROM python:3.9.12-alpine

WORKDIR /usr/src/app
# COPY . .

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add netcat-openbsd 

RUN pip install --upgrade pip
COPY req_dev.txt .
RUN pip install -r req_dev.txt

# RUN mkdir -p /vol/web/static/

# COPY wait.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/wait.sh
# RUN chmod +x /usr/src/app/wait.sh

COPY ./wait.sh .
RUN sed -i 's/\r$//g' /usr/src/app/wait.sh
RUN chmod +x /usr/src/app/wait.sh
# RUN sed -i 's/\r$//g' wait.sh
# RUN chmod +x wait.sh

COPY . .


ENTRYPOINT ["/usr/src/app/wait.sh"]




