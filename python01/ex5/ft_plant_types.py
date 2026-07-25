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


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str
            ) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> str:
        if self.has_bloomed:
            msj = f"{self.name.capitalize()} is blooming beautifully!"
        else:
            msj = f"{self.name.capitalize()} has not bloomed yet"
        return (
            f"{super().show()}\n"
            f" Color: {self.color}\n"
            f" {msj}"
            )


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> str:
        return (
            f"{super().show()}\n"
            f" Trunk diameter: {self.trunk_diameter}"
            )

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int = 0
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> str:
        return (
            f"{super().show()}\n"
            f" Harvest season: {self.harvest_season.capitalize()}\n"
            f" Nutritional value: {self.nutritional_value}"
            )

    def vegetable_growth(self, days: int, growth_rate: float = 0.03) -> None:
        if days > 0:
            for _ in range(days):
                self.nutritional_value += 1
                self.grow(growth_rate)
                self.age()


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, "red")
    print(rose.show())
    print("[asking the rose to bloom]")
    rose.bloom()
    print(rose.show())
    print()

    print("=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 5.0)
    print(oak.show())
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, "April")
    print(tomato.show())
    print("[make tomato grow and age for 20 days]")
    tomato.vegetable_growth(20, 0.11)
    print(tomato.show())
    print("----------------------------------------------------")
    onion: Vegetable = Vegetable("onion", 3.0, 40, "mars")
    print(onion.show())
    print("[make onion grow and age for 5 days]")
    onion.vegetable_growth(5, 0.5)
    print(onion.show())


if __name__ == "__main__":
    main()
