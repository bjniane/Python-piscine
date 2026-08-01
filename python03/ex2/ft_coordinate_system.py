import math


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError as e:
        print(f"Error on parameter '{s}': {e}")
        return False


def get_player_pos() -> tuple:
    while True:
        player_coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': ").split(",")
        if len(player_coordinates) != 3:
            print("Invalid syntax")
            continue

        corrds: list[float] = []
        is_valid = True
        for i in range(len(player_coordinates)):
            if is_number(player_coordinates[i]):
                corrds.append(float(player_coordinates[i]))
            else:
                is_valid = False
                break
        if is_valid:
            break
    return tuple(corrds)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first_tuple: tuple = get_player_pos()
    print(f"Got a first tuple: {first_tuple}")
    X1, Y1, Z1 = first_tuple
    print(f"It includes: X={X1}, Y={Y1}, Z={Z1}")
    distance_to_center = math.sqrt((X1 - 0)**2 + (Y1 - 0)**2 + (Z1 - 0)**2)
    print(f"Distance to center: {round(distance_to_center, 4)}")

    print("\nGet a second set of coordinates")
    second_tuple: tuple = get_player_pos()
    X2, Y2, Z2 = second_tuple
    distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2 + (Z2 - Z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
