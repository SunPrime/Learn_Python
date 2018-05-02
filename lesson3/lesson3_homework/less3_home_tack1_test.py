import unittest

from lesson3.lesson3_homework.less3__home_tack1 import Flower, Decorative_greenery, Decor, Bouquet, Bouquet_part


class MyTestCase(unittest.TestCase):
    def test_bouquet(self):
        rosa = Flower('rosa', 40)
        lily = Flower('lily', 100)
        green = Decorative_greenery('some green', 20)
        dec = Decor('some decor', 10)
        bouquet1 = Bouquet()
        bouquet1.add_bouquet_part(rosa, 5)
        bouquet1.add_bouquet_part(green, 2)
        bouquet1.add_bouquet_part(dec, 1)
        bouquet1.add_bouquet_part(lily, 2)
        self.assertEqual(bouquet1.calculate_total_cost(), 450, 'cost')
        self.assertEqual(bouquet1.bouquet_print(), """Вы выбрали rosa по 40 грн - 5 шт
Вы выбрали some green по 20 грн - 2 шт
Вы выбрали some decor по 10 грн - 1 шт
Вы выбрали lily по 100 грн - 2 шт

Общая сумма: 450 гривен""", 'print')

    def test_cost(self):
        rosa = Flower('rosa', 50)
        bouquet_part = Bouquet_part(rosa, 5)
        self.assertEqual(bouquet_part.cost(), 250)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
