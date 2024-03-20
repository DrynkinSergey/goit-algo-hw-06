from collections import UserDict


def command_parser(input_str: str):
    """Parse command and attributes from user input

    Args:
        input_str (str): All string what user input

    Returns:
        command, *args: command - main operation, args - list of attributes for functions like [name, phone, new_phone]
    """
    try:
        command, *args = input_str.lower().split()
        return command, *args
    except (TypeError, ValueError):
        print('Command is empty string...Try again!')


def greetings():
    return "Welcome to CLI assistant 🔥"


def help_api():
    return ("Available commands: \n"
            "- add name number\n"
            "- update name old_number new_number\n"
            "- delete name\n"
            "- all (saw all contacts)\n")


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'{self.value}'


class Name(Field):
    ...


class Phone(Field):
    ...


class Record:
    """Record - class for new user, where we take all info: name and phones

    Main methods:

    phone_is_exist : Find exist phone in record
    edit_phone : Edit one of the phone in phones
    add_phone : Add phone to phones list

    """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    @staticmethod
    def phone_is_exist(data, phone):
        for p in data:
            if p.value == phone:
                return True

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                print(f'Phone {old_phone} edited to {new_phone}')
                break
        else:
            print(f'Phone {old_phone} is not exist!')

    def add_phone(self, phone):
        if self.phone_is_exist(self.phones, phone):
            return print('This number already exist')

        self.phones.append(Phone(phone))

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """AddressBook - class where we hold info about all users.

    Main methods:

    add_record: Add new record to book
    find_record: Find the record inside book
    show: Show all data from the book
    remove: Remove record from book


    Args:
        UserDict (dict): OptimizedDict from collections for holding data inside class
    """

    def add_record(self, record):
        self.data[record.name] = record

    def find_record(self, target):
        for i in self.data.values():
            if i.name.value.lower() == target.lower():
                return i

    def show(self):
        if len(self.data) == 0:
            print('No data exist!')
        for record in self.data.values():
            print(record)

    def remove(self, target):
        for record in list(self.data.keys()):
            if record.value == target:
                del self.data[record]
                print(f'User {target} has been deleted!')
