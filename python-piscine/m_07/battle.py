import ex0


def creature_creation(factory: ex0.CreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()

    print("Testing factory")
    print(base_creature.describe())
    print(base_creature.attack())

    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}\n")


def creature_combact(factory1: ex0.CreatureFactory,
                     factory2: ex0.CreatureFactory) -> None:
    flame_creature = factory1.create_base()
    aqua_creature = factory2.create_base()

    print("Testing battle")
    print(f"{flame_creature.describe()}\n")
    print(f" vs.\n{aqua_creature.describe()}\n fight!")
    print(f"{flame_creature.attack()}")
    print(f"{aqua_creature.attack()}")


def test_m7_ex0() -> None:
    Flame_factory: ex0.CreatureFactory = ex0.FlameFactory()
    Aqua_factory: ex0.CreatureFactory = ex0.AquaFactory()

    creature_creation(Flame_factory)
    creature_creation(Aqua_factory)

    creature_combact(Flame_factory, Aqua_factory)


if __name__ == "__main__":
    test_m7_ex0()
