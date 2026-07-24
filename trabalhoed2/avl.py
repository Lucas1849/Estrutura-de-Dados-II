from no import NO
class AvlTree:
    def __init__(self):
        self.__raiz = None
        self.__rotacoesEsq = 0
        self.__rotacoesDir = 0

    def elemRaiz(self):
        if (self.__raiz != None):
           return self.__raiz.info
        else:
           return None

    def __altura(self, no):
        if(no == None):
            return -1
        else:
            return no.altura

    #Versão pública do __altura, usando a raiz da árvore, pra não precisar expor o nó pra quem
    #está usando a classe de fora
    def altura(self):
        return self.__altura(self.__raiz)

    #Conta quantos nós existem na árvore percorrendo em ordem, sem depender de nenhum
    #atributo guardado à parte
    def __quantidadeElementos(self, raiz):
        if(raiz == None):
            return 0
        else:
            return 1 + self.__quantidadeElementos(raiz.esq) + self.__quantidadeElementos(raiz.dir)

    def quantidadeElementos(self):
        return self.__quantidadeElementos(self.__raiz)

    def rotacoesEsquerda(self):
        return self.__rotacoesEsq

    def rotacoesDireita(self):
        return self.__rotacoesDir

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.esq) - self.__altura(no.dir))    

    def __maior(self, x, y):
        if(x > y):
            return x
        else:
            return y

    def __RotacaoLL(self, A):
        #print('RotacaoLL: ',A.info);
        self.__rotacoesDir = self.__rotacoesDir + 1
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.__maior(self.__altura(A.esq),self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq),A.altura) + 1
        #A = B
        return B

    def __RotacaoRR(self, A):
        #print('RotacaoRR: ',A.info);
        self.__rotacoesEsq = self.__rotacoesEsq + 1
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__altura(A.esq),self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir),A.altura) + 1
        #A = B
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        A = self.__RotacaoLL(A)
        return A
        
    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        A = self.__RotacaoRR(A)
        return A

    def __insereValor(self,atual,valor):
        if(atual == None): # árvore vazia ou nó folha
            novo = NO(valor)
            return novo
        else:
            
            if(valor < atual.info):
                atual.esq = self.__insereValor(atual.esq, valor)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(valor < atual.esq.info):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
            elif (valor > atual.info):
                atual.dir = self.__insereValor(atual.dir, valor)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(valor > atual.dir.info):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)
            else: return
            atual.altura = self.__maior(self.__altura(atual.esq),self.__altura(atual.dir)) + 1
            return atual                

    def insere(self, valor):
        if(self.buscafreq(valor)):
            return False #valor já existe na árvore
        else:
            self.__raiz = self.__insereValor(self.__raiz, valor)
            return True

    def buscafreq(self, valor):
        if(self.__raiz == None):
            return False

        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                atual.freq = atual.freq + 1
                return True
            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq
        return False

    def busca(self, valor):
        if(self.__raiz == None):
            return False

        atual = self.__raiz
        while(atual != None):
            if(valor == atual.info):
                return True

            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq

        return False

    #Diferente de busca(), que só confirma se existe, essa função devolve o próprio livro encontrado
    #ou None quando o código não está cadastrado, pra quem chamar poder tratar os dois casos
    def buscaLivro(self, codigo):
        if(self.__raiz == None):
            return None

        atual = self.__raiz
        while(atual != None):
            if(codigo == atual.info.codigo):
                return atual.info

            if(codigo > atual.info.codigo):
                atual = atual.dir
            else:
                atual = atual.esq

        return None

    #Percorre em ordem, mas só desce pros ramos que podem ter algo dentro do intervalo,
    #assim evita visitar a árvore inteira quando o intervalo é pequeno
    def __buscaIntervalo(self, raiz, codigoInicial, codigoFinal, encontrados):
        if(raiz == None):
            return

        if(raiz.info.codigo > codigoInicial):
            self.__buscaIntervalo(raiz.esq, codigoInicial, codigoFinal, encontrados)

        if(codigoInicial <= raiz.info.codigo <= codigoFinal):
            encontrados.append(raiz.info)

        if(raiz.info.codigo < codigoFinal):
            self.__buscaIntervalo(raiz.dir, codigoInicial, codigoFinal, encontrados)

    def buscaIntervalo(self, codigoInicial, codigoFinal):
        encontrados = []
        self.__buscaIntervalo(self.__raiz, codigoInicial, codigoFinal, encontrados)
        return encontrados

    def __procuraMenor(self, atual):
        no1 = atual
        no2 = atual.esq
        while(no2 != None):
            no1 = no2
            no2 = no2.esq
        return no1

    def __removeValor(self, atual, valor):
        if(atual.info == valor): #achou o nó a ser removido
            if(atual.esq == None or atual.dir == None): # nó tem 1 filho ou nenhum
                if(atual.esq != None):
                    atual = atual.esq
                else:
                    atual = atual.dir
                
            else: # nó tem 2 filhos
                temp = self.__procuraMenor(atual.dir)
                atual.info = temp.info
                atual.dir = self.__removeValor(atual.dir, atual.info)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(self.__altura(atual.esq.dir) <= self.__altura(atual.esq.esq)):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
                        
            if(atual != None):
                atual.altura = self.__maior(self.__altura(atual.esq),self.__altura(atual.dir)) + 1

        else:# procura o nó a ser removido
            if(valor < atual.info):
                atual.esq = self.__removeValor(atual.esq, valor)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(self.__altura(atual.dir.esq) <= self.__altura(atual.dir.dir)):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)                        
            else:
                atual.dir = self.__removeValor(atual.dir, valor)
                if(self.__fatorBalanceamento(atual) >= 2):
                    if(self.__altura(atual.esq.dir) <= self.__altura(atual.esq.esq)):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            atual.altura = self.__maior(self.__altura(atual.esq),self.__altura(atual.dir)) + 1

        return atual    
    
    def remove(self, valor):
        if(self.__raiz == None or not self.busca(valor)):
            return False #árvore vazia ou valor não existe na árvore
        else:
            self.__raiz = self.__removeValor(self.__raiz, valor)
            return True

    #A árvore só sabe remover recebendo um Livro (pra comparar com __lt__/__eq__), então
    #essa função busca o livro pelo código e manda ele mesmo pra remove(), evitando que quem
    #chama de fora precise montar um Livro só pra conseguir remover
    def removeCodigo(self, codigo):
        livro = self.buscaLivro(codigo)
        #Aqui a implementação do __equal__ trouxe dor de cabeça, pois == chama __equal__ independente do caso quando
        #relacionado a classe Livro, o que fez com que gerasse erros e eu tive que procurar uma forma de comparar se é None
        #de um outra forma. Usando o "is None" foi a alternativa que resolvi usar.
        if(livro is None):
            return False
        else:
            return self.remove(livro)

    def __preOrdem(self,raiz):
        if(raiz != None):
            print("(",raiz.info.codigo, raiz.freq,")")
            self.__preOrdem(raiz.esq)
            self.__preOrdem(raiz.dir)

    def preOrdem(self):
        if(self.__raiz != None):
            self.__preOrdem(self.__raiz)

    def __emOrdem(self,raiz):
        if(raiz != None):            
            self.__emOrdem(raiz.esq)
            print("(",raiz.info.codigo, raiz.freq,") ", end=' ')
            self.__emOrdem(raiz.dir)

    def emOrdem(self):
        if(self.__raiz != None):
            self.__emOrdem(self.__raiz)
        
    def __posOrdem(self,raiz):
        if(raiz != None):            
            self.__posOrdem(raiz.esq)
            self.__posOrdem(raiz.dir)
            print("(",raiz.info.codigo, raiz.freq,")")

    def posOrdem(self):
        if(self.__raiz != None):
            self.__posOrdem(self.__raiz)


    def emNivel(self):
        h = self.__altura(self.__raiz)
        for i in range(0, h+1):
            print('\n - Nivel ',i)
            self.__imprimeNivel(self.__raiz, i)
            
 
 
    # Imprimir elementos que estão no mesmo nível
    def __imprimeNivel(self, raiz, nivel):
        if raiz is None:
            return
        if nivel == 0:
            print("(",raiz.info.codigo, raiz.freq,") ", end=" ")
        elif nivel > 0:
            self.__imprimeNivel(raiz.esq, nivel-1)
            self.__imprimeNivel(raiz.dir, nivel-1)


    def rotacoes(self):
        if self.__raiz is None:
            return
        else:
            print('\n\n- Rotacoes a Esquerda: ',self.__rotacoesEsq)
            print('- Rotacoes a Direita: ',self.__rotacoesDir)