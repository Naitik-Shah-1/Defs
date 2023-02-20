from re import split


def remove_xtra_spaces_list(str_to_check: str) -> list[str]:
    """
    It takes a string,
    removes any leading or trailing spaces,
    then splits the string into a list of strings,
    using a regular expression to match one or more spaces

    Parameters
    ----------
    str_to_check : str
        The string to check for extra spaces.

    Returns
    -------
        A list of strings

    """
    return split(" +", str_to_check.strip(" "))


def remove_xtra_spaces_str(str_to_check: str) -> str:
    """
    It takes a string, splits it into a list,
    removes the extra spaces,
    and then joins the list back into a string

    Parameters
    ----------
    str_to_check : str
        The string to check for extra spaces.

    Returns
    -------
        A string with no extra spaces.

    """
    return " ".join(remove_xtra_spaces_list(str_to_check))
