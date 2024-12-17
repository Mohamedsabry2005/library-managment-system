from Resources.Models.Human import Human
from Resources.Models.Order import Order


class Client(Human):
    """
    Represents a client of the library.

    Attributes:
        phone_num (str): Client's phone number.
        id (int): Unique identifier for the client.
        name (str): Name of the client.
        age (int): Age of the client.
        id_num (str): National ID number of the client.
        address (str): Address of the client.
        reading_history (list[Order]): List of orders representing the client's reading history.
        orders_num (int): Total number of orders the client has made.
    """

    def __init__(self, phone_num, id, name, age, id_num, address, reading_history, orders_num):
        """
        Initializes a Client object with the given attributes.
        """
        super(Client, self).__init__(id=id, name=name, age=age, id_num=id_num, phone_num=phone_num, address=address)
        self.reading_history = reading_history
        self.orders_num = orders_num

    def get_reading_history(self):
        """Returns the client's reading history."""
        return self.reading_history

    def set_reading_history(self, new_history):
        """
        Sets the reading history of the client.

        Args:
            new_history (list): List of Order objects.

        Raises:
            ValueError: If new_history is not a list of Order objects.
        """
        if isinstance(new_history, list) and all(isinstance(order, Order) for order in new_history):
            self.reading_history = new_history
        else:
            raise ValueError("Reading history must be a list of Order objects.")

    def get_orders_num(self):
        """Returns the number of orders made by the client."""
        return self.orders_num

    def set_orders_num(self, orders_num):
        """Sets the number of orders made by the client."""
        self.orders_num = orders_num

    def to_dict(self):
        """
        Converts the Client object into a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the client.
        """
        return {
            "phone_num": self.phone_num,
            "id": self.get_id(),
            "name": self.name,
            "age": self.age,
            "id_num": self.get_id_num(),
            "address": self.address,
            "reading_history": [order.to_dict() for order in self.reading_history],
            "orders_num": self.orders_num,
        }
