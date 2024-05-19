import re

phonebook = {}


class PhonebookError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def handle_input_error(error_message: str = "Invalid input."):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except PhonebookError as e:
                return e.message
            except(ValueError, IndexError):
                return error_message

        return wrapper

    return decorator


@handle_input_error(error_message="Invalid command. Usage: add [name] [phone number]")
def add_entry(*args) -> str:
    name, phone = args

    if name in phonebook:
        raise PhonebookError("Contact already exists.")
    phonebook[name] = normalize_phone_number(phone)
    return "Contact added."


@handle_input_error(error_message="Invalid command. Usage: change [name] [phone number]")
def update_entry(*args) -> str:
    name, phone = args

    if name not in phonebook:
        raise PhonebookError("No such contact.")

    phonebook[name] = normalize_phone_number(phone)
    return "Contact updated."


@handle_input_error(error_message="Invalid command. Usage: phone [name]")
def retrieve_phone_number(*args) -> str:
    (name,) = args

    if name not in phonebook:
        raise PhonebookError("No such contact.")

    return phonebook[name]


def list_all_entries() -> dict:
    return phonebook


def normalize_phone_number(phone_number: str, country_code: str = "38") -> str:
    pattern = r"[+\d]"
    normalized_number = "".join(re.findall(pattern, phone_number))

    if not normalized_number.startswith("+"):
        normalized_number = re.sub(fr"^({country_code})?", f"+{country_code}", normalized_number)

    if len(normalized_number) != 13:
        raise ValueError("Invalid phone number.")

    return normalized_number
