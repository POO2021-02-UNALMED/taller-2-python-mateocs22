class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color in ("rojo", "verde", "amarillo", "negro", "blanco")):
            self.color= color


class Auto:
    cantidadCreados= 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
            c= 0
            for i in self.asientos:
                if type(i) == type(Asiento):
                    c += 1 
            return c

    def verificarIntegridad(self):
        rc= "Auto original"
        re= "Las piezas no son originales"
        for i in self.asientos:
            if(i !=  None and i.registro != self.registro):
                return re
        if (self.registro == self.motor.registro):
            return rc
        else:
            return re

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros= numeroCilindros
        self.tipo= tipo
        self.registro= registro

    def cambiarRegistro(self, registro):
        self.registro= registro

    def asignarTipo(self, tipo):
        if tipo in ("electrico", "normal"):
            self.tipo= tipo
