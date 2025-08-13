class Cookie:
    def __init__(self, name, price, weight):
        try:
            #Encontré una palabra clave "raise" que me permite lanzar una excepción por mi cuenta
            if name == '': raise NameError("El nombre de la galleta no puede estar vacío")
            if price <= 0: raise ValueError("El precio de la galleta debe ser mayor que 0")
            if weight <= 0: raise ValueError("El peso de la galleta debe ser mayor a 0")
            self.nombre = name
            self.precio = price
            self.weight = weight
        except Exception as e:
            print(f"Error al crear Producto: {e}")

co = Cookie('name', 0,-2)