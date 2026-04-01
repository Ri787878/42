def ft_seed_inventory(seed_tp: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_tp.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_tp.capitalize()} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_tp.capitalize()} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
