class Plant:

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._days} days old")

    def age(self):
        self._days = self._days + 1

    def grow(self):
        self.height = round(self.height + 1.2, 1)

    def get_height(self):
        return self._height

    def set_height(self, new_height):
        if new_height < 0:
            print(f"""{self.name}: Error, height can't be negative
            Height update rejected""")
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


def main():

    plant1 = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("")
    print("Plant created:", end=" ")
    plant1.show()
    print("")
    plant1.set_height(25.0)
    plant1.set_age(30)
    print("")
    plant1.set_height(-3)
    plant1.set_age(-45)
    print("")
    print("Current state:", end=" ")
    plant1.show()


if __name__ == "__main__":
    main()
