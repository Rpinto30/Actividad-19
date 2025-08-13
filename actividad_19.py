class Filling:
    def __init__(self, filling_type): self.filling_type = filling_type
    def describe(self): print(f"El relleno de tu galleta es: {self.filling_type}")

class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class ChocolateChips(Cookie):
    def __init__(self, name, price, weight, chips):
        # Uso de super() para heredar los atributos del objeto Padre
        #https://ellibrodepython.com/herencia-en-python
        super().__init__(name, price, weight)
        self.chips = chips

class FillingCookie(Cookie, Filling):
    def __init__(self, name, price, weight, filling_type):
        Cookie.__init__(self,name,price,weight)
        Filling.__init__(self, filling_type)

    def show_inf(self):
        print(f"La galleta: {self.name} Precio: {self.price} | Pesa: {self.weight}")
        self.describe()

class CookiesSystem:
    def add_cookie(self):
        pass

    def add_cookie_chips(self):
        pass

    def add_cookie_filling(self):
        pass

    def list_cookies(self):
        pass

    def find_cookie(self):
        pass

    def del_cookie(self):
        pass


co = Cookie('', -1,-2)