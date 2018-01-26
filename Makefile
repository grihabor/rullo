IMAGE=rullo:latest

all: docker-tests

docker-tests:
	docker build . \
		-f tests/Dockerfile \
		-t $(IMAGE) 
	docker run $(IMAGE)

.PHONY: docker-tests all
