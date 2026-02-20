# Design a Phone Class with methods to call_contact and take_picture, abtract away any internal
# processing details and focus on creating a user friendly interface


class Phone:
    @staticmethod
    def call_contact():
        print("Call Contact process")

    @staticmethod
    def take_picture():
        print("Picture capture in phone through camera")

phone = Phone()
phone.call_contact()
phone.take_picture()


