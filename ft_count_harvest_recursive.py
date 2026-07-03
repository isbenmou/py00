def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def recursive(days, i):
        if (i > days):
            print("Harvest time!")
            return
        recursive(days, i+1)
ft_count_harvest_recursive()
