from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI") or "mongodb://localhost:27017/SomeDatabase"
app.config['MONGO_DATABASE'] = os.getenv("MONGO_DATABASE") or 'SomeCollection'
app.config['SECRET_KEY'] = 'secret_key'

mongo = PyMongo(app)
db = mongo.db
col = mongo.db[app.config['MONGO_DATABASE']]
print ("MongoDB Database:", mongo.db)

@app.route("/")
def connect_mongo():
    out = f"Connection: {str(mongo.cx)},"

    for obj in col.find():
        out += f" one object from collection: {obj}"

    return out

i = 42
@app.route("/test")
def test():
    global i
    db.SomeCollection.insert_one({"name": f"Anton{i}"})
    i += 1
    return "testAnton"

if __name__ == '__main__':
    app.run(debug=os.getenv("app_env") == "prod" or True, host='0.0.0.0')
