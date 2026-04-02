import sys


class InvalidInputError(Exception):
    def __init__(self):
        message = ("No scores provided. "
                   "Usage: python3 "
                   "ft_score_analytics.py <score1> <score2> ...\n")
        super().__init__(message)


class InputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def get_scores(argv_list: list) -> None:
    for argument in sys.argv[1:]:
        argv_list.append(argument)


def get_total_score(scores_list: list) -> int:
    total: int = 0

    for score in scores_list:
        total += score

    return total


def get_avg_score(scores_list: list, player_count: int) -> float:
    sum: int = get_total_score(scores_list)
    result: float = sum / player_count

    return result


def get_score_range(scores_list: list) -> int:
    max_score = max(scores_list)
    min_score = min(scores_list)
    range: int = max_score - min_score

    return range


def test_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    argv_list: list = []
    scores_list: list = []
    player_count: int = 0

    get_scores(argv_list)
    player_count = len(argv_list)

    try:
        if player_count == 0:
            raise InvalidInputError()
        for score in argv_list:
            try:
                number: int = int(score)
            except ValueError:
                raise InputError(f"Invalid parameter: {score}")
            scores_list.append(number)

    except InvalidInputError as e:
        print(f"{e}")

    except InputError as e:
        print(f"{e}")

    else:
        print(f"Scores processed: {scores_list}")
        print(f"Total players: {player_count}")
        print(f"Total score: {sum(scores_list)}")
        print(
            f"Average score: "f"{get_avg_score(scores_list, player_count)}")
        print(f"High score: {max(scores_list)}")
        print(f"Low score: {min(scores_list)}")
        print(f"Score range: {get_score_range(scores_list)}\n")


if __name__ == "__main__":
    test_score_analytics()
