import numpy as np
import matplotlib.pyplot as plt
import pandas


class Patron:

    def __init__(self, vector, clase):
        self.vector = vector
        self.clase = clase
        self.claseResultante = "Desconocida"

    def __init__(self, n):
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

    def acumular(self, aux):
        # iterate through the characteristic vector to accumulate
        for i in range(len(super().getVector())):
            super().getVector()[i] += aux.getVector()[i]
        self.acumulador += 1

    def promediar(self):
        for i in range(len(super().getVector())):
            super().getVector()[i] /= self.acumulador

