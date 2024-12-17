class Book:
    """
    Represents a book in the library.

    Attributes:
        id (int): Unique identifier for the book.
        title (str): Title of the book.
        description (str): A brief description of the book.
        author (str): Author of the book.
        status (str): Current status of the book (e.g., "Available", "Checked out").
        categories (list): List of categories the book belongs to.
        ISBN (str): International Standard Book Number of the book.
        image (str): Path or URL to the book's cover image.
        price (float): Price of the book if it is buyable.
        quantity (int): Number of copies available in the library.
        borrowable (bool): Whether the book can be borrowed.
        buyable (bool): Whether the book can be purchased.
    """
    def __init__(self, id, title, description, author, status, categories, ISBN, image, price, quantity, borrowable: bool, buyable: bool):
        """
        Initializes a Book object with the given attributes.
        """
        self.__id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status
        self.categories = categories
        self.ISBN = ISBN
        self.image = image
        self.price = price
        self.quantity = quantity
        self.borrowable = borrowable
        self.buyable = buyable

    def get_Book_id(self):
        """Returns the ID of the book."""
        return self.__id

    def set_Book_id(self, id):
        """Sets the ID of the book."""
        self.__id = id

    def get_Book_title(self):
        """Returns the title of the book."""
        return self.title

    def set_Book_tittle(self, title):
        """Sets the title of the book."""
        self.title = title

    def get_Book_description(self):
        """Returns the description of the book."""
        return self.description

    def set_Book_descriptioj(self, description):
        """Sets the description of the book."""
        self.description = description

    def get_Book_author(self):
        """Returns the author of the book."""
        return self.author

    def set_Book_author(self, author):
        """Sets the author of the book."""
        self.author = author

    def get_Book_status(self):
        """Returns the status of the book."""
        return self.status

    def set_Book_status(self, status):
        """Sets the status of the book."""
        self.status = status

    def get_Book_categories(self):
        """Returns the categories of the book."""
        return self.categories

    def set_Book_categories(self, categories):
        """Sets the categories of the book."""
        self.categories = categories

    def get_Book_ISBN(self):
        """Returns the ISBN of the book."""
        return self.ISBN

    def set_Book_ISBN(self, ISBN):
        """Sets the ISBN of the book."""
        self.ISBN = ISBN

    def get_Book_image(self):
        """Returns the image of the book."""
        return self.image

    def set_Book_image(self, image):
        """Sets the image of the book."""
        self.image = image

    def get_Book_price(self):
        """Returns the price of the book."""
        return self.price

    def set_Book_price(self, price):
        """Sets the price of the book."""
        self.price = price

    def get_Book_quantity(self):
        """Returns the quantity of the book."""
        return self.quantity

    def set_Book_quantity(self, quantity):
        """Sets the quantity of the book."""
        self.quantity = quantity

    def get_Book_borrowable(self):
        """Returns whether the book is borrowable."""
        return self.borrowable

    def set_Book_borrowable(self, borrowable):
        """Sets whether the book is borrowable."""
        self.borrowable = borrowable

    def get_Book_buyable(self):
        """Returns whether the book is buyable."""
        return self.buyable

    def set_Book_buyable(self, buyable):
        """Sets whether the book is buyable."""
        self.buyable = buyable

    def to_dict(self):
        """
        Converts the Book object into a dictionary for serialization.

        Returns:
            dict: Dictionary representation of the book.
        """
        return {
            "id": self.__id,
            "title": self.title,
            "description": self.description,
            "author": self.author,
            "status": self.status,
            "categories": self.categories,
            "ISBN": self.ISBN,
            "image": self.image,
            "price": self.price,
            "quantity": self.quantity,
            "borrowable": self.borrowable,
            "buyable": self.buyable,
        }
