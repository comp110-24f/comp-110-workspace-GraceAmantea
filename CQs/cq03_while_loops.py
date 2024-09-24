__author__: str = "730655946"

"""First Exercise Using While Loops!"""


def num_instances(phrase: str, search_char: str) -> str:
    """How many times a character occurrs in a string"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    return str(count)
