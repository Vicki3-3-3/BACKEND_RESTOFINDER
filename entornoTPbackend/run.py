from flask import Flask
from app.database import init_app
from app.views import *

app = Flask(__name__)
app.route('/', methods=['GET'])(index)
init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

