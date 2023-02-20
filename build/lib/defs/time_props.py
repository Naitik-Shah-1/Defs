from datetime import datetime


def time_stamp():
    """
    It takes the current date and time,
    formats it as a string,
    splits it into a list of strings,
    and then converts each string into an integer

    Returns
    -------
        A tuple of integers.

    """
    return tuple(
        int(obj) for obj in datetime.now().strftime("%Y-%m-%d-%H-%M").split("-")
    )


def greeting_word_human_time(current_hour: int):
    """
    It returns "Morning" if the current hour is less than 12,
    "Afternoon" if the current hour is less than or equal to 16,
    "Evening" if the current hour is less than or equal to 18,
    and "Night" otherwise

    Parameters
    ----------
    current_hour : int
        The current hour of the day.

    Returns
    -------
        A string

    """
    if current_hour < 12:
        return "Morning"
    if current_hour <= 16:
        return "Afternoon"
    if current_hour <= 18:
        return "Evening"
    return "Night"
