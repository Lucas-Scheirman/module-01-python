class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = float(height)
        self._days = int(days)

    def show(self) -> None:
        print(
            f"{self._name}:"
            f" {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._days += 1

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


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-1)
    rose.set_age(-5)
    print("Current state:", end=" ")
    rose.show()
