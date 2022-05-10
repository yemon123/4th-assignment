from django.shortcuts import render
from django.http import HttpResponse
import pymongo
import random

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def loginchecker(request):
    username = request.POST['username']
    upassword = request.POST['password']
    try:
        for i in range(0, len(credentials_list)):
            if credentials_list[i]["username"] == username:
                if credentials_list[i]["password"] == upassword:
                    x = credentials_list[i]["money"]
                    return HttpResponse(f"Login Successful.Money: {x}.")
                else:
                    return render(request,'login.html',{'data':"Username or password is wrong." })
            else:
                pass
    except Exception as error:
        return render(request,'login.html',{'data':"error" })


def username_checker(z):
    try:
        for i in range(0, len(credentials_list)):
            if credentials_list[i]["username"] == z:
                print("The username is already existed.")
                return False
            else:
                return True
    except Exception as error:
        print(error)
        return False


def add(request):
    try:        
        username = request.POST['username']
        upassword = request.POST['password']
        uconfirm_password = request.POST['confirm_password']
        umoney = request.POST['money']
        if username_checker(username) is True:   
            if uconfirm_password == upassword:
                id = random.randint(0,1000)
                data = {'_id':id, 'username':username, 'password':upassword, 'money':umoney}
                x = collection.insert_one(data)
                return HttpResponse('Registered Successfully!')
            else:               
                return render(request,'register.html',{'data':'Passwords are not the same.'})
        else:
            return render(request,'register.html',{'data':'Username is already in use.Try again.'})
    except Exception as error:
            return render(request,'register.html',{'data':error})

try:
    connection = pymongo.MongoClient('localhost',27017)
    database = connection['my_db']
    collection = database['my_collection']    
    print("Connection Success!")
    credentials_list: list = []
    id_user = None
    dbs = collection.find()
    for d in dbs:
        credentials_list.append(d)
    print(credentials_list)

except Exception as error:
    print(error)

