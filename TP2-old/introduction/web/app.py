import sys

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
global client

@app.route("/")
def index():
    db = client.test
    cursor = db.restaurants.find()
    l = []
    for e in cursor:
        try:
            print e['name']
            print e['address']
            l.append(e['name'])
        except (UnicodeEncodeError):
            pass
    return render_template('show_entries.html', entries=l)

if __name__ == "__main__":
    global client 
    addr = sys.argv[1]
    client = MongoClient("mongodb://" + addr + ":27017")
    app.run(host="0.0.0.0", port=8080)