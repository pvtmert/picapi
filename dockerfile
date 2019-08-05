#!/usr/bin/env docker build --compress -t pvtmert/picapi -f

FROM debian

ENV PORT 80
EXPOSE ${PORT}
WORKDIR /data

RUN apt update && apt install -y \
	nfs-kernel-server nfs-common \
	redis webdis nginx uwsgi curl nano \
	postgresql-all uwsgi-plugin-python3 \
	python3 python3-pip python3-dev \
	python3-redis python3-flask \
	procps net-tools

COPY api/requirements.txt ./
RUN pip3 install -U -r requirements.txt

ARG FLASK_ENV=production
ENV FLASK_ENV ${FLASK_ENV}
ENV APPNAME api

COPY nginx.conf /etc/nginx/sites-enabled/default
COPY uwsgi.ini  /etc/uwsgi/apps-enabled/${APPNAME}.ini
COPY ${APPNAME} ./


CMD echo 'export FLASK_ENV="${FLASK_ENV:-'${FLASK_ENV}'}"' \
	| tee -a /etc/default/uwsgi; nginx -t; \
	service redis-server status; \
	service uwsgi start; \
	service nginx start; \
	tail -fn99 \
		/var/log/nginx/error.log \
		/var/log/nginx/access.log \
		/var/log/uwsgi/app/${APPNAME}.log
