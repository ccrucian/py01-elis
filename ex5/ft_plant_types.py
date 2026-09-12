class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days} days old")

    def age(self) -> None:
        self._days = self._days + 1

    def grow(self, lenght: float) -> None:
        self._height = round(self._height + lenght, 1)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_age(self) -> int:
        return self._days

    def set_age(self, new_days: int) -> None:
        if new_days >= 0:
            self._days = new_days
            print(f"Age updated: {self._days} days")
        else:
            print(f"{self.name}: Error, age can't be negative")


class Flower(Plant):

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:

        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True


class Tree(Plant):

    def __init__(self, name: str, height: float, days: int,
                 diameter: float) -> None:
        super().__init__(name, height, days)
        self.diameter = diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.diameter}cm wide.")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str, nutritional_value: int):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def make_tomato(self, time: int, lenght: float) -> None:
        print(f"[make {self.name} grow and age for {time} days]")
        for i in range(time):
            self.age()
            self.grow(lenght)


def main() -> None:

    plant1 = Flower("Rose", 15.0, 10, "red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    plant3 = Vegetable("Tomato", 5.0, 10, "April", 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1.show()
    plant1.bloom()
    plant1.show()
    print("")
    print("=== Tree")
    plant2.show()
    plant2.produce_shade()
    print("")
    print("=== Vegetable")
    plant3.show()
    plant3.make_tomato(20, 2.1)
    plant3.show()


if __name__ == "__main__":

    main()
