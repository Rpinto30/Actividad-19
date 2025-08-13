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
    def describe(self): print(f"    > El relleno de tu galleta es: {self.filling_type}")

class Cookie:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def show_inf(self):
        print(f"Galleta: {self.name} (Precio: Q{self.price} | Pesa: {self.weight} kg)")

class CookieChips(Cookie):
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
        print(f"Galleta: {self.name} (Precio: Q{self.price} | Pesa: {self.weight} Kg)")
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
        # Se regresa una tupla con las tres variables, ya solo para llamar el metdoto y no escribir otra vez el codigo
        return _name, _price, _weight

    def add_cookie(self):
        print("-" * 20 + "AÑADIR GALLETA" + "-" * 20)
        name, price, weight = self.consult_cookie()
        self.cookies.append(Cookie(name, price, weight)) #sE AÑADE A LA LISTA EL COOKIE BASICO

    def add_cookie_chips(self):
        print("-" * 20 + "AÑADIR GALLETA CON CHISPAS" + "-" * 20)
        name, price, weight = self.consult_cookie()
        while True:
            chips = input_number("Ingresa la cantidad de chispas de tu galleta: ")
            if chips > 0: break
            else: print("\nLo siento, tu gallta debe de tener una cantidad de chispas mayor a 0")
        #Se añade a ka kusta el cookiechips
        self.cookies.append(CookieChips(name, price, weight, chips))

    def add_cookie_filling(self):
        print("-" * 20 + "AÑADIR GALLETA CON RELLENO" + "-" * 20)
        name, price, weight = self.consult_cookie()
        while True:
            filling = input("Ingresa el tipo de relleno de tu galleta: ")
            if filling != '': break
            else: print("\nLo siento, tu gallta debe de tener un tipo de relleno")
        #Se añade a la lista el fillingcookie
        self.cookies.append(FillingCookie(name, price, weight, filling))

    def list_cookies(self):
        if self.cookies:
            print("-"*20+"GALLETAS"+"-"*20)
            for num, i in enumerate(self.cookies,1):
                # Se llama a show_inf(), en caso de las galletas rellenas, el mismo show_inf() llama a otro metodo para mostrar el relleno
                print(f"{num}) ", end='') #Se imprime la numeración y luego la info de las galletas
                i.show_inf()
        else: print("\n Lo sentimos, no hay galletas registradas")

    def find_cookie(self):
        if self.cookies:
            print("-" * 20 + "BUSCAR GALLETA" + "-" * 20)
            name = input("Ingresa el nombre de la galleta que quieres buscar: ").lower()
            for i in self.cookies:
                if i.name.lower() == name:
                    i.show_inf() #Si la galleta se encuentra se llama a su medotod show_inf()
                    break
            else:
                print(f"Lo sentimos, no encontramos la galleta {name}")
        else: print("\n Lo sentimos, no hay galletas registradas")

    def del_cookie(self):
        print("-" * 20 + "BUSCAR GALLETA" + "-" * 20)
        name = input("Ingresa el nombre de la galleta que quieres buscar: ").lower() #Para evitar que no lo encuentre solo por las mayusculas
        for i in self.cookies:
            if i.name.lower() == name:
                self.cookies.remove(i) #Se remueve de la lista solo si el elemento fue encontrado
                print("La galleta fue removida correctamente!")
                break
        else:
            print(f"Lo sentimos, no encontramos la galleta {name}")


sys_cookie = CookiesSystem()


while True:
    try:
        print("-"*20+"COOKIES"+"-"*20)
        print("1) Registrar galleta basica\n2) Registrar galleta con chispas\n3) Regsitrar galleta rellena\n4) Listar galletas\n5) Buscar por nombre\n6) Eliminar galleta\n7) Salir")
        op = input("Ingresa una opción: ")
        match op:
            case '1': sys_cookie.add_cookie()
            case '2': sys_cookie.add_cookie_chips()
            case '3': sys_cookie.add_cookie_filling()
            case '4': sys_cookie.list_cookies()
            case '5': sys_cookie.find_cookie()
            case '6': sys_cookie.del_cookie()
            case '7':
                print("\nNos vemos!")
                break
            case _: print("\nPorfavor, elige una opción valida")
    except Exception as e:
        print("\nVaya... parece que hubo un error inesperado, devolviendo al menú principal")
        print("Error: ", e)