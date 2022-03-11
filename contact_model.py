from flask_mongoengine import mongoengine


class Contact(mongoengine.Document):
    Name = mongoengine.StringField(max_length=50, required=True)
    PhoneNumber = mongoengine.StringField(max_length=10, required=True)
    Address = mongoengine.StringField(max_length=10)
    Email = mongoengine.EmailField(max_length=50)

