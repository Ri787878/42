import ex1


def test_healing_factory(factory: ex1.HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")

    print(" base:")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.heal("itself"))

    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.heal("itself and others"))


def test_transform_factory(factory: ex1.TransformCreatureFactory) -> None:
    print("\nTesting Creature with transform capability")

    print(" base:")
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())
    print(base_creature.transform("sharper"))
    print(base_creature.attack())
    print(base_creature.revert())

    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print(evolved_creature.transform("dragonic battle"))
    print(evolved_creature.attack())
    print(evolved_creature.revert())


def test_m7_ex1() -> None:
    Healing_fac: ex1.HealingCreatureFactory = ex1.HealingCreatureFactory()
    test_healing_factory(Healing_fac)

    Transf_fac: ex1.TransformCreatureFactory = ex1.TransformCreatureFactory()
    test_transform_factory(Transf_fac)


if __name__ == "__main__":
    test_m7_ex1()
