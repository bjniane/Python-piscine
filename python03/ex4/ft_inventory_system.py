import sys


def duplicate_item(dic: dict[str, int], item: str) -> bool:
    for key in dic.keys():
        if key == item:
            return True
    return False


def get_item_name(my_dict: dict[str, int]) -> list[str]:
    item_list: list[str] = []
    for key in my_dict.keys():
        item_list.append(key)
    return item_list


def most_abundant(my_dict: dict[str, int]) -> tuple[str, int]:
    largest_key: str = str()
    largest_value = float('-inf')

    for key in my_dict.keys():
        if my_dict[key] > largest_value:
            largest_value = my_dict[key]
            largest_key = key
    return largest_key, int(largest_value)


def least_abundant(my_dict: dict[str, int]) -> tuple[str, int]:
    lowest_key: str = str()
    lowest_value = float('inf')

    for key in my_dict.keys():
        if my_dict[key] < lowest_value:
            lowest_value = my_dict[key]
            lowest_key = key
    return lowest_key, int(lowest_value)


def get_inventor() -> dict[str, int]:
    my_dict: dict[str, int] = {}
    for i in range(1, len(sys.argv)):
        try:
            items: list = sys.argv[i].split(':')
            if len(items) != 2:
                print(f"Error - invalid parameter '{items[0]}'")
            else:
                item_name, quantity = items
                quantity = int(quantity)
                if not duplicate_item(my_dict, item_name):
                    my_dict.update({item_name: quantity})
                else:
                    print(f"Redundant item '{item_name}' - discarding")
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
    return my_dict


def inventory_system() -> None:
    if len(sys.argv) == 1:
        print(
            "No info provided. Usage: python3"
            " ft_inventory_system.py <item_name>:<quantity> ..."
        )
        return
    else:
        my_dict: dict[str, int] = get_inventor()
        print(f"Got inventory: {my_dict}")

        item_list: list[str] = get_item_name(my_dict)
        print(f"Item list: {item_list}")

        total_quantity: int = sum(my_dict.values())
        print(
            f"Total quantity of the {len(item_list)}items: {total_quantity}"
        )

        # The quantity percentage it represents in the inventory
        for item in item_list:
            result = round((my_dict[item] / total_quantity) * 100, 1)
            print(f"Item {item} represents {result}%")

        # Report the most and least abundant items
        largest_key, largest_value = most_abundant(my_dict)
        lowest_key, lowest_value = least_abundant(my_dict)
        print(
            f"Item most abundant: {largest_key} with quantity {largest_value}"
        )
        print(
            f"Item least abundant: {lowest_key} with quantity {lowest_value}"
        )

        my_dict.update({"magic_item": 1})
        print(f"Updated inventory: {my_dict}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory_system()


if __name__ == "__main__":
    main()
