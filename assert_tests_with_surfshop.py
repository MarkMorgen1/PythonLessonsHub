import surfshop
import unittest
import datetime


class BoardShopTestClass(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()  # brings a copy of cart into this test file

    def test_add_boards_to_cart(self):
        for num in [
            2,
            3,
            4,
        ]:
            self.cart = (
                surfshop.ShoppingCart()
            )  # Reset cart for each test run, so no items in cart
            self.assertEqual(
                self.cart.add_surfboards(num),
                f"Successfully added {num} surfboards to cart!",
            )
        for num in [
            5,
            6,
        ]:
            self.cart = (
                surfshop.ShoppingCart()
            )  # Reset cart for each test run, so no items in cart
            self.assertEqual(
                self.cart.add_surfboards(num),
                f"Cart cannot have more than 4 surfboards in it!",
            )

    def test_checkout_date(self):
        date = datetime.datetime.strptime("2025-08-09", "%Y-%m-%d")
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)

    def test_locals_discount(self):
        self.cart.apply_locals_discount()  # call to function
        self.assertTrue(self.cart.locals_discount)


unittest.main()
