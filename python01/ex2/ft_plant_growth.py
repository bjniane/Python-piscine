class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            growth_rate: float = 0.03
            ) -> None:
        self.name = name
        self.height = height
        self.plant_age = age
        self.growth_rate = growth_rate
        self.initial_height = height

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
            f"{self.plant_age} days old"
            )

    def grow(self) -> None:
        self.height += round(self.height * self.growth_rate, 1)

    def age(self) -> None:
        self.plant_age += 1

    def weekly_growth(self) -> float:
        return round(self.height - self.initial_height, 1)


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose: Plant = Plant("rose", 25.0, 30, 0.03)
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    total_growth: float = rose.weekly_growth()
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    main()
