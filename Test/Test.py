import unittest
import os, sys
current_folder = os.getcwd()

print("Current Folder Path:", current_folder)
sys.path.insert(2, current_folder)


from Resources.Models.Book import Book
from Resources.Models.Client import Client
from Resources.Models.Order import Order


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(
            1, "Title", "Description", "Author", "Available", ["Fiction"],
            "123456789", "image.png", 10.99, 5, True, True
        )

    def test_get_book_id(self):
        self.assertEqual(self.book.get_Book_id(), 1)

    def test_set_book_id(self):
        self.book.set_Book_id(2)
        self.assertEqual(self.book.get_Book_id(), 2)

    def test_to_dict(self):
        book_dict = self.book.to_dict()
        self.assertEqual(book_dict["id"], 1)
        self.assertEqual(book_dict["title"], "Title")

    def test_borrowable_and_buyable(self):
        # Test valid borrowable and buyable states
        self.assertTrue(self.book.get_Book_borrowable())
        self.assertTrue(self.book.get_Book_buyable())

        # Test changing borrowable and buyable
        self.book.set_Book_borrowable(False)
        self.book.set_Book_buyable(False)
        self.assertFalse(self.book.get_Book_borrowable())
        self.assertFalse(self.book.get_Book_buyable())


class TestClient(unittest.TestCase):
    def setUp(self):
        self.orders = [Order(1, "2024-12-16", 1, 1, "Completed", "buy", 10.99)]
        self.client = Client("555-555-5555", 1, "John Doe", 30, "ID123", "123 Street", self.orders, 1)

    def test_get_reading_history(self):
        history = self.client.get_reading_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].get_id(), 1)

    def test_set_reading_history(self):
        # Valid case: Pass a list of Order objects
        new_order = Order(2, "2024-12-16", 2, 2, "Pending", "borrow")
        self.client.set_reading_history([new_order])
        self.assertEqual(self.client.get_reading_history()[0].get_id(), 2)

        # Invalid case: Pass a list with non-Order objects
        with self.assertRaises(ValueError):
            self.client.set_reading_history(["not an order"])

    def test_to_dict(self):
        client_dict = self.client.to_dict()
        self.assertEqual(client_dict["name"], "John Doe")
        self.assertEqual(client_dict["orders_num"], 1)


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order(1, "2024-12-16", 1, 1, "Completed", "buy", 10.99)

    def test_get_id(self):
        self.assertEqual(self.order.get_id(), 1)

    def test_set_id(self):
        self.order.set_id(2)
        self.assertEqual(self.order.get_id(), 2)

    def test_to_dict(self):
        order_dict = self.order.to_dict()
        self.assertEqual(order_dict["id"], 1)
        self.assertEqual(order_dict["order_type"], "buy")
        self.assertEqual(order_dict["price"], 10.99)

    def test_from_dict(self):
        data = {
            "id": 2,
            "date": "2024-12-17",
            "client_id": 2,
            "book_id": 3,
            "status": "Pending",
            "order_type": "borrow"
        }
        new_order = Order.from_dict(data)
        self.assertEqual(new_order.get_id(), 2)
        self.assertEqual(new_order.get_order_type(), "borrow")

    def test_price_set_only_for_buy(self):
        # Valid case: Order type is "buy"
        buy_order = Order(3, "2024-12-17", 1, 1, "Completed", "buy", 15.99)
        self.assertEqual(buy_order.get_price(), 15.99)

        # Invalid case: Order type is not "buy"
        borrow_order = Order(4, "2024-12-17", 1, 1, "Pending", "borrow")
        self.assertIsNone(borrow_order.get_price())

        # Changing price for non-buy order
        borrow_order.set_price(20.00)
        self.assertEqual(borrow_order.get_price(), 20.00)


if __name__ == "__main__":
    unittest.main()
