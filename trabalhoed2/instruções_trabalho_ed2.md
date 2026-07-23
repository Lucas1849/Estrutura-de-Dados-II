# Tema: Sistema de Gerenciamento de Livros de uma Biblioteca

Uma biblioteca universitária deseja manter um sistema eficiente para armazenar e consultar seus livros. Como o acervo cresce constantemente, a busca deve permanecer rápida independentemente da ordem em que os livros são cadastrados. Para isso, será utilizada uma Árvore AVL, garantindo o balanceamento automático após inserções e remoções.

Cada livro será identificado por uma chave: código (do tipo inteiro).

 
class Livro:
    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
 
A árvore deverá utilizar o código do livro como chave de ordenação.

Objetivos
Desenvolver, em Python, uma implementação completa de uma Árvore AVL capaz de armazenar objetos do tipo Livro, mantendo a árvore balanceada automaticamente.

Não é permitido utilizar bibliotecas prontas para árvores.

Funcionalidades Obrigatórias
## Implementar a inserção de um novo livro na árvore AVL. A implementação deverá:

inserir obedecendo a propriedade da árvore binária de busca;
atualizar as alturas dos nós;
calcular o fator de balanceamento;
realizar as rotações necessárias.
## Implementar uma função que receba um código e retorne o livro correspondente. Caso o livro não exista, informar adequadamente.

## Implementar a remoção de um livro pelo código. Após a remoção a árvore deverá permanecer balanceada. Todos os casos devem ser tratados:

folha;
um filho;
dois filhos.
## Implementar um percurso em ordem (in-order) que apresente os livros ordenados pelo código.

## Implementar uma função que receba dois códigos: codigoInicial, codigoFinal e exiba todos os livros cujos códigos pertencem ao intervalo informado. A solução deve explorar a estrutura da árvore, evitando visitar ramos que certamente não possuem elementos do intervalo.

## Implementar funções que retornem: altura da árvore; quantidade de livros armazenados; quantidade de rotações à esquerda realizadas; quantidade de rotações à direita realizadas.

 
# No programa principal:

inserir pelo menos 100 livros com códigos gerados aleatoriamente;
realizar pelo menos 20 buscas;
remover 20 livros;
apresentar:
altura final da árvore;
número total de rotações à esquerda;
número total de rotações à direita;
quantidade de elementos restantes.
Ao final, escrever um relatório (entregar em PDF) discutindo:

por que a AVL mantém buscas eficientes;
em quais situações ocorreram mais rotações;
quais vantagens ela apresenta em relação a uma árvore binária de busca comum.
Organização do Código e Instruções:
O programa deverá ser dividido em classes: main, Livro, AVL, No. A classe AVL deverá conter todas as operações sobre a árvore