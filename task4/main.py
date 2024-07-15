
def parse_input(user_input):
    """Function parses input."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts: dict):
    """Function create new contact."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict):
    """Function changes existing contact."""
    res = ''
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        res = "Contact updated."
    else:
        res = f"Error: There is no contact like {name}"
    return res

def show_contacts(contacts):
    """Function returns all contacts."""
    if len(contacts) == 0:
        return "Contact list is empty. Use add/change/all <name> <phone>."
    return contacts

def main():
    """Start program."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command not in ["close", "exit", "all"] and (len(args) < 2 or len(args) > 2):
            print('Invalid count of arguments. It must be 2 arguments.\n \
Example:\n \
    add John 45897742')
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_contacts(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command. Use add/change/all <name> <phone>.")

if __name__ == "__main__":
    main()
