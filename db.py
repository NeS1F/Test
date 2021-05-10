import pymongo
 
client = pymongo.MongoClient('mongodb://localhost/calibrationbot')
users_db = client.get_database()["users_db"]