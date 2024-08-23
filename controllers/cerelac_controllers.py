from flask import request
import time
from data.cerelac_data import users,is_available,entry_pass,purple,black

def home():
    return {"from_backend": 'wewe'}
def get_health():
    return {"purple": purple["hp"],"black": black["hp"] } 

def checkAvailable():
    if(is_available == True):
        return {"available": True}
    else:
        return {"available": False}

# Authenticate ----------------------------------------------------------
def authenticate():
    request_data = request.get_json()
    for i in range(0,len(users)):
        if request_data["username"] == users[i]["username"]:
            if request_data["password"] == users[i]["password"]:
                return {"auth_state": "yes"}
    return {"auth_state": "no"}


def tmpauth():
    request_data = request.get_json()
    if request_data["password"] == entry_pass:
        return {"auth_state": "yes"}
    else:
        return {"auth_state": "no"}
def alive_state():
    curr = time.time()
    if curr - purple["is_alive_timer"] > 6:
        purple["is_alive"] = False
    else:
        purple["is_alive"] = True
        
    if curr - black["is_alive_timer"] > 6:
        black["is_alive"] = False
    else:
        black["is_alive"] = True
        
    return {"purple": purple["is_alive"], "black": black["is_alive"]}