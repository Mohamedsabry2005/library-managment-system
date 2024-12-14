from Models.Human import Human


class Librarian(Human):
    def __init__(self,id,name,age,id_num,address,phone_num ,emp_type):
        super(Librarian, self).__init__(id=id,name=name,age = age,id_num=id_num , address = address , phone_num = phone_num)
        self.emp_type = emp_type
    


    def get_emp_type(self):
        return self.emp_type
    

    def set_emp_type(self,emp_type):
         self.emp_type=emp_type

    def to_dict(self):
        return {
            "id": self.get_id(),
            "name": self.name,
            "age": self.age,
            "id_num": self.get_id_num(),
            "address": self.address,
            "phone_num": self.phone_num,
            "emp_type": self.emp_type,
        }