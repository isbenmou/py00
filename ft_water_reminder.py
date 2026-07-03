def ft_water_reminder():
    nb_days = int(input("Days since last watering: "))
    if nb_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
ft_water_reminder()
