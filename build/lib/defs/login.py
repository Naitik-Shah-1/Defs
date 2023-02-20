from .unc import prompt_autocomplete
from .time_props import time_stamp
from .formatting import remove_xtra_spaces_str, remove_xtra_spaces_list
from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from prompt_toolkit import prompt


def sign_up() -> dict[str, str]:
    """
    It asks for a name, date of birth, and gender, and returns a dictionary with those values

    Returns
    -------
        A dictionary with three keys and three values.

    """
    name: str = ask_full_name()
    dob: str = ask_dob(time_stamp()[0])
    gender: str = ask_gender()
    return {"Name": name, "Dob": dob, "Gender": gender}


def ask_full_name() -> str:
    """
    It asks for user's name and checks if it is valid or not

    Returns
    -------
        A string which is the username.

    """
    user_input = remove_xtra_spaces_str(
        input("Enter your name {Name FatherName Surname}: ")
    ).title()
    user_input_x_spaces = user_input.replace(" ", "")
    splitted_user_input = user_input.split()
    if len(splitted_user_input) != 3:
        print("Try: Enter name in format of {Your name, Your father's name, surname")
        return ask_full_name()
    for item in splitted_user_input:
        len_item = len(item)
        if 10 <= len_item or len_item <= 2:
            print(
                "Entered name too short. Try: Enter your father's name instead of his initial"
            )
            return ask_full_name()
    if not user_input_x_spaces.isalnum():
        print(
            "Entered name contains something which is neither a alphabet nor a number,"
            " probably punctuations."
        )
        return ask_full_name()
    if user_input_x_spaces.isnumeric():
        print("Entered name doesn't have any alphabets in it.")
        return ask_full_name()
    return user_input


def create_password() -> str:

    password = prompt(
        message="Create Password: ",
        is_password=True,
    )

    password_unique_letters: set[str] = set(password)

    if {"'", '"', " "}.isdisjoint(password_unique_letters) is False:
        print("Your Password contains inverted commas or spaces.")
        return create_password()

    if password.isidentifier():
        print("Your Password Contains identifiers")
        return create_password()

    if 16 < len(password) or 8 > len(password):
        print("Length must be between 7 & 17")
        return create_password()

    if len(password_unique_letters) < 4:
        print("Very Less Unique Characters Detected.")
        return create_password()

    if set(ascii_lowercase).isdisjoint(password_unique_letters):
        print("No lower Cased Characters Detected.")
        return create_password()

    if set(ascii_uppercase).isdisjoint(password_unique_letters):
        print("No UPPER Cased Characters Detected.")
        return create_password()

    if set(digits).isdisjoint(password_unique_letters):
        print("No Digits Detected.")
        return create_password()

    if set(punctuation).isdisjoint(password_unique_letters):
        print("No Symbols in Password.")
        return create_password()

    if password != prompt("Retype **your password to confirm it: ", is_password=True):
        return create_password()

    return password


def ask_dob(year: int) -> str:
    auto_complete_word_list: list[str] = [str(day_obj) for day_obj in range(1, 32)] + [
        str(year_obj) for year_obj in range(year - 90, year - 4)
    ]
    user_input: list[str] = remove_xtra_spaces_list(
        prompt_autocomplete(
            what_to_ask="Enter your Birthdate {dd/mm/yyyy} (use space to split them): ",
            word_list=auto_complete_word_list,
            match_middle=True,
        )
    )
    user_input = [item.removeprefix("0") for item in user_input]
    if (
        len(user_input) != 3
        or user_input[0] not in auto_complete_word_list[0:32]
        or user_input[1] not in auto_complete_word_list[0:13]
        or user_input[2] not in auto_complete_word_list[32:]
    ):
        print(
            "Invalid Input Given."
        )
        return ask_dob(year)
    return " ".join(user_input)


def ask_gender() -> str:
    auto_complete_word_list: list[str] = ["Male", "Female", "Transgender", "Others"]
    user_input: str = remove_xtra_spaces_str(
        prompt_autocomplete(
            what_to_ask="Enter your Gender: ",
            word_list=auto_complete_word_list,
            match_middle=True,
        )
    ).title()
    if len(user_input.split()) != 1 or user_input not in auto_complete_word_list:
        print("Invalid Input Given")
        return ask_gender()
    return user_input
