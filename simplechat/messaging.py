# from bson.objectid import ObjectId
from pymongo.collection import Collection
import datetime
from simplechat import app, mongo


class Message(object):
    messages: Collection = mongo.db.messages

    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.datetime = datetime.datetime.now()
        self._id = None
        self.save()

    def save(self):
        if self._id:
            self.messages.update_one({"_id": self._id},
                                     {
                                         "name": self.name,
                                         "text": self.text,
                                         "datetime": self.datetime
                                     })
        else:
            self._id = self.messages.insert_one({
                "name": self.name,
                "text": self.text,
                "datetime": self.datetime
            }).inserted_id

    @classmethod
    def get_messages(cls):
        messages = [{"name": m["name"], "text": m["text"], "datetime": m["datetime"].isoformat()}
                    for m in cls.messages.find()]
        return messages

    @classmethod
    def send_message(cls, name, text):
        cls(name, text)
