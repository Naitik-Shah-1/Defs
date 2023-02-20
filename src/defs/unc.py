from typing import Callable, NoReturn

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def prompt_autocomplete(
    what_to_ask: str,
    word_list: list[str],
    ignore_case: bool = True,
    match_middle: bool = True,
    confirm_input: bool = False,
) -> str:
    """
    It takes a string to ask the user,
    a list of words to autocomplete from,
    and a few optional parameters to control the behavior of the autocompletion

    Parameters
    ----------
    what_to_ask : str
        str
    word_list : list[str]
        list[str]
    ignore_case : bool, optional
        bool = True
    match_middle : bool, optional
        bool = True
    confirm_input : bool, optional
        bool = False,

    Returns
    -------
        A string

    """

    completer_ = WordCompleter(
        word_list, match_middle=match_middle, ignore_case=ignore_case
    )
    if confirm_input:
        while True:
            user_input: str = prompt(message=what_to_ask, completer=completer_)
            confirmation: str = input(
                "Confirm the input by entering 'y'.\nIf want to edit enter anything except 'y':"
            )
            if confirmation.lower() == "y":
                return user_input
            prompt_autocomplete(what_to_ask, word_list + [user_input])
    else:
        return prompt(message=what_to_ask, completer=completer_)


def chk_res_words(
    word_to_chk: str,
    res_words_func: dict[str, Callable[..., None | NoReturn]],
) -> None:
    """
    If the word to check is a key in the dictionary of reserved words,
    then call the function associated with that key

    Parameters
    ----------
    word_to_chk : str
        str
    res_words_func : dict[str, Callable[..., None | NoReturn]]
        A dictionary of reserved words and their corresponding functions.

    """

    val = res_words_func.get(word_to_chk)
    if callable(val):
        val()
