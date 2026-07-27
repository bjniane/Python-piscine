class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown plant error"):
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(self, error_message: str = "Unknown plant error"):
        super().__init__(error_message)


class WaterError(GardenError):
    def __init__(self, error_message: str = "Unknown plant error"):
        super().__init__(error_message)


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_all_garden_errors() -> None:
    for func in [test_plant_error, test_water_error]:
        try:
            func()
        except GardenError as e:
            print(f"Caught GardenError: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    test_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
