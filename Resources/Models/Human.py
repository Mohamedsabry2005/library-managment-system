class Human(object):
        def __init__(self,id,name,age,id_num,address,phone_num):
                self.__id = id
                self.name = name
                self.age = age
                self.__id_num = id_num
                self.address = address
                self.phone_num= phone_num

        def get_id(self):
            return self.__id

        def set_id(self,id):
            self.__id=id

        def get_name(self):
            return self.name

        def set_name(self,name):
            self.name=name

        def get_age(self):
            return self.age

        def set_age(self, age):
            self.age = age

        def get_id_num(self):
            return self.__id_num

        def set_id_num(self, id_num):
            self.__id_num = id_num

        def get_address(self):
            return self.address

        def set_address(self,address):
            self.address = address
        def get_phone_num(self):
            return self.phone_num

        def set_phone_num(self,phone_num):
            self.phone_num = phone_num

        def to_dict(self):
             return {"phone_number": self.phone_num,"id": self.__id,"name": self.name,"age": self.age,"id_num": self.__id_num,"address": self.address,}