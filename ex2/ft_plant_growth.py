class Plant:

    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self):
        self.height = round(self.height + 0.5, 1)

    def age(self):
        self.days += 1


def main():

    plant1 = Plant("Rose", 20.0, 30)
    start = plant1.height
    print("=== Garden Plant Growth ===")
    plant1.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant1.grow()
        plant1.age()
        plant1.show()

    print(f"Growth this week: {plant1.height - start}cm")


if __name__ == "__main__":
    main()
