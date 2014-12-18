from flask import Flask

application = Flask(__name__)

from views import *

# A neat hack to add custom functions to jinja
def websites(web_list):
    return ", ".join([ t['url'] for t in web_list ])

def need_four_workplaces(workplaces_list):
    return workplaces_list[:4]

if __name__ == '__main__':
    application.jinja_env.filters['websites'] = websites # A neat hack to add custom functions to jinja
    application.jinja_env.filters['need_four_workplaces'] = need_four_workplaces
    application.run(debug=True, host="0.0.0.0", port=8888)