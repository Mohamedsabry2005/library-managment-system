from Models.Human import Human
from Models.Order import Order


class Client(Human):
     
     def __init__(self,phone_num,id,name,age,id_num ,address , reading_history ,orders_num ):
        super(Client, self).__init__(id=id, name=name, age=age, id_num=id_num , phone_num = phone_num , address =address)
        self.reading_history = reading_history 
        self.orders_num = orders_num 


     def get_reading_history(self):
        return self.reading_history

    # Setter for reading_history
     def set_reading_history(self, new_history):
        if isinstance(new_history, list) and all(isinstance(order, Order) for order in new_history):
            self.reading_history = new_history
        else:
            raise ValueError("Reading history must be a list of Order objects.")

    # Optionally, add methods to add/remove individual orders
     def add_to_reading_history(self, order):
        if isinstance(order, Order):
            self._reading_history.append(order)
        else:
            raise ValueError("Only Order objects can be added to the reading history.")
     def get_orders_num(self):
         return self.orders_num

     def set_orders_num(self, orders_num):
         self.orders_num = orders_num

     def to_dict(self):
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
     

