from flask import Flask

application = Flask(__name__)

from views import *

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=8888)