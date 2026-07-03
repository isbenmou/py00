def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    r = range(1, days+1)
    for day in r:
        print(f"Day {day}")
    print("Harvest time!")
ft_count_harvest_iterative()
