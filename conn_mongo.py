from mongoengine import Document, StringField, connect


connect(db="AddressBook",
        host="mongodb+srv://user_web7:1234567890@cluster0.hxujwpa.mongodb.net/?retryWrites=true&w=majority")


class User(Document):
    login = StringField(max_length=120, unique=True)
    last_name = StringField(max_length=120)
    phone = StringField(max_length=20)
    email = StringField(max_length=50)
    address = StringField(max_length=120)
    birthday = StringField(max_length=12)
    black_list = StringField(max_length=12)


if __name__ == '__main__':

    one = User(login="Ivan2").save()
