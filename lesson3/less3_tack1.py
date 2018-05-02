class Lorry:
    def __init__(self):
        self.boxes = []

    def load_box(self, box):
        self.boxes.append(box)

    def total_cost(self):
        total = 0
        for box in self.boxes:
            total += box.cost()
        return total

class Box:
    def __init__(self, coffee, weight):
        self.coffee = coffee
        self.weight = weight

    def cost(self):
        return self.coffee.price * self.weight

class Coffee:
    def __init__(self, type):
        self.type = type
        self.price = None

    def set_price(self, price):
        self.price = price


arabica = Coffee('Arabica')
robusta = Coffee('Robusta')
arabica.set_price(50)
robusta.set_price(30)
box1 = Box(arabica, 100)
box2 = Box(robusta, 200)
box3 = Box(arabica, 150)
lorry = Lorry()
lorry.load_box(box1)
lorry.load_box(box2)
lorry.load_box(box3)
total = lorry.total_cost()
print(total)