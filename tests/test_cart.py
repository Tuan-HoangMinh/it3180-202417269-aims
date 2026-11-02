import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for i in range(20):
            dvd = DigitalVideoDisc(f"DVD {i}", cost=80)
            self.assertTrue(cart.add_dvd(dvd))

        dvd_21 = DigitalVideoDisc("DVD 21", cost=80)
        self.assertFalse(cart.add_dvd(dvd_21))


if __name__ == "__main__":
    unittest.main()