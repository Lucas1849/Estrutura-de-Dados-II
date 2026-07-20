class NO:
    def __init__(self, info):
        self.info = info
        self.esquerda = None
        self.direita = None

    def __repr__(self):
        return f'{self.esquerda and self.esquerda.info} <- {self.info}  -> {self.direita and self.direita.info}\n'

class ArvBin:
    def __init__(self):
        self.__raiz = None

    def insere(self, valor):
        novo = NO(valor)

        if self.__raiz == None:
            self.__raiz = novo
        else:
            atual = self.__raiz
            ant = None
            while atual != None:
                ant = atual
                if valor > atual.info:
                    atual = atual.direita
                else:
                    atual = atual.esquerda
            if valor > ant.info:
                ant.direita = novo
            elif valor < ant.info:
                ant.esquerda = novo
            else:
                return False
            
    def emOrdem(self):
        if self.__raiz == None:
            return 
        self._emOrdem(self.__raiz)

    def _emOrdem(self, raiz):
        if raiz != None:
            self._emOrdem(raiz.esquerda)
            print(raiz.info)
            self._emOrdem(raiz.direita)

    def preOrdem(self):
        if self.__raiz == None:
            return
        self._preOrdem(self.__raiz)

    def _preOrdem(self, raiz):
        if raiz != None:
            print(raiz.info)
            self._preOrdem(raiz.esquerda)
            self._preOrdem(raiz.direita)

    def posOrdem(self):
        if self.__raiz == None:
            return
        self._posOrdem(self.__raiz)

    def _posOrdem(self,raiz):
        if raiz != None:
            self._posOrdem(raiz.esquerda)
            self._posOrdem(raiz.direita)
            print(raiz.info)

    def contagem(self):
        if self.__raiz == None:
            return 0
        self._contagem(self.__raiz)

    def _contagem(self, raiz):
        if raiz != None:
            self._contagem(raiz.esquerda)
            self._contagem(raiz.direita)
            return "feito"
        

arv1 = ArvBin()
arv1.insere(10)
arv1.insere(15)
arv1.insere(1)
arv1.contagem()
