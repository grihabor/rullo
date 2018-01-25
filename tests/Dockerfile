FROM python:3.6-alpine
MAINTAINER Borodin Gregory <grihabor@mail.ru>

WORKDIR /project

ADD . .
RUN pip3 install .

CMD ["python3", "setup.py", "test"]