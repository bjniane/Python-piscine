from typing import Self


class Plant:

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> str:
            return (
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

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
        self._stats: Plant._Stats = Plant._Stats()

    @staticmethod
    def is_older_than_year(given_age: int) -> bool:
        return given_age > 365

    @classmethod
    def anonymous_plant(
        cls,
        name: str = "Unknown plant",
        height: float = 0.0,
        age: int = 0
    ) -> Self:
        return cls(name, height, age)

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
        self._stats.record_show()
        return (
            f"{self.name.capitalize()}: {round(self._height, 1)}cm, "
            f"{self._plant_age} days old"
            )

    def grow(self, growth_rate: float = 0.03) -> None:
        self._height += round(self._height * growth_rate, 1)
        self._stats.record_grow()

    def age(self) -> None:
        self._plant_age += 1
        self._stats.record_age()

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


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            color: str,
            number_of_seeds: int = 0):
        super().__init__(name, height, age, color)
        self.number_of_seeds = number_of_seeds

    def bloom(self) -> None:
        super().bloom()
        if self.has_bloomed:
            self.number_of_seeds = 42

    def show(self) -> str:
        return (
            f"{super().show()}\n"
            f" Seeds: {self.number_of_seeds}"
        )


class Tree(Plant):

    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> str:
            return (
                f"{super().display()}\n"
                f" {self._shade_calls} shade"
            )

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree._TreeStats = Tree._TreeStats()

    def show(self) -> str:
        return (
            f"{super().show()}\n"
            f" Trunk diameter: {self.trunk_diameter}"
            )

    def produce_shade(self) -> None:
        self._stats.record_shade()
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
                super().grow(growth_rate)
                super().age()


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    print(plant._stats.display())


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, "red")
    print(rose.show())
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom()
    rose.grow(0.07)
    print(rose.show())
    display_statistics(rose)
    print()

    print("=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 5.0)
    print(oak.show())
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    print("=== Seed")
    seed: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    print(seed.show())
    print("[make sunflower grow, cleage and bloom]")
    seed.grow(0.5)
    seed.age()
    seed.bloom()
    print(seed.show())
    display_statistics(seed)
    print()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, "April")
    print(tomato.show())
    display_statistics(tomato)
    print("[make tomato grow and age for 20 days]")
    tomato.vegetable_growth(20, 0.11)
    print(tomato.show())
    display_statistics(tomato)
    print()

    print("=== Anonymous")
    anonymos = Plant.anonymous_plant()
    print(anonymos.show())
    display_statistics(anonymos)


if __name__ == "__main__":
    main()
