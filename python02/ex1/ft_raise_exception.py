def input_temperature(temp_str: str):
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        if temp_int > 40:
            raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
        if temp_int < 0:
            raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
        return temp_int
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")
        return None


def test_temperature() -> None:
    temp = input_temperature("25")
    if temp is not None:
        print(f"Temperature is now {temp}°C\n")

    temp = input_temperature("abc")
    if temp is not None:
        print(f"Temperature is now {temp}°C\n")

    temp = input_temperature("100")
    if temp is not None:
        print(f"Temperature is now {temp}°C\n")

    temp = input_temperature("-50")
    if temp is not None:
        print(f"Temperature is now {temp}°C\n")

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
