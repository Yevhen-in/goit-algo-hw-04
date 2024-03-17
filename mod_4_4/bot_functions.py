import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        name = new_name(name)
    contacts[name] = phone
    return "Contact added."

def new_name(name):
    has_a_number = re.search("\d+", name)
    if has_a_number:
        number = int(has_a_number.group()) + 1
        name = re.sub("\d+", str(number), name)
    else:
        name = name + "_1" 
    return name

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"{name} is not in the contact list."

def phone_from_contacts(args, contacts):
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        return f"{name} has this phone number: {phone}."
    else:
        return f"{name} is not in the contact list."