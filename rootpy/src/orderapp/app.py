class Basket:
    def __init__(self):
        self.basket = []

    def __add__(self, fruit):
        self.basket.append(fruit)

    def __del__(self, fruit):
        return self.basket.remove(fruit) if fruit in self.basket else None


