class Plant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age      
    def show(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"        

def main():
    pianta1 = Plant("Rose", 25, 4)
    pianta2 = Plant("Sunflower", 80, 30)
    pianta3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(pianta1.show())
    print(pianta2.show())
    print(pianta3.show())

if __name__ ==  "__main__":
    main()
