
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_mongoengine import MongoEngine
from contact_model import Contact


app = Flask(__name__)
api = Api(app)

# connecting with Database
app.config['MONGODB_SETTINGS'] = {"db": "contact_book", 'host': 'localhost', 'port': 27017}
db = MongoEngine(app)


class ContactBook(Resource):
    def get(self):
        data = Contact.objects()
        new_data = []
        for x in data:
            new_data.append({"Name": x["Name"], "PhoneNumber": x["PhoneNumber"], "Address": x["Address"], "Email": x["Email"]})
        return jsonify(new_data)

    def post(self):
        data = Contact(Name=request.form['Name'], PhoneNumber=request.form['PhoneNumber'], Address=request.form['Address'], Email=request.form['Email'])
        data.save()
        return jsonify(message='SuccessFully Added')


class ModifyContact(Resource):
    def get(self, name):
        data = Contact.objects(Name=name).first()
        result = {"Name": data.Name, "PhoneNumber": data.PhoneNumber, "Address": data.Address, "Email": data.Email}
        return jsonify(result)

    def patch(self, name):
        data = Contact.objects(Name=name).first()
        data.update(Name=name, PhoneNumber=request.form["PhoneNumber"])
        return jsonify(message="User ContactData Updated")

    def delete(self, name):
        data = Contact.objects(Name=name).first()
        data.delete()
        return jsonify(message="Deleted")

    def sort(self, name):
        data = Contact.objects(Name=name)
        data.find().sort("Name")


api.add_resource(ContactBook, '/get')
api.add_resource(ModifyContact, '/get/<name>')


if __name__ == "__main__":
    app.run(debug=True)
