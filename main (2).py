# наследование 
class User:
    def __init__(self, fullname,login,password,email):
        self._fullname = fullname  
        self._login = login 
        self._password = password 
        self._email = email
#геттеры 
    @property
    def fullname(self):
        return self._fullname
    @property
    def login(self):
        return self._login
    @property
    def password(self):
        return self._password
    @property
    def email(self):
        return self._email
    # сеттеры
    @fullname.setter
    def fullname(self, new_fullname):
        self._fullname = new_fullname
        return self._fullname

user = User('ivan','ivan89','1234','ivan89@ivan.ru')

print(user.fullname)
user.fullname = 'ivan ivanov'
# создаем наследник - MANAGER
class Manager(User):
    def __init__(self, fullname,login,password,email,departament):
        super().__init__(fullname,login,password,email)
        self._departament = departament
#геттеры
        @property 
        def departament(self):
            return self.departament
        @property
        def password(self):
            return self.password

        @password.setter
        def password(self,new_password):
            self._password = new_password
            return self.fullname
            
manager = Manager('peter','petya99','petya@petya.petya','бухгалтерия','pedil')
print(manager.email)
manager.fullname = 'peter petrow'
print(manager.fullname)
manager._password = '4321'
print(manager.password)
        # наследование метода 
class Root(Manager):
    def __init__(self,fullname,login,password,email,departament):
        super().__init__(fullname,login,password,email,departament)
    #departament
    @login.setter
    def login(self,new_login):
        self._login = new_login
        return self.login
    @email.setter
    def email(self,new_email):
        self._email
        @departament.setter
        def departament(self,new_departament):
            self._departament = new_departament
            return self.departament

class Main:
    def __init__(self, item_1,item_2):
        self.item_1 = item_1
        self.item_2 = item_2
    def name(self):
        print "вывод атрибута"
        
            
            
        
        
            
        