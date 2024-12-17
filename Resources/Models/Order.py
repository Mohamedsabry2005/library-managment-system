class Order:
    """
    Represents an order made by a client.

    Attributes:
        id (int): Unique identifier for the order.
        date (str): Date of the order.
        client_id (int): ID of the client who made the order.
        book_id (int): ID of the book related to the order.
        status (str): Current status of the order (e.g., "Completed", "Pending").
        order_type (str): Type of order ("buy" or "borrow").
        price (float): Price of the book if the order type is "buy".
    """
    def __init__(self, id, date, client_id, book_id, status, order_type, price=None):
        """
        Initializes an Order object with the given attributes.
        """
        self.__id = id
        self.date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.status = status
        self.order_type = order_type
        self.price = price if order_type == "buy" else None

    def get_id(self):
        """Returns the ID of the order."""
        return self.__id

    def set_id(self, id):
        """Sets the ID of the order."""
        self.__id = id

    def get_date(self):
        """Returns the date of the order."""
        return self.date

    def set_date(self, date):
        """Sets the date of the order."""
        self.date = date

    def get_client_id(self):
        """Returns the ID of the client who made the order."""
        return self.__client_id

    def set_client_id(self, client_id):
        """Sets the ID of the client who made the order."""
        self.__client_id = client_id

    def get_book_id(self):
        """Returns the ID of the book related to the order."""
        return self.__book_id

    def set_book_id(self, book_id):
        """Sets the ID of the book related to the order."""
        self.__book_id = book_id

    def get_status(self):
        """Returns the status of the order."""
        return self.status

    def set_status(self, status):
        """Sets the status of the order."""
        self.status = status

    def get_order_type(self):
        """Returns the type of the order."""
        return self.order_type

    def set_order_type(self, order_type):
        """Sets the type of the order."""
        self.order_type = order_type

    def get_price(self):
        """Returns the price of the order if applicable."""
        return self.price

    def set_price(self, price):
        """Sets the price of the order."""
        self.price = price

    def to_dict(self):
        """
        Converts the Order object into a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the order.
        """
        data = {
            "id": self.__id,
            "date": self.date,
            "client_id": self.__client_id,
            "book_id": self.__book_id,
            "status": self.status,
            "order_type": self.order_type,
        }
        if self.order_type == "buy":
            data["price"] = self.price
        return data

    @classmethod
    def from_dict(cls, data):
        """
        Creates an Order object from a dictionary.

        Args:
            data (dict): Dictionary representation of an order.

        Returns:
            Order: An Order object created from the dictionary data.
        """
        return cls(
            id=data["id"],
            date=data["date"],
            client_id=data["client_id"],
            book_id=data["book_id"],
            status=data["status"],
            order_type=data["order_type"],
            price=data.get("price"),
        )
