from flask import Flask
from threading import Thread
from aria2p import API as ariaAPI, Client as ariaClient

app = Flask('')
aria2 = ariaAPI(ariaClient(host="http://localhost", port=6800, secret=""))

@app.route('/')
def home():
    return "Program is online/active, all thanks to UpTimeRobot!"

def run():
    app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
    t = Thread(target = run)
    t.start()