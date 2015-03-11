from flask import Flask

app = Flask(__name__)

from investa_gator import views
