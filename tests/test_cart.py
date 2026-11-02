import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", cost=0.8)
            self.assertTrue(cart.add_dvd(dvd))

        dvd_21 = DigitalVideoDisc("DVD 21", cost=0.8)
        self.assertFalse(cart.add_dvd(dvd_21))


    def test_sort_by_title(self):
    	cart = Cart()

    	cart.add_dvd(DigitalVideoDisc("Star Wars", cost=20))
    	cart.add_dvd(DigitalVideoDisc("Aladdin", cost=10))
    	cart.add_dvd(DigitalVideoDisc("The Lion King", cost=30))

    	cart.sort_by_title()

    	titles = [dvd.title for dvd in cart.items]

    	self.assertEqual(
        	titles,
        	["Aladdin", "Star Wars", "The Lion King"]
    	)


    def test_sort_by_cost(self):
    	cart = Cart()

    	cart.add_dvd(DigitalVideoDisc("Star Wars", cost=20))
    	cart.add_dvd(DigitalVideoDisc("Aladdin", cost=10))
    	cart.add_dvd(DigitalVideoDisc("The Lion King", cost=30))

    	cart.sort_by_cost()

    	costs = [dvd.cost for dvd in cart.items]

    	self.assertEqual(costs, [10, 20, 30])

if __name__ == "__main__":
    unittest.main()