import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")

mydb = myclient["PrdConfig"]

user_session = mydb["UserDetails"]

def Fetch_User_Info(key):
     
     for i in user_session.find({'key' : key}) :
          return i