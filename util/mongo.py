from pymongo import MongoClient
import json

SERVER_ADDR="68.183.120.187"
client=MongoClient(SERVER_ADDR,27017)
db=client.geoquest
collection=db.main
with open('../data/quests.json') as f:
    data = json.load(f)



# def drop():
#     client.drop_database("")

def build_db(ipaddress):
    drop()
    client.close()
    client = MongoClient(ipaddress, 27017)
    db = client['mongolia']
    collection = db['pokedex']
    with open('pokedex.json') as f:
        data = json.load(f)
        collection.insert_many(data["pokemon"])

def add_user(name):
    with open('../data/quests.json',"r") as f:
        data = json.load(f)
        if not name in data["users"]:
            data["users"].append(name)

    with open('../data/quests.json',"w") as f:
        json.dump(data,f)
        # f.truncate()


def add_location(name,long,lat,address,reviews,type):

    with open('../data/quests.json',"r") as f:
        data = json.load(f)
        data["locations"][name]={"long" : long , "lat":lat, "address":address, "reviews":reviews, "type":type}
    with open('../data/quests.json',"w") as f:
        json.dump(data,f)
        # f.truncate()

add_location("stuyvesant",55,45,"chambers",["bad"],"school")


def update_mongo():
    with open('../data/quests.json',"r") as f:
        collection.insert_many()
