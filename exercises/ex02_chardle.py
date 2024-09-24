"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730655946"


def input_word() -> str:
    "enter a 5-character word"
    guess_word: str = str(
        input("Enter a 5-character word: ")
    )  # make sure to put the string being input.
    while (
        len(guess_word) != 5
    ):  # type static issue, I had an infinite loop and put guess_word(len).
        print("Error: Word must contain 5 characters.")
    else:
        return guess_word
    exit()


def input_letter() -> str:
    "enter a single character"
    guess_letter: str = str(
        input("Enter a single character: ")
    )  # see the remarks on line 8, same error made here.
    while len(guess_letter) != 1:  # see remarks on line nine, same error made here.
        print("Error: Character must be a single character.")
    else:
        return guess_letter
    exit()


def contains_char(input_word: str, input_letter: str) -> None:
    count: int = 0  # i can define the count variable here instead of using index.
    while len(input_word) == 5:
        if (
            input_word[count] == input_letter
        ):  # link count to the input letters in the input word.
            print(
                "search for " + input_letter + " in " + input_word
            )  # make sure there are spaces before and/or after quotation marks.
            count = (
                count + 1
            )  # make sure indent lines up with print here since it falls under this.
        if input_word[count] == input_letter:
            print(str(count) + " instances of " + input_letter + " found")
        else:
            print("No instances of " + input_letter + " found")


def main() -> None:
    contains_char(
        input_word=str(), input_letter=str()
    )  # make sure the arguments here agree with prior parameters.


if __name__ == "__main__":
    main()
