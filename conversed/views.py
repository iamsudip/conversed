from flask import Flask, render_template, request

from main import application
from utils import validate
import requests

@application.route('/')
def index():
    return render_template("index.html")

@application.route('/', methods=['POST'])
def profile(emailid=None):
    emailid = request.form['emailid']
    emailstatus = validate(emailid)
    if emailstatus:
        return render_template("404.html")
    else:
        data = requests.get("https://vibeapp.co/api/v1/initial_data/?api_key=b2acf1eadef73f4aeda890e0571f3e06&email="+emailid)
        return render_template("data.html")