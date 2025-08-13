class Cookie:
    def __init__(self, name, price, weight):
        try:
            #Encontré una palabra clave "raise" que me permite lanzar una excepción por mi cuenta
            #https://ellibrodepython.com/excepciones-try-except-finally
            if name == '': raise NameError("El nombre de la galleta no puede estar vacío")
            if price <= 0: raise ValueError("El precio de la galleta debe ser mayor que 0")
            if weight <= 0: raise ValueError("El peso de la galleta debe ser mayor a 0")
            self.nombre = name
            self.precio = price
            self.weight = weight
        except Exception as e:
            print(f"Error al crear Producto: {e}")

class Chocolate_chips(Cookie):
    def __init__(self, name, price, weight, chips):
        # Uso de super() para heredar los atributos del objeto Padre
        #https://ellibrodepython.com/herencia-en-python
        super().__init__(name, price, weight)
        try:
            if chips <= 0: raise ValueError("La galleta debe de tener al menos 1 chispa de chocolate")
            self.chips = chips
        except Exception as e:
            print(f"Error al crear Producto: {e}")

co = Cookie('name', 0,-2)