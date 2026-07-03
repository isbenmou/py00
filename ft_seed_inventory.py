def ft_seed_inventory(seed_type: str, quantity : int, unit : str) -> None:
    if unit == "packets":
        new_unit = "packets available"
    elif unit == "grams":
        new_unit = "grams total"
    else:
        print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
        return
    print(f"{seed_type.capitalize()} seeds: {quantity} {new_unit}")
ft_seed_inventory("lettuce", 12, "area")
