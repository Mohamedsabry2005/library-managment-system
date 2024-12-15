class Book:
    def __init__(self,id,title,description,author,status, categories , ISBN , image , price , quantity , borrowable:bool , buyable:bool):
        self.__id=id
        self.title = title
        self.description = description
        self.author = author
        self.status= status
        self.categories = categories
        self.ISBN = ISBN
        self.image = image
        self.price = price
        self.quantity = quantity
        self.borrowable = borrowable
        self.buyable = buyable


    def get_Book_id(self):
        return self.__id
    
    def set_Book_id(self,id):
        self.__id=id

    def get_Book_tittle(self):
            return self.tittle

    def set_Book_tittle(self, tittle):
            self.tittle = tittle

    def get_Book_description(self):
        return self.description
    def set_Book_descriptioj(self,description):
        self.description=description

    def get_Book_author(self):
            return self.author

    def set_Book_author(self, author):
            self.author = author

    def get_Book_status(self):
        return self.__status
    
    def set_Book_status(self,status):
        self.__status=status

    
    def get_Book_category(self):
            return self.category

    def set_Book_category(self, category):
            self.category = category

    
    def get_Book_ISBN(self):
            return self.ISBN

    def set_Book_ISBN(self, ISBN):
            self.ISBN = ISBN
    
    def get_Book_price(self):
            return self.price

    def set_Book_price(self, price):
            self.price = price

    def get_Book_quantity(self):
            return self.quantity

    def set_Book_quantity(self, quantity):
            self.quantity = quantity


    def get_Book_borrowable(self):
            return self.borrowable

    def set_Book_borrowable(self, borrowable):
            self.borrowable = borrowable 

    def get_Book_buyable(self):
            return self.buyable

    def set_Book_buyable(self, buyable):
            self.buyable = buyable 

    def to_dict(self):
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