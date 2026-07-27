def input_temperature(temp_str: str):
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
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
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
