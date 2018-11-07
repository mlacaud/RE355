FROM mongo

# dependencies
RUN mkdir -p /usr/src/data
COPY primer-dataset.json /usr/src/data
WORKDIR /usr/src/data

RUN mongod --fork --logpath=/tmp/mongodb.log --dbpath /usr/src/data && sleep 5 && mongoimport -h localhost --db test --collection restaurants --drop --file primer-dataset.json

CMD mongod --dbpath /usr/src/data
