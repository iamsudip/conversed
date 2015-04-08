from ast import literal_eval
import json

from flask import Flask, render_template, request
import requests
import redis

from main import application, POOL
from utils import cleanup, validate
from config import API, API_KEY, LOCAL_DEV


@application.route('/')
def home():
    return render_template("home.html")


@application.route('/', methods=['POST'])
def profile():
    emailid = request.form['emailid']
    emailstatus = validate(emailid)
    if emailstatus:
        return render_template("sorry.html")
    else:
        try:
            redis_server = redis.Redis(connection_pool=POOL)
            if not (redis_server.exists(emailid) or LOCAL_DEV):
                payload = {
                    'api_key': API_KEY,
                    'email': emailid,
                    'force': 1
                }
                response = requests.get(API, params=payload)
                if response.status_code == 200:
                    data = json.loads(response.text)
                    if data.get('success'):
                        cleaned_data = cleanup(data)
                        redis_server.set(emailid, json.dumps(cleaned_data))
                        redis_server.bgsave()
                else:
                    return render_template("sorry.html")
            data = literal_eval(redis_server.get(emailid))
            if data.get('success', False):
                return render_template("data.html", user=data)
            else:
                return render_template("sorry.html")
        except (requests.exceptions.ConnectionError, TypeError):
            return render_template("sorry.html")


@application.route('/status/')
def api_status():
    return render_template("home.html")


@application.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404