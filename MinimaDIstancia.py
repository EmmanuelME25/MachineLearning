import numpy as np
import matplotlib.pyplot as plt
import pandas
import math


class Patron:

    def Patron(self, vector, clase):
        self.vector = vector
        self.clase = clase
        self.claseResultante = "Desconocida"

    def Patron(self, n):
        self.vector = [0.0] * n
        self.clase = "Desconocida"
        self.claseResultante = "Desconocida"

    def getVector(self):
        return self.vector

    def setVector(self, vector):
        self.vector = vector

    def getClase(self):
        return self.clase

    def setClase(self, clase):
        self.clase = clase

    def getClaseResultante(self):
        return self.claseResultante

    def setClaseResultante(self, claseResultante):
        self.claseResultante = claseResultante


class PatronRepresentativo(Patron):
    def __init__(self, vector, clase):
        super().__init__(vector, clase)
        self.acumulador = 0

    def __init__(self, n):
        super().__init__(n)
        self.acumulador = 0

    def acumular(self, aux):
        for x in range(len(self.getVector())):
            self.getVector()[x] += aux.getVector()[x]
        self.acumulador += 1

    def promediar(self):
        for x in range(len(self.getVector())):
            self.getVector()[x] /= self.acumulador

class Herramientas():
    @staticmethod
    def distanciaEuclidiana(a, b):
        acu = 0
        for x in range(len(a.getVector())):
            res = a.getVector()[x] - b.getVector()[x]
            res *= res
            acu = acu + res
        return math.sqrt(acu)

    @staticmethod
    def calcularDistribucion(media, varianza, c):
        return (1 / (math.sqrt(math.pi * 2 * varianza))) * (
            math.exp(-1 * ((math.pow((c - media), 2)) / (2 * varianza))))

