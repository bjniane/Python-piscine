def recursion(current=1, target=1):
    if current <= target:
        print("Day", current)
        recursion(current + 1, target)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursion(target=days)
    print("Harvest time!")

