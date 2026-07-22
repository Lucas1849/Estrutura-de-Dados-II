from avl import AvlTree
from livro import Livro

def main():
    codigos = AvlTree()
    nome_documento_livros = 'trabalhoed2/acervo.txt' #Note, aqui a escolha txt é puramente pela natureza do trabalho e indicação no campo
                                         # de entrega do moodle. Poderia ser um JSON, por exemplo.
    documentar_livro(nome_documento_livros)
    devolver_classe_de_cada_linha(nome_documento_livros, codigos)

    codigos.emOrdem()
    print(codigos.elemRaiz())
    print(codigos.elemRaiz().__str__())
    
#Primeiro passo é preciso estruturar como as infomações dos livros serão estruturadas para que sejam cadastrados mais de um 
#livro por vez
def documentar_livro(arquivo_destino):
    with open(arquivo_destino, 'w') as acervo:
        while True:
            quer_cadastrar = input("Deseja cadastrar um livro ? ").capitalize()[0]
            if quer_cadastrar not in "Ss":
                break
            cadastro_livro = Livro(int(input("Código: ")),
                                   str(input("Título: ")),
                                   str(input("Autor: ")),
                                   str(input("Ano: ")))
            acervo.write(f'{cadastro_livro.__str__()}\n')


#Ideia genial: Porque ao invez de eu cadastrar uma classe direto no arquivo eu fazer uma função para pegar as informações do
#arquivo e devolver uma classe, dessa forma eu resolvo o problema da não conseguir pegar as informaçõe do livro

"""def devolver_classe_de_cada_linha(lista):
    classe_livro = Livro(int(lista[0]),
                         lista[1],
                         lista[2],
                         lista[3]
    )
    return classe_livro"""


#Parte do código que deu errado
def devolver_classe_de_cada_linha(arquivo_leitura, arvore):
    with open(arquivo_leitura, "r") as livros:
        for info in livros.readlines():
           classe_livro = Livro(int(info.split(";")[0]),
                                info.split(";")[1],
                                info.split(";")[2],
                                info.split(";")[3])
           arvore.insere(classe_livro)
           

        
"""
Parte do código que não precisou, substituído por readlines()

#Conseguir o tamanho do arquivo para retornar a classe de cada linha
def len_arquivo(arquivo_com_livros):
    with open(arquivo_com_livros, "r") as arquivo:
        total_de_linhas = sum(1 for linhas in arquivo)

    return total_de_linhas"""

#Segundo passo seria, tá eu tenho os livros documentados em algum lugar.
#Agora eu tenho que ler esse arquivo e pegar apenas os códigos transformando-os para inteiros
#Na hora de devolver as informações do livro no __str__ foi utilizado ";" estrategicamente para facilitar o split()
"""def insere_na_arvore(arvore, caminho_arquivo):
    with open(caminho_arquivo, 'r') as livros:
        for linhas in livros.readlines():
            arvore.insere(devolver_classe_de_cada_linha(linhas.split(";")))"""

main()