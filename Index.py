from flask import Flask,jsonify, request
from flask_cors import CORS
app = Flask(__name__)
import Flow

@app.route('/',methods = ['POST','GET'])
def Index():
    return "This is Index" 

@app.route('/ping',methods = ['POST','GET'])
def ping():
    data = request.get_json()
    return data

@app.route('/Register',methods = ['POST','GET'])
def Register():
    data = request.get_json()
    Flow.keypassmailer(data['email'],Flow.Encryption(data['key']))
    return Flow.Encryption(data['key'])
    
@app.route('/Getkey',methods = ['POST','GET'])
def getkey():
    data = request.get_json()
    return Flow.get_key({"email" : "marirajayt508@gmail.com"})
    
@app.route('/Otp',methods = ['POST','GET'])
def otp():
    data = request.get_json()
    otp_val = Flow.otps()
    Flow.otpmailer(data['email'],otp_val)
    return otp_val
    
@app.route('/Encryption',methods = ['POST','GET'])
def Encryption():
    data = request.get_json()
    #return jsonify({'data':data['key']})
    return Flow.Encryption(data['key'])
  
@app.route('/Check',methods = ['POST','GET'])  
def Name_check():
    data = request.get_json()
    #return jsonify({'data':data['key']})
    if Flow.check_name(data) :
        msg = "false"
    else :
        msg = "true"
    
    return msg


@app.route('/Decryption',methods = ['POST','GET'])
def Decryption():
    #encrypted = {"Encrypted_datas": {"keys": {"key1": "utfpbb6FIHhsvP_gBtcDwW_prPybgk2msM2SNt3l4BE=", "key2": "0j1C8eXOeX9HkuxF_fqW3xTkGWsRrjCX5MiwdZgflnw=", "key3": "adFQDn0V6bpiwQjt-ulV9bXgIHdM4v5LOL3YwLiy1eU="}, "Other_datas": {"data1": "gAAAAABiODgI1luofa1fGOuceKVdZDcjlUoRSN9OjS9Th16TuT0itOdaehb1MIqsvukMdAJgbQ2d0PiO4yNF5dcyIYgN9jgbDcDFIfI1rtU82dWLIo3yLHY=", "data2": "gAAAAABiODgIQVkhEPX2Iptl3nCJ1v9SBD0VSk4ryb7Ow7d-yLqT51j5r0D4Q9j4eoIsZRbvk46E1LhZAgcH1R_jMXaHsPjm5RAcC0ho-w_9ZuoN5jf1If275Ay2kqunxo6srTvHXPPuXhjvIG3UNM6nZmd7pGJ0N78140sUzUxIZmwSoB3g6EWLE5vY8rmcKlacvAlgKBdFd6FOPO8qbUsC-DkAYhdBW7rt_3HXdw9lZe--EVM8yfg=", "data3": "gAAAAABiODgIVj3iIQABRQgyy99RrDuSN62jVtSN32lvnKndJ_GvriZzEAlo9lvItSnh8MIZL_HSpzqKX8viRxodAR5heEC9wmRn5YsTeVmwC5VqWn4_BooWCvHpJin-Sz_2qQJsn5agmmoEDW1GfwDGqdjqvakFU9A7U7_bhP45cfYyJMmysGBSeVki2GJE4KC_xjbip4gpyRn0VDL2qOdW3Z4h7lg0jACKc48wtnQVXfjI7JaBCfyA3DIvlXwukvEljSrpmdxbu6n9SMKWH6MDS2XlnH8k0nmK4pnzUxNEA1TP3TIft7wDpKL8JeKcQ-dcdqRL3VeMHHmRJOo238XiuBrGtJrOVybKqFLsGTStNCSbnUqpTeRDwnrwFmN78LcDoY1ZoJQUjk4rPle0rQbd2-svAbxkwg=="}, "isecure": {"key1": "utfpbb6FIHhsvP_gBtcDwW_prPybgk2msM2SNt3l4BE=", "key2": "0j1C8eXOeX9HkuxF_fqW3xTkGWsRrjCX5MiwdZgflnw=", "key3": "adFQDn0V6bpiwQjt-ulV9bXgIHdM4v5LOL3YwLiy1eU="}, "data": "gAAAAABiODgIVj3iIQABRQgyy99RrDuSN62jVtSN32lvnKndJ_GvriZzEAlo9lvItSnh8MIZL_HSpzqKX8viRxodAR5heEC9wmRn5YsTeVmwC5VqWn4_BooWCvHpJin-Sz_2qQJsn5agmmoEDW1GfwDGqdjqvakFU9A7U7_bhP45cfYyJMmysGBSeVki2GJE4KC_xjbip4gpyRn0VDL2qOdW3Z4h7lg0jACKc48wtnQVXfjI7JaBCfyA3DIvlXwukvEljSrpmdxbu6n9SMKWH6MDS2XlnH8k0nmK4pnzUxNEA1TP3TIft7wDpKL8JeKcQ-dcdqRL3VeMHHmRJOo238XiuBrGtJrOVybKqFLsGTStNCSbnUqpTeRDwnrwFmN78LcDoY1ZoJQUjk4rPle0rQbd2-svAbxkwg=="}}
    encrypted = request.get_json()
    #print(content['mytext']) 'Encrypted_datas' : {
    #return jsonify({"uuid":uuid})
    key1 = encrypted['Encrypted_datas']['keys']['key1']
    key2 = encrypted['Encrypted_datas']['keys']['key2']
    key3 = encrypted['Encrypted_datas']['keys']['key3']
    endata = encrypted['Encrypted_datas']['data']
    return Flow.Decryption(key1,key2,key3,endata)
    #return Flow.Decryption(key1,key2,key3,endata)

@app.route('/InsertBasicLogin',methods = ['POST','GET'])
def InsertBasicLogin():
    data = request.get_json()
    col = ['BaicDetails','KeyDetails','UserDetails']
    if data['collection'] in col :

        if (data['collection'] == "BaicDetails") : #name,password,key,collection
            Flow.BasicInsert(data['name'],data['password'],data['key'])
            return "Basic Details Inserted"

        elif (data["collection"]=="KeyDetails") :  #key,collection
            if(Flow.check_key(data['key'])):
               return "Ohh Sorry, Data Alredy Exist !!!.."
            else :   
               Flow.KeyInsert(data['key'])
               return "Key Details Inserted"

        elif (data["collection"]=="UserDetails") : #name/firstname,lastname,code,phonenumber
            Flow.UserInsert(data['name'],data['firstname'],data['lastname'],data['code'],data['phonenumber'],data['email'],data['password'],data['key'])
            return "User Details Inserted"
        else:
             return "Collection Not Found" 
        return 1
 
    
if __name__ == "__main__" :
      CORS(app)
      app.run()

'''data = request.get_json()
    col = ['BaicDetails','KeyDetails','UserDetails']
    if data['collection'] in col :

        if (data['collection'] == "BaicDetails") : #name,password,key,collection
            Flow.BasicInsert(data['Name'],data['Password'],data['Key'])
            return "Basic Details Inserted"

        elif (data["collection"]=="KeyDetails") :  #key,collection
            Flow.KeyInsert(data['key'])
            return "Key Details Inserted"

        elif (data["collection"]=="UserDetails") : #name/firstname,lastname,code,phonenumber
            Flow.UserInsert(data['name'],data['firstname'],data['lastname'],data['code'],data['phonenumber'],data['email'],data['password'],data['key'])
            return "User Details Inserted"
        else:'''