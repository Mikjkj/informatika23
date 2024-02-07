import random
import requests
from flask import Flask, render_template
count = 0
app = Flask(__name__)

@app.route("/")

def protocol():
    pozdravy = ["ŽĎÁREC PÁREC!","HELLo","[VLOZ POZDRAV] ","DOBRÝ DEN, VÍTEJTE NA TÉTO STRÁNCE"]
    pozdrav = random.choice(pozdravy)
    return render_template("hello.html", pozdrav = pozdrav)

@app.route("/add")
def add():
    count+=1