from flask import Flask, render_template, request
import json

import requests

from main import application
from utils import validate


@application.route('/')
def home():
    return render_template("home.html")

@application.route('/', methods=['POST'])
def profile():
    emailid = request.form['emailid']
    emailstatus = validate(emailid)
    if emailstatus:
        return render_template("sorry.html") # enable js validation currently only server side validation is done
    else:
        try: # https://vibeapp.co/api/v1/initial_data/?api_key=b2acf1eadef73f4aeda890e0571f3e06&email=
            response = requests.get("https://vibeapp.co/api/v1/initial_data/?api_key=b2acf1eadef73f4aeda890e0571f3e06&email="+emailid)
            if response.status_code == 200:
                data = json.loads(response.text)
                if data.get('success'):
                    return render_template("data.html", user=data)
                else:
                    return render_template("sorry.html")
            else:
                return render_template("sorry.html")
        except requests.exceptions.ConnectionError:
            return render_template("sorry.html")
            
@application.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404