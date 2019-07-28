#!/usr/bin/env make -f

IPORT := 80
EPORT := 80
IMAGE := pvtmert/picapi
FLASK_ENV := development

all:
	# maybe use 'run' ?

docker: dockerfile
	docker build -t $(IMAGE) -f $< .

run: docker
	docker run --rm -it -e FLASK_ENV=$(FLASK_ENV) \
		-p $(EPORT):$(IPORT) -v $$(pwd):/data \
		$(IMAGE)

deps: requirements.txt
	pip3 install --user -U -r $<

local: deps
	python3 main.py
