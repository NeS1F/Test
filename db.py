import pymongo
 

client = pymongo.MongoClient("mongodb+srv://CalibBot:718293465calibbot@calibbotcluster.1rxhx.mongodb.net/CalibBotDatabase.users_db?retryWrites=true&w=majority")
users_db = client.test

#get_database()["users_db"]
