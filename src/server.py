from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return json.dumps

@app.route("/hello")
def hai():
    return json.dumps({"message":"Hai!"})
