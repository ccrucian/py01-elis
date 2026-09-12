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

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._days} days old")
        self._stats._show += 1
        print(f"[statistics for {self.name}]")
        self._stats.display_stats()

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
        return _days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plan", 0.0, 0)
       

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

    def __init__(self, name, height, days, color, seeds):
        super().__init__(name, height, days, color)
        self.seeds = seeds

    def check_bloom(self):
        if self.bloomed:
            self.seeds += 42
        else:
            pass

    def bloom(self):
        super().bloom()

    def seeds_stat(self):
        print(f" Seeds: {self.seeds}")

    def show(self):
        super().show()


class Tree(Plant):

    def __init__(self, name, height, days, diameter):
        super().__init__(name, height, days)
        self.diameter = diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.diameter}cm")

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self.diameter}cm wide.")


def main():

    plant1 = Flower("Rose", 15.0, 10, "red")
    plant2 = Tree("Oak", 200.0, 365, 5.0)
    seed = Seed("Rose", 15.0, 10, "red", 0)
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("=== Flower")
    plant1.show()
    plant1.bloom()
    plant1.show()
    print("")
    print("=== Tree")
    plant2.show()
    plant2.produce_shade()
    #plant2.display_stats()
    print("")
    print("=== Seed")
    seed.show()
    seed.bloom()
    seed.check_bloom()
    seed.seeds_stat()



if __name__ == "__main__":

    main()
