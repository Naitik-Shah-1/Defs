from .formatting import remove_xtra_spaces_str


def natural_num(what_to_ask: str) -> int:
    """
    It asks the user for a natural number,
    and if the user doesn't give a natural number,
    it asks again

        Parameters
        ----------
        what_to_ask : str
            str

        Returns
        -------
            A natural number.

    """

    try:
        user_input = int(remove_xtra_spaces_str(input(what_to_ask)))
        if user_input >= 1:
            return user_input
        return natural_num(what_to_ask)
    except ValueError:
        print("Input is Not a Valid Natural Number.")
        return natural_num(what_to_ask)


def whole_num(what_to_ask: str) -> int:
    """
    It asks the user for a whole number,
    and if the user doesn't enter a whole number,
    it asks the user again

    Parameters
    ----------
    what_to_ask : str
        str

    Returns
    -------
        A whole number.

    """

    try:
        user_input = int(remove_xtra_spaces_str(input(what_to_ask)))
        if user_input >= 0:
            return user_input
        return whole_num(what_to_ask)
    except ValueError:
        print("Input is Not a Valid Whole Number.")
        return whole_num(what_to_ask)


def integer(what_to_ask: str) -> int:
    """
    It asks the user for an integer,
    and if the user doesn't enter an integer,
    it asks the user again

    Parameters
    ----------
    what_to_ask : str
        str

    Returns
    -------
        the integer value of the input.

    """

    try:
        return int(remove_xtra_spaces_str(input(what_to_ask)))
    except ValueError:
        print("Input is Not a Valid Integer.")
        return integer(what_to_ask)


def rational_num(what_to_ask: str) -> float:
    """
    It asks the user for a floating point number,
    and if the user doesn't enter a floating point number,
    it asks the user again

    Parameters
    ----------
    what_to_ask : str
        str

    Returns
    -------
        A float.

    """

    try:
        return float(remove_xtra_spaces_str(input(what_to_ask)))
    except ValueError:
        print("Input is Not a Valid Floating Point Number.")
        return rational_num(what_to_ask)


def whole_num_with_decimal(what_to_ask: str) -> float:
    """
    It asks the user for a whole number with decimal,
    and if the user inputs a whole number with decimal,
    it returns it,
    otherwise it asks the user for a whole number with decimal again

    Parameters
    ----------
    what_to_ask : str
        str

    Returns
    -------
        A float

    """

    try:
        user_input = float(remove_xtra_spaces_str(input(what_to_ask)))
        if user_input >= 0:
            return user_input
        return whole_num_with_decimal(what_to_ask)
    except ValueError:
        print("Input is Not a Valid Whole Number with Decimal.")
        return whole_num_with_decimal(what_to_ask)
