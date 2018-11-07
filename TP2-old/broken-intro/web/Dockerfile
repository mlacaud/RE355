FROM ubuntu

# dependencies
RUN apt-get update && apt-get install --yes python-pip iputils-ping
RUN pip install flask pymongo

# copy source code
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

CMD python app.py 172.78.238.11
