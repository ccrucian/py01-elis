class Plant:

    class Stats:

        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0

        def display_stats(self):
            print(f"Stats: {self._grow} grow, "
                  f"{self._age} age, {self._show} show")

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days
        self._stats = self.Stats()

    def title_stats(self):
        print(f"[statistics for {self.name}]")

    def show_stats(self):
        self.title_stats()
        self._stats.display_stats()

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._days} days old")
        self._stats._show += 1

    def age(self, age):
        self._days = self._days + age
        self._stats._age += 1

    def grow(self, lenght):
        self._height = round(self._height + lenght, 1)
        self._stats._grow += 1

    def get_height(self):
        return self._height

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def get_age(self):
        return self._age

    def set_age(self, new_days):
        if new_days >= 0:
            self._days = new_days
            print(f"Age updated: {self._days} days")
        else:
            print(f"{self.name}: Error, age can't be negative")

    @staticmethod
    def older_than_a_year(_days):
        if _days > 365:
            x = "True"
        else:
            x = "False"
        print(f"Is {_days} more than a year? -> {x}")

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):

    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self.bloomed = True


class Seed(Flower):

    def __init__(self, name, height, days, color):
        super().__init__(name, height, days, color)
        self.seeds = 0

    def check_bloom(self):
        if self.bloomed:
            self.seeds += 42
        else:
            pass

    def seed_born(self):
        print(f"[make {self.name} grow, age and bloom]")

    def bloom(self):
        self.bloomed = True

    def seeds_stat(self):
        print(f" Seeds: {self.seeds}")

    def show(self):
        super().show()


class Tree(Plant):

    def __init__(self, name, height, days, diameter):
        super().__init__(name, height, days)
        self.diameter = diameter
        self.shade = 0

    def show_stats(self):
        super().show_stats()
        print(f"{self.shade} shade")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self):
        self.shade += 1
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.diameter}cm wide.")


def main():

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
    plant1.show_stats()
    plant1.bloom()
    plant1.show()
    plant1.show_stats()
    print("")
    print("=== Tree")
    plant2.show()
    plant2.show_stats()
    plant2.produce_shade()
    plant2.show_stats()
    print("")
    print("=== Seed")
    seed.show()
    seed.seeds_stat()
    seed.seed_born()
    seed.age(20)
    seed.grow(30.0)
    seed.bloom()
    seed.show()
    seed.check_bloom()
    seed.seeds_stat()
    seed.show_stats()
    print("")
    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    unknown.show_stats()


if __name__ == "__main__":
    main()
