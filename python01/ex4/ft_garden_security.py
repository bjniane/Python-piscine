class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age: int
            ) -> None:
        self.name = name
        self._height = height
        self._plant_age = age
        self.initial_height = height

    def get_age(self) -> int:
        return self._plant_age

    def get_height(self) -> float:
        return self._height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(
                f"{self.name.capitalize()}: Error, age can't be negative"
            )
            print("Age update rejected")
        else:
            self._plant_age = new_age
            print(f"Age updated: {self._plant_age} days")

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(
                f"{self.name.capitalize()}: Error, height can't be negative"
            )
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def show(self) -> str:
        return (
            f"{self.name.capitalize()}: {round(self._height, 1)}cm, "
            f"{self._plant_age} days old"
            )

    def grow(self, growth_rate: float = 0.03) -> None:
        self._height += round(self._height * growth_rate, 1)

    def age(self) -> None:
        self._plant_age += 1

    def weekly_growth(self) -> float:
        return round(self._height - self.initial_height, 1)


def main() -> None:
    print("=== Garden Security System ===")

    rose: Plant = Plant("rose", 15.0, 10)

    print(f"Plant created: {rose.show()}\n")

    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-1)
    rose.set_age(-1)

    print(f"\nCurrent state: {rose.show()}")


if __name__ == "__main__":
    main()
