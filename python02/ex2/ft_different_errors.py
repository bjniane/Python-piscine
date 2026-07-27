def garden_operations(op_number: int) -> None:
    if op_number == 0:
        int("abc")
    elif op_number == 1:
        100 / 0
    elif op_number == 2:
        open("/non/existent/file")
    elif op_number == 3:
        "hello" + 12


def test_error_types() -> None:
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully\n")
        except (ValueError, ZeroDivisionError, FileNotFoundError,
                TypeError) as e:
            print(f"Caught {e.__class__.__name__}: {e}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
