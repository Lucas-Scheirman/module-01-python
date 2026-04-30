class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = float(height)
        self._days = int(days)
        self._stats = Plant.Stats()

    def show(self) -> None:
        print(
            f"{self._name}:"
            f" {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )
        self._stats._show += 1

    def grow(self) -> None:
        self._height += 0.8
        self._stats._grow += 1

    def age(self) -> None:
        self._days += 1
        self._stats._age += 1

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self._name}: "
                f"Error, height can't be negative\n"
                f"Height update rejected"
            )
        else:
            self._height = height
            print(f"Height updated: {int(self.get_height())}cm")

    def set_age(self, days: int) -> None:
        if days < 0:
            print(
                f"{self._name}: "
                f"Error, age can't be negative\n"
                f"Age update rejected"
            )
        else:
            self._days = days
            print(f"Age updated: {int(self.get_age())} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0


class Flower(Plant):
    def __init__(
        self, name: str, height: float, days: int, color: str
    ) -> None:
        super().__init__(name, height, days)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._bloomed:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    def __init__(
        self, name: str, height: float, days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days)
        self._trunk_diameter = float(trunk_diameter)
        self._produce_shade_count = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self.get_height(), 1)}cm long and "
            f"{self._trunk_diameter}cm wide."
        )
        self._produce_shade_count += 1


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, days: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {int(self._nutritional_value)}")

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 0.5
        self._stats._grow += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
