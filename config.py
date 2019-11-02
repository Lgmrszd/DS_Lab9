import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    MONGO_URI = os.environ.get('MONGO_URI') or "mongodb://127.0.0.1:27017/messages"
