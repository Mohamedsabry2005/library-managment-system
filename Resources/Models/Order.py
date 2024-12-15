
class Order:
    def __init__(self,id,date,client_id,book_id,status,order_type , price=None):
        self.__id=id
        self.date=date
        self.__client_id=client_id
        self.__book_id=book_id
        self.status=status
        self.order_type= order_type
        self.price = price if order_type == "buy" else None 


    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def get_book_id(self):
            return self.__book_id

    def set_book_id(self, book_id):
            self.__book_id = book_id

    def get_status(self):
         return self.status

    def set_status(self, status):
         self.status = status

    def get_order_type(self):
         return self.order_type

    def set_order_type(self, order_type):
         self.order_type = order_type

    def get_price(self):
        return self.price
    
    def set_price(self , price):
        self.price = price


    def to_dict(self):
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
    # We use @classmethod for the from_dict method in a class like Order because it allows us to create new
    #  instances of the class (Order in this case) using the class itself as a reference (cls), rather than
    #  requiring an existing instance of the class. This approach is especially useful for factory methods,
    #  like from_dict, which construct and return new objects from a given input
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            date=data["date"],
            client_id=data["client_id"],
            book_id=data["book_id"],
            status=data["status"],
            order_type=data["order_type"],
            price=data.get("price")  # Use `.get` for optional fields
        )
    
    