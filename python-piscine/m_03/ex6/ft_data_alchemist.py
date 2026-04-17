import random


def generate_int_list(size: int, min_value: int, max_value: int) -> list[int]:
    return [random.randint(min_value, max_value) for _ in range(size)]


def generate_scores_dict(plrs_list: list, min_v: int, max_v: int) -> dict:
    new_dict: dict = {}
    scores_list: list = generate_int_list(len(plrs_list), min_v, max_v)
    for i in range(min(len(plrs_list), len(scores_list))):
        new_dict[plrs_list[i]] = scores_list[i]
    return new_dict


def test_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")
    players_list: list = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam']
    capitalized_players_list: list = [
        name.capitalize() for name in players_list
    ]
    capitalized_only_players_list: list = [
        name for name in players_list if name[0].isupper()
    ]

    print(f"Initial list of players: {players_list}")
    print(
        f"New list with all names capitalized: {capitalized_players_list}"
    )
    print(
        "New list of capitalized names only: "
        f"{capitalized_only_players_list}\n"
    )

    plrs_scores: dict[str, int] = generate_scores_dict(
        players_list, 0, 1000)
    print(f"Score dict: {plrs_scores}")

    average: float = round(sum(plrs_scores.values()) / len(plrs_scores), 1)
    print(f"Score average is {average}")

    higher_plrs_scores: dict[str, int] = generate_scores_dict(
        players_list, round(average), 1000)
    print(f"High scores: {higher_plrs_scores}")


if __name__ == "__main__":
    test_data_alchemist()
