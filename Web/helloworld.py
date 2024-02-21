import random
import requests
from flask import Flask, render_template, redirect, url_for
count = 0
power = 1
app = Flask(__name__)

@app.route("/")
def protocol():
    global count 
    pozdravy = ["ŽĎÁREC PÁREC!","HELLo","[VLOZ POZDRAV] ","DOBRÝ DEN, VÍTEJTE NA TÉTO STRÁNCE"]
    pozdrav = random.choice(pozdravy)
    return render_template("hello.html",count = count, pozdrav = pozdrav)

@app.route("/add", methods = ["POST"])
def add():
    global count, power
    count = count + power
    return redirect(url_for('protocol'))
@app.route("/buy", methods = ["POST"])
def buy():
    global count, power
    if count >= 10:
        power += 1
        count -= 10
    return redirect(url_for('protocol'))