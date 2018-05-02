#создание и стоимость букета
class Bouquet:
    def __init__(self):
        self.part = []

    def add_bouquet_part(self, type, quantity):
        self.part.append(Bouquet_part(type, quantity))

    def calculate_total_cost(self):
        total = 0
        for bouquet_part in self.part:
            total += bouquet_part.cost()
        return total

    def bouquet_print(self):
        res = ''
        for bouquet_part in self.part:
            res += "Вы выбрали %s по %d грн - %d шт\n" % (bouquet_part.type.type, bouquet_part.type.price, bouquet_part.quantity)
        cost = self.calculate_total_cost()
        return res + "\nОбщая сумма: %d гривен" % cost


#часть букета, передаем количество, считаем стоимость части букета
class Bouquet_part():
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

    def cost(self):
        return self.quantity * self.type.price


#цветы
class Flower:
    def __init__(self, type, price):
        self.type = type
        self.price = price

#зелень
class Decorative_greenery:
    def __init__(self, type, price):
        self.type = type
        self.price = price

#декор
class Decor:
    def __init__(self, type, price):
        self.type = type
        self.price = price

def main():
    rosa = Flower('rosa', 40)
    lily = Flower('lily', 100)
    green = Decorative_greenery('some green', 20)
    dec = Decor('some decor', 10)
    bouquet1 = Bouquet()
    bouquet1.add_bouquet_part(rosa, 5)
    bouquet1.add_bouquet_part(green, 2)
    bouquet1.add_bouquet_part(dec, 1)
    bouquet1.add_bouquet_part(lily, 2)
    res = bouquet1.bouquet_print()
    print(res)

main()