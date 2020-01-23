#!/usr/bin/env -S docker build --compress -t pvtmert/picapi:full -f

FROM debian:10

RUN apt update && apt install -y \
	nfs-kernel-server nfs-common \
	redis webdis nginx uwsgi curl nano \
	postgresql-all uwsgi-plugin-python3 \
	python3 python3-pip python3-dev \
	python3-redis python3-flask \
	procps net-tools

WORKDIR /data

COPY ./requirements.txt ./
RUN pip3 install -U -r requirements.txt

ENV FLASK_ENV ${FLASK_ENV:-production}
ENV APPNAME api

COPY ./cfg/nginx.conf /etc/nginx/sites-enabled/default
COPY ./cfg/uwsgi.ini  /etc/uwsgi/apps-enabled/${APPNAME}.ini
COPY ${APPNAME} ./${APPNAME}

ENV PORT 80
EXPOSE ${PORT}

CMD echo 'export FLASK_ENV="${FLASK_ENV:-'${FLASK_ENV}'}"' \
	| tee -a /etc/default/uwsgi; nginx -t; \
	service redis-server status; \
	service uwsgi start; \
	service nginx start; \
	tail -fn99 \
		/var/log/nginx/error.log \
		/var/log/nginx/access.log \
		/var/log/uwsgi/app/${APPNAME}.log
