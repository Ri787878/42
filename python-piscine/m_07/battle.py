import ex0


def test_factory_creature_creation(factory: ex0.CreatureFactory) -> None:
    base_creature = factory.create_base()

    # Base creature
    print("Testing factory")
    print(base_creature.describe())
    print(base_creature.attack())

    # Evolved creature
    evolved_creature = factory.create_evolved()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}\n")


def test_factory_combat(factory1: ex0.CreatureFactory,
                        factory2: ex0.CreatureFactory) -> None:
    creature_1 = factory1.create_base()
    creature_2 = factory2.create_base()

    print("Testing battle")
    print(f"{creature_1.describe()}")
    print(f" vs.\n{creature_2.describe()}\n fight!")
    print(f"{creature_1.attack()}")
    print(f"{creature_2.attack()}")


def test_m7_ex0() -> None:
    Flame_factory: ex0.CreatureFactory = ex0.FlameFactory()
    Aqua_factory: ex0.CreatureFactory = ex0.AquaFactory()

    test_factory_creature_creation(Flame_factory)
    test_factory_creature_creation(Aqua_factory)

    test_factory_combat(Flame_factory, Aqua_factory)


if __name__ == "__main__":
    test_m7_ex0()
