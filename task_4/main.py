"""Module for Task 4."""

import handler


def parse_input(user_input: str) -> tuple:
    command, *arguments = user_input.split()
    command = command.strip().lower()
    return command, *arguments


def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *arguments = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            print(handler.list_all_entries())

        elif command == "add":
            print(handler.add_entry(*arguments))

        elif command == "change":
            print(handler.update_entry(*arguments))

        elif command == "phone":
            print(handler.retrieve_phone_number(*arguments))

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print(
                "Invalid command. Usage: hello | all | add [name] [phone] | change [name] [phone] | phone [name] | exit | close")


if __name__ == "__main__":
    main()
