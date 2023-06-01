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


class MinimaDistancia(List[Patron]):
    def __init__(self):
        self.medias = None
        self.eficacia = None

    def entrenar(self, aux: List[Patron]) -> None:
        # calcular las medias de cada clase
        self.medias = []
        # recorrer la lista de entrenamiento
        for p in aux:
            # verificar si existe elemento representativo
            if not self.existeRepresentativo(self.medias, p):
                # tiene que generar el representativo y acumular
                self.generarMediaRepresentativa(p, self.medias)
        # iterar las medias
        for pr in self.medias:
            pr.promediar()

    def existeRepresentativo(self, medias: List[PatronRepresentativo], p: Patron) -> bool:
        # recorrer la medias y verificar si existe alguna con un mismo nombre de clase que "p"
        for media in medias:
            if media.getClase() == p.getClase():
                media.acumular(p)
                return True
        return False

    def generarMediaRepresentativa(self, p: Patron, medias: List[PatronRepresentativo]) -> None:
        # generar por referencia una media representativa
        aux = PatronRepresentativo([0] * len(p.getVector()), p.getClase())
        aux.acumular(p)
        medias.append(aux)

    def clasificar(self, aux: Patron) -> None:
        # generar una hipotesis
        i = 0
        di = Herramientas.distanciaEuclidiana(self.medias[i], aux)
        for x in range(1, len(self.medias)):
            j = Herramientas.distanciaEuclidiana(self.medias[x], aux)
            if j < di:
                di = j
                i = x
        # aux.setClase(self.medias[i].getClase())
        aux.setClaseResultante(self.medias[i].getClase())

    def clasificarConjunto(self, conjunto: List[Patron]) -> None:
        # para cada elemento de la coleccion se genera un proceso
        # de clasificación
        self.eficacia = 0
        c = 0
        for aux in conjunto:
            self.clasificar(aux)
            # if(aux.getClase().equals(aux.getClaseResultante()))c++;
        # calcular la eficacia del clasificador
        # proceso iterativo de a coleccion "conjunto"
        # h = (double)100/conjunto.size();
        # this.eficacia = h*c;
        # mandar llamar a MC

        print()

    def getEficacia(self) -> float:
        return self.eficacia