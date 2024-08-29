"""Challenge Question 00"""

__author__ = "730655946"


def mimic(message: str) -> str:
    """repeat input"""
    return message


def main() -> None:
    """Pull together functions"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
