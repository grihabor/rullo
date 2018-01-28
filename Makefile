IMAGE=rullo:latest

all: docker-tests

docker-tests:
	docker build . \
		-f tests/Dockerfile \
		-t $(IMAGE) 
	docker run \
		-v rullo_tests_eggs:/project/.eggs \
		$(IMAGE)

.PHONY: docker-tests all
