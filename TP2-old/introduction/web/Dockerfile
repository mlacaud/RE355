FROM ubuntu

# dependencies
RUN apt-get update && apt-get install --yes python-pip iputils-ping
RUN pip install flask pymongo

# copy source code
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

CMD addr=`ping -c 1 data | grep "PING" | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'` && python app.py $addr