def input_number(message): #INGRESAR UN NUMERO Y VERIFICAR QUE SU ENTRADA SEA VALIDA
    while True:
        try:
            value = float(input(message))
            break
        except ValueError: print('-'*50+'\n'+"❌"*5+"   Lo siento valor no valido, intenta nuevamente   "+"❌"*5)

    if value == int(value): return int(value)
    else: return value

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
    def __init__(self): self.cookies = []

    def consult_cookie(self):
        while True:
            _name = input("Ingrese el nombre de su galleta: ")
            if _name != '': break
            print("\nLo sentimos, debe agregar un nombre a la galleta, intente de nuevo")

        while True:
            _price = input_number("Ingresa el precio de tu galleta: ")
            if _price >= 0: break
            print("\nEl precio debe ser mayor o igual a 0, intenta de nuevo por favor")

        while True:
            _weight = input_number("Ingresa el peso de tu galleta: ")
            if _weight >= 0: break
            print("\nEl peso debe ser mayor o igual a 0, intenta de nuevo por favor")
        return _name, _price, _weight

    def add_cookie(self):
        name, price, weight = self.consult_cookie()
        self.cookies.append(Cookie(name, price, weight))

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


sys_cookie = CookiesSystem()

sys_cookie.add_cookie()
print(sys_cookie.cookies)