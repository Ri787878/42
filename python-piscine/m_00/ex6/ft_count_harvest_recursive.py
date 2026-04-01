def recursive_helper(days: int, i: int) -> None:
    print(f"Day {i}")
    if i == days:
        print("Harvest time!")
    else:
        recursive_helper(days, i + 1)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive_helper(days, 1)
