from pymongo import MongoClient
import json

SERVER_ADDR="68.183.120.187"
client=MongoClient(SERVER_ADDR,27017)
db=client.geoquest
collection=db.main
with open('data/quests.json') as f:
    data = json.load(f)



# def drop():
#     client.drop_database("")
#
# def build_db(ipaddress):
#     drop()
#     client.close()
#     client = MongoClient(ipaddress, 27017)
#     db = client['mongolia']
#     collection = db['pokedex']
#     with open('pokedex.json') as f:
#         data = json.load(f)
#         collection.insert_many(data["pokemon"])

def add_user(name):
    with open('data/quests.json',"r") as f:
        data = json.load(f)
        if not name in data["users"]:
            data["users"].append(name)

    with open('data/quests.json',"w") as f:
        json.dump(data,f)
        # f.truncate()


def add_location(name,long,lat,address,reviews,type):
    with open('data/quests.json',"r") as f:
        data = json.load(f)
        data["locations"][name]={"long" : long , "lat":lat, "address":address, "reviews":reviews, "type":type}
    with open('data/quests.json',"w") as f:
        json.dump(data,f)
        # f.truncate()

def add_quest(name,list_loc, time):
    with open('data/quests.json',"r") as f:
        data = json.load(f)
        data["quests"][name]={"list_loc":list_loc, "time":time}
    with open('data/quests.json',"w") as f:
        json.dump(data,f)


# add_location("Central Park", 40.7828647,-73.9653551, "Central Park", ["good"], "Outside")
# add_location("Hudson River Waterfront Greenway", 40.7876879,-73.9832952, "New York State Reference Rte 907V, New York, NY 10024", ["amazing"], "Outside")
# # add_location("Central Park", 40.7828647,-73.9653551, "Central Park", ["good"], "Outside")
#
# allLocs=[]
# with open('data/quests.json',"r") as f:
#     data=json.load(f)
#     for i in data["locations"]:
#         allLocs.append(i)
#
#
# print("hi")
# print(allLocs)
#
# add_quest("Nature Lover's Trail",allLocs)
#
# def update_mongo():
#     with open('data/quests.json',"r") as f:
#         collection.insert_many()
#
# def getQuests():
#     with open('data/quests.json',"r") as f:
#         data=json.load(f)
#         return data["quests"]
