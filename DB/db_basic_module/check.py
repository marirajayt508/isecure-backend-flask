import DB.db_basic_module.connection as connection
import Modules.KeySecurity.isecure as keysecure
#myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")



KeyDetails = connection.keydb()


def check_keys(key):
    keys = KeyDetails.find({'key' : key})
    
    if keys == None :
        return False
    else :
       for i in keys :
          if i['key'] == key :
              
              print("-- KEY Found -- "+key)
              return True
          elif i['key'] == None:
              return False
          else :
              print("-- KEY Not Found -- "+key)
              return False
     


#dsaghj34jkhsdfjsh
  