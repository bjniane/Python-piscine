class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown plant error"):
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(self, error_message: str = "Unknown plant error"):
        super().__init__(error_message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(
            f"Invalid plant name to water: '{plant_name}'\n"
            f".. ending tests and returning to main"
        )


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
