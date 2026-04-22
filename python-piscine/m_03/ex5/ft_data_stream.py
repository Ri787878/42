from typing import Generator
import random


# The 3 variable are:
# 1. return type of the generator,
# 2. what can be sent to the gen via .send() aka parameters
# 3. final return after completing the gen (so never because "While True")
def gen_event() -> Generator[tuple[str, str], None, None]:
    players_list: list = ["alice", "bob", "dylan", "charlie"]
    actions_list: list = [
        "run", "eat", "sleep", "grab", "move",
        "climb", "swim", "release", "use"]

    while True:
        name: str = random.choice(players_list)
        action: str = random.choice(actions_list)
        yield name, action


def consume_event(act_log: list[tuple[str, str]]) -> Generator[tuple[str, str],
                                                               None, None]:
    while len(act_log) > 0:
        log_index = random.randrange(len(act_log))
        yield act_log.pop(log_index)


def test_data_stream() -> None:
    g = gen_event()
    for i in range(1000):
        combo: tuple[str, str] = next(g)
        print(f"Event {i}: Player {combo[0]} did action {combo[1]}")

    actions_log: list = [next(g) for i in range(10)]
    print(f"Built list of 10 events: {actions_log}")

    for log in consume_event(actions_log):
        print(f"Got event from list: {log}")
        print(f"Remains in list: {actions_log}")


if __name__ == "__main__":
    test_data_stream()
