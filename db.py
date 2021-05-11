import pymongo
 

client = pymongo.MongoClient("mongodb+srv://CalibBot:MUiSB252nDKd7zAj@calibbotcluster.1rxhx.mongodb.net/CalibBotDatabase?retryWrites=true&w=majority")
users_db = client.get_database()["users_db"]
