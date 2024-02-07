import random
import requests
from flask import Flask, render_template

app = Flask(__name__)
def protocol():
    app.render_template("hello.html")

