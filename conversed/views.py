from flask import Flask, render_template, request
import json

import requests

from main import application
from utils import validate


@application.route('/')
def index():
    return render_template("index.html")

@application.route('/', methods=['POST'])
def profile(emailid=None):
    emailid = request.form['emailid']
    emailstatus = validate(emailid)
    if emailstatus:
        return render_template("sorry.html") # enable js validation currently only server side validation is done
    else:
        response = requests.get("https://vibeapp.co/api/v1/initial_data/?api_key=b2acf1eadef73f4aeda890e0571f3e06&email="+emailid)
        if response.status_code == 200:
            data = json.loads(response.text)
            if data.get('success'):
                return render_template("data.html", user=data)
            else:
                return render_template("sorry.html")
        else:
            return render_template("sorry.html")
        # Comment below line for development
        # data = {u'organizations': [{u'title': u'CPython Core Developer', u'name': u'Python Software Foundation', u'timespan': u'2014-04 - '}, {u'title': u'Free Software lover', u'name': u'Red Hat', u'timespan': u''}, {u'title': None, u'name': u'DSL Software', u'timespan': u''}, {u'title': None, u'name': u'Comat', u'timespan': u''}], u'name': u'Kushal Das', u'success': True, u'bio': u'Visit <a href="http://kushaldas.in" rel="nofollow" target="_blank">http://kushaldas.in</a><br />', u'gender': u'Male', u'topics': [u'Python', u'Photographers', u'Photography', u'Open Source', u'India'], u'domain_title': None, u'websites': [{u'url': u'http://kushaldas.in'}], u'email': u'kushaldas@gmail.com', u'profile_picture': u'https://d2ojpxxtu63wzl.cloudfront.net/static/f11c2845681df0e41bf6d26c11ed3ed3_c891e174ae8c7234c713f1b9f1b42a3585abd0a6e566164b4f7d70939d1fd82d', u'location': u'Bangalore', u'domain_desc': None, u'position': u'Comat', u'likelihood': 0.91, u'social_profiles': [{u'username': u'kushaldas', u'typeId': u'klout', u'url': u'http://klout.com/kushaldas', u'typeName': u'Klout', u'type': u'klout', u'id': u'38280601597589379'}, {u'bio': u'Community Gardener at Eucalyptus Systems Inc.', u'typeId': u'linkedin', u'url': u'https://www.linkedin.com/pub/kushal-das/8/55b/5a6', u'typeName': u'LinkedIn', u'type': u'linkedin', u'id': u'kushal-das/8/55b/5a6'}, {u'username': u'kushaldas', u'bio': u'Photographer, FOSS developer, plays with Python. Interested in education. Fellow at Python Software Foundation. Community Gardener in Eucalyptus Systems.', u'typeId': u'twitter', u'url': u'https://twitter.com/kushaldas', u'typeName': u'Twitter', u'followers': 1072, u'following': 1368, u'type': u'twitter', u'id': u'14452322'}, {u'bio': u'Visit <a href="http://kushaldas.in" rel="nofollow" target="_blank">http://kushaldas.in</a><br />', u'typeId': u'googleplus', u'url': u'https://plus.google.com/u/0/114013331910661220533', u'typeName': u'GooglePlus', u'type': u'googleplus', u'id': u'114013331910661220533'}, {u'url': u'https://youtube.com/user/babaidas', u'typeId': u'youtube', u'username': u'babaidas', u'type': u'youtube', u'typeName': u'Youtube'}, {u'username': u'liveshowsphotos', u'typeId': u'facebook', u'url': u'https://www.facebook.com/liveshowsphotos', u'typeName': u'Facebook', u'type': u'facebook', u'id': u'100000186712778'}, {u'username': u'kushaldas', u'typeId': u'flickr', u'url': u'https://www.flickr.com/people/kushaldas', u'typeName': u'Flickr', u'type': u'flickr', u'id': u'88746839@n00'}, {u'username': u'kushaldas', u'typeId': u'gravatar', u'url': u'https://gravatar.com/kushaldas', u'typeName': u'Gravatar', u'type': u'gravatar', u'id': u'849903'}, {u'url': u'https://github.com/kushaldas', u'typeId': u'github', u'username': u'kushaldas', u'type': u'github', u'typeName': u'Github'}], u'extra_pictures': [u'https://d2ojpxxtu63wzl.cloudfront.net/static/2aaa62a81e4ad143fe6c0867c2b113f7_2a44f109d6ca0c0c085fed9a4d817a09a9795ec7d867497c7c663724103fe83d', u'https://d2ojpxxtu63wzl.cloudfront.net/static/486de76262f6154de0202e90e30186f9_66b87d65f1c853c715c7b74bf96a58e088f4e3e5c9c3cefdfb6ca27535e24f23', u'https://d2ojpxxtu63wzl.cloudfront.net/static/b95a8cb342d1be350b8bae2d294c198c_66298f3f2b3db48b17982cc816518f538605358a70130aa6ce182580d6136d62', u'https://d2ojpxxtu63wzl.cloudfront.net/static/aa7ced9f2302f2b1d10b6923fae54b35_ab41cb548206f906b075282c900d85017376e35cdd6b1851ed9ad6f24b3d4dcf', u'https://d2ojpxxtu63wzl.cloudfront.net/static/175835a3ffd9342b3141ec8fda2a88ba_3f5b87ed82b89fba4510f57232db06204d392aa75122474ea05f4b12e2878d2b', u'https://d2ojpxxtu63wzl.cloudfront.net/static/e95253a58ee099a2148f032b86126f86_056da93b800c26b5feb838a1efc302eacdc58a539bb6e821b047d4206f41a091', u'https://d2ojpxxtu63wzl.cloudfront.net/static/5ab744a814c5ff502b9e002f500f6640_ee2bc63b8fe28439b4d45523e0d6ca08040420dfb9de8f8eea24f7ec7378a6a1']}
        # return render_template("data.html", user=data)

@application.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404