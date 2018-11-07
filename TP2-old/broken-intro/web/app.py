import sys
import time

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
global client

@app.route("/")
def index():
    start_time = time.time()
    db = client.test
    cursor = db.restaurants.find()
    l = []
    for e in cursor:
        try:
            l.append(str(e['name']))
        except (UnicodeEncodeError):
            pass
    elapsed_time = time.time() - start_time
    return render_template('show_entries.html', entries=l, elapsed_time=elapsed_time)

if __name__ == "__main__":
    global client
    addr = sys.argv[1]
    client = MongoClient("mongodb://" + addr + ":27017")
    app.run(host="0.0.0.0", port=8080)
