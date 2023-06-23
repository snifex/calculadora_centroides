from decimal import *
from math import pi
from TipoFigura import *

class Figura():
    def __init__(self, x_lado: float, y_lado: float, tipo_figura : int) -> None:
        self._x_lado = Decimal(x_lado) # Base
        self._y_lado = Decimal(y_lado) # Altura
        self._tipo_figura = TipoFigura(tipo_figura)
        self._area_x = Decimal()
        self._area_y = Decimal()
        self._area = Decimal()

    @property
    def area(self)-> Decimal:
        return self._area
    
    @property
    def tipo_figura(self)-> str:
        return self._tipo_figura.name
    
    @property
    def x_lado(self)-> Decimal:
        return self._x_lado
    
    @property
    def y_lado(self) -> Decimal:
        return self._y_lado
    
    @property
    def area_x(self)-> Decimal:
        return self._area_x
    
    @property
    def area_y(self)-> Decimal:
        return self._area_y
    
    @area.setter
    def area(self, nueva_area: Decimal) -> None:
        if not isinstance(nueva_area, Decimal):
            raise ValueError("area must be Decimal")
        self._area = nueva_area

    @x_lado.setter
    def x_lado(self, nuevo_x_lado: Decimal) -> None:
        if not isinstance(nuevo_x_lado, Decimal):
            raise ValueError("x_lado must be Decimal")
        self._x_lado = nuevo_x_lado

    @y_lado.setter
    def y_lado(self, nuevo_y_lado:Decimal) -> None:
        if not isinstance(nuevo_y_lado, Decimal):
            raise ValueError("y_lado must be Decimal")
        self._y_lado = nuevo_y_lado

    @area_x.setter
    def area_x(self, nueva_area_x: Decimal) -> None:
        if not isinstance(nueva_area_x, Decimal):
            raise ValueError("area_x must be Decimal")
        self._area_x = nueva_area_x

    @area_y.setter
    def area_y(self, nueva_area_y: Decimal) -> None:
        if not isinstance(nueva_area_y, Decimal):
            raise ValueError("area_y must be Decimal")
        self._area_y = nueva_area_y


    def get_centroide(self, valor_anterior_x = 0, valor_anterior_y = 0) -> dict[str,Decimal]:
        resultado_centroide = {"x_coord": Decimal("0"), "y_coord": Decimal("0")}
        if self._tipo_figura == TipoFigura.RECTANGULO:
            #Para el calculo del centroide es mitad y mitad
            resultado_centroide["x_coord"] = Decimal((self._x_lado + valor_anterior_x) / Decimal(2))
            resultado_centroide["y_coord"] = Decimal((self._y_lado + valor_anterior_y) / Decimal(2))

        elif self._tipo_figura == TipoFigura.TRIANGULO:
            #Triangulo x=h/3 y=a/3
            resultado_centroide["x_coord"] = Decimal((self._x_lado + valor_anterior_x) / Decimal(3))
            resultado_centroide["y_coord"] = Decimal((self._y_lado + valor_anterior_y) / Decimal(3))

        elif self._tipo_figura == TipoFigura.SEMI_CIRCUNFERENCIA: 
            #Semicirculo x = 0 y = 4r/3pi
            if self._x_lado > self._y_lado:
                resultado_centroide["y_coord"] = Decimal((4 * ((self._x_lado + valor_anterior_y) / 2))/(Decimal(3 * pi)))
            else:
                resultado_centroide["x_coord"] = Decimal((4 * ((self._y_lado + valor_anterior_x)/ 2))/(Decimal(3 * pi)))

        elif self._tipo_figura == TipoFigura.CUARTO_CIRCUNFERENCIA:
            resultado_centroide["x_coord"] = Decimal((4 * self._x_lado + valor_anterior_x) / (Decimal(3 * pi)))
            resultado_centroide["y_coord"] = Decimal((4 * self._y_lado + valor_anterior_y) / (Decimal(3 * pi)))

        elif self._tipo_figura == TipoFigura.SEMI_ELIPSE:
            if self._x_lado > self._y_lado:
                resultado_centroide["y_coord"] = Decimal((4 * (self._x_lado + valor_anterior_y))/(Decimal(3 * pi)))
            else:
                resultado_centroide["x_coord"] = Decimal((4 * (self._y_lado + valor_anterior_x))/(Decimal(3 * pi)))

        elif self._tipo_figura == TipoFigura.CUARTO_ELIPSE:
            resultado_centroide["x_coord"] = Decimal(( 4 * self._x_lado + valor_anterior_x)/(Decimal(3 * pi)))
            resultado_centroide["y_coord"] = Decimal(( 4 * self._y_lado + valor_anterior_y)/( Decimal(3 * pi) ))

        elif self._tipo_figura == TipoFigura.PARABOLA:
            resultado_centroide["x_coord"] = Decimal( ( 3 * self._x_lado + valor_anterior_x) / 8)
            resultado_centroide["x_coord"] = Decimal(Decimal((3/5)) * self._y_lado + valor_anterior_y)

        elif self._tipo_figura == TipoFigura.EJUTA:
            resultado_centroide["x_coord"] = Decimal(Decimal((3/4)) * self._x_lado + valor_anterior_x)
            resultado_centroide["y_coord"] = Decimal(Decimal((3/10)) * self._y_lado + valor_anterior_y)

        return resultado_centroide
    
    @staticmethod
    def get_area(self) -> Decimal:
        area_semi_circ = lambda x : Decimal( (Decimal(pi) * x ** Decimal(2)) / 2)
        result = Decimal(0)
        areas={
            TipoFigura.RECTANGULO: Decimal(self._x_lado * self._y_lado),
            TipoFigura.TRIANGULO: Decimal((self._x_lado * self._y_lado) / 2),
            TipoFigura.SEMI_CIRCUNFERENCIA: self._x_lado > self._y_lado if area_semi_circ(self._x_lado) else area_semi_circ(self._y_lado),
            TipoFigura.CUARTO_CIRCUNFERENCIA: Decimal((Decimal(pi) * self._x_lado ** Decimal(2)) / Decimal(4)),
            TipoFigura.SEMI_ELIPSE: Decimal((self._x_lado * self._y_lado * Decimal(pi)) / 2),
            TipoFigura.CUARTO_ELIPSE: Decimal((self._x_lado * self._y_lado * Decimal(pi)) / 4),
            TipoFigura.PARABOLA: Decimal(( 2 * self._x_lado * self._y_lado) / 3),
            TipoFigura.EJUTA: Decimal(( self._x_lado * self._y_lado ) / 3)
        }


        if self._tipo_figura in areas.keys():
            result = areas[self._tipo_figura]
        
        return result
    