#!/usr/bin/env docker build --compress -t pvtmert/picapi -f

FROM debian

ARG FLASK_ENV=production

ENV PORT 80
ENV APPNAME picapi
ENV FLASK_ENV ${FLASK_ENV}
EXPOSE ${PORT}

WORKDIR /data

RUN apt update && apt install -y \
	nfs-kernel-server nfs-common \
	redis webdis nginx uwsgi curl nano \
	postgresql-all uwsgi-plugin-python3 \
	python3 python3-pip python3-dev \
	python3-redis python3-flask

COPY requirements.txt ./
RUN pip3 install -U -r requirements.txt

COPY nginx.conf /etc/nginx/sites-enabled/default
COPY uwsgi.ini  /etc/uwsgi/apps-enabled/${APPNAME}.ini
COPY *.py ./

CMD echo 'export FLASK_ENV="${FLASK_ENV:-'${FLASK_ENV}'}"' \
	| tee -a /etc/default/uwsgi; nginx -t; \
	service redis-server status; \
	service uwsgi start ${APPNAME}; \
	service nginx start; \
	tail -fn99 \
		/var/log/nginx/error.log \
		/var/log/nginx/access.log \
		/var/log/uwsgi/app/${APPNAME}.log
