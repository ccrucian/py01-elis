class Plant:

    class Stats:

        def __init__(self) -> None:
            self._grow: int = 0
            self._age: int = 0
            self._show: int = 0
            self._shade: int = 0

        def add_grow(self) -> None:
            self._grow += 1

        def add_age(self) -> None:
            self._age += 1

        def add_show(self) -> None:
            self._show += 1

        def add_shade(self) -> None:
            self._shade += 1

        def display_stats(self) -> None:
            print(f"Stats: {self._grow} grow, "
                  f"{self._age} age, {self._show} show")

        def display_shade(self) -> None:
            print(f"{self._shade} shade")

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self._height: float = height
        self._days: int = days
        self._stats: Plant.Stats = self.Stats()

    def title_stats(self) -> None:
        print(f"[statistics for {self.name}]")

    def show_stats(self) -> None:
        self.title_stats()
        self._stats.display_stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._days} days old")
        self._stats.add_show()

    def age(self, age: int) -> None:
        self._days = self._days + age
        self._stats.add_age()

    def grow(self, lenght: float) -> None:
        self._height = round(self._height + lenght, 1)
        self._stats.add_grow()

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: int) -> None:
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

    @staticmethod
    def older_than_a_year(_days: int) -> None:
        if _days > 365:
            x: str = "True"
        else:
            x = "False"
        print(f"Is {_days} more than a year? -> {x}")

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


def display_statistics(plant: Plant) -> None:
    plant.show_stats()


class Flower(Plant):

    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self.color: str = color
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


class Seed(Flower):

    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self.seeds: int = 0

    def seed_born(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")

    def bloom(self) -> None:
        self.bloomed = True
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):

    def __init__(self, name: str, height: float, days: int,
                 diameter: float) -> None:
        super().__init__(name, height, days)
        self.diameter: float = diameter

    def show_stats(self) -> None:
        super().show_stats()
        self._stats.display_shade()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.diameter}cm wide.")


def main() -> None:

    plant1 = Flower("Rose", 15.0, 10, "red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.older_than_a_year(30)
    Plant.older_than_a_year(400)
    print("")
    print("=== Flower")
    plant1.show()
    display_statistics(plant1)
    plant1.bloom()
    plant1.show()
    display_statistics(plant1)
    print("")
    print("=== Tree")
    plant2.show()
    display_statistics(plant2)
    plant2.produce_shade()
    display_statistics(plant2)
    print("")
    print("=== Seed")
    seed.show()
    seed.seed_born()
    seed.age(20)
    seed.grow(30.0)
    seed.bloom()
    seed.show()
    display_statistics(seed)
    print("")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
