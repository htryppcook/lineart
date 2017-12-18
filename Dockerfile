
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN mkdir /prep
WORKDIR /prep
ADD requirements.txt /prep/
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code
#ENTRYPOINT ["/bin/bash"]

