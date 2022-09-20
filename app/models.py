from mongoengine import Document, StringField


class Offer(Document):
    position = StringField()
    description = StringField()
    conditions = StringField()