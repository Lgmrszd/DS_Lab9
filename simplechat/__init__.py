from flask import Flask, render_template
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

from simplechat import messaging
from simplechat import routes
