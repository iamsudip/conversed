from flask import Flask
import redis

from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

application = Flask(__name__)
POOL = redis.ConnectionPool(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD
    )

from views import *

# A neat hack to add custom functions to jinja
@application.template_filter('websites')
def websites(web_list):
    return [ t['url'] for t in web_list ]
    # return ", ".join([ t['url'] for t in web_list ])

@application.template_filter('need_four_workplaces')
def need_four_workplaces(workplaces_list):
    return workplaces_list[:4]

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=8888)
    