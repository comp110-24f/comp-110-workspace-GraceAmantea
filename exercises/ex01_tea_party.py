"""Planning A Cozy Tea Party"""

__author__: str = "730655946"


def main_planner(guests: int) -> None:
    """Calculating costs per person"""
    print("a cozy tea party for " + str(guests) + " people")
    print("tea bags: " + str(tea_bags(people=guests)))
    print("treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # number of people/tea/treats should be specified when calling.

    return None


def tea_bags(people: int) -> int:
    """Number of people attending"""
    return people * 2
    # do not put tea_bags in the return function, or it will not generate an RV.


def treats(people: int) -> int:
    """Number of treats per person"""
    return int(
        tea_bags(people=people) * 1.5
    )  # you have to put tea_bags here because treats is tied to the tea bags function.


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea and treats"""
    return (
        tea_count * 0.50 + treat_count * 0.75
    )  # these are independent of tea_bags and treats.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
