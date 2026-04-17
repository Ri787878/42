import random


def get_random_achivements_index() -> list:
    random_numbers: list = []
    nbr_of_achivements: int = random.randint(3, 13)

    while len(random_numbers) < nbr_of_achivements:
        num: int = random.randint(0, 12)
        if num not in random_numbers:
            random_numbers.append(num)

    return random_numbers


def gen_player_achievements(achievements_list: set) -> set:
    player_list: set = set()
    achivements_index = get_random_achivements_index()

    for i in achivements_index:
        player_list.add(list(achievements_list)[i])

    return player_list


def test_achievement_tracker_system() -> None:
    print("=== Achievement Tracker System ===\n")
    achievs_list: set = set([
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'])
    hidden_achievements: set = set(["Hidden Path Finder"])

    alice_achv: set = set(gen_player_achievements(achievs_list))
    bob_achv: set = gen_player_achievements(achievs_list)
    charlie_achv: set = gen_player_achievements(achievs_list)
    dylan_achv: set = gen_player_achievements(achievs_list)

    print(f"Player Alice: {alice_achv}")
    print(f"Player Bob: {bob_achv}")
    print(f"Player Charlie: {charlie_achv}")
    print(f"Player Dylan: {dylan_achv}")

    print(f"\nAll distinct achievements: {achievs_list}")

    print(
        f"\nCommon achievements: "
        f"{alice_achv.intersection(bob_achv, charlie_achv, dylan_achv)}")

    print(
        f"\nOnly Alice has: "
        f"{alice_achv.difference(bob_achv, charlie_achv, dylan_achv)}")
    print(
        f"Only Bob has: "
        f"{bob_achv.difference(alice_achv, charlie_achv, dylan_achv)}")
    print(
        f"Only Charlie has: "
        f"{charlie_achv.difference(alice_achv, bob_achv, dylan_achv)}")
    print(
        f"Only Dylan has: "
        f"{dylan_achv.difference(alice_achv, bob_achv, charlie_achv)}")

    print(
        f"\nAlice is missing: "
        f"{hidden_achievements.union(achievs_list.difference(alice_achv))}")
    print(
        f"Bob is missing: "
        f"{hidden_achievements.union(achievs_list.difference(bob_achv))}")
    print(
        f"Charlie is missing: "
        f"{hidden_achievements.union(achievs_list.difference(charlie_achv))}")
    print(
        f"Dylan is missing: "
        f"{hidden_achievements.union(achievs_list.difference(dylan_achv))}")


if __name__ == "__main__":
    test_achievement_tracker_system()
