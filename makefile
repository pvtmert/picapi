#!/usr/bin/env make -f

IPORT := 80
EPORT := 80
IMAGE := pvtmert/picapi:full
FLASK_ENV := development

all:
	# maybe use 'run' or 'local' ?

docker: full.dockerfile
	docker build -t $(IMAGE) -f $< .

run: docker
	docker run --rm -it -e FLASK_ENV=$(FLASK_ENV) \
		-p $(EPORT):$(IPORT) -v $$(pwd):/data \
		$(IMAGE)

deps: requirements.txt
	pip3 install --user -U -r $<

local: deps
	FLASK_ENV=development python3 -m api 8080

clean:
	-find . -iname __pycache__ -exec rm -rf {} +
	-docker rmi $(IMAGE)
