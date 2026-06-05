def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return dict({"max_power": max(mages, key=lambda a: a["power"]),
                 "min_power": min(mages, key=lambda a: a["power"]),
                 "avg_power": float(sum(map(lambda a: a["power"], mages))
                                    / len(mages))})


if __name__ == "__main__":
    artifacts: list[dict] = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"}]

    spells: list[str] = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    s_artifacts: list[dict] = artifact_sorter(artifacts)
    print(f"{s_artifacts[0]['name']} ({s_artifacts[0]['power']} power)"
          f" comes before {s_artifacts[1]['name']} "
          f"({s_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed_spells: list[str] = spell_transformer(spells)
    for spell in transformed_spells:
        print(f"{spell} ", end="")
    print()
    pass
