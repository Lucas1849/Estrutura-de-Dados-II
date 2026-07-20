from avl import AvlTree
from livro import Livro

def main():
    codigos = AvlTree()
    nome_documento_livros = 'trabalhoed2/acervo.txt' #Note, aqui a escolha txt é puramente pela natureza do trabalho e indicação no campo
                                         # de entrega do moodle. Poderia ser um JSON, por exemplo.
    documentar_livro(nome_documento_livros)
    insere_na_arvore(nome_documento_livros,codigos)
    codigos.emOrdem()
    
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
            acervo.write(cadastro_livro.__str__())

#Segundo passo seria, tá eu tenho os livros documentados em algum lugar.
#Agora eu tenho que ler esse arquivo e pegar apenas os códigos transformando-os para inteiros
#Na hora de devolver as informações do livro no __str__ foi utilizado ";" estrategicamente para facilitar o split()
def insere_na_arvore(arquivo_path, arvore):
    with open(arquivo_path,'r') as arquivo:
        texto = arquivo.readlines()
        for info in texto:
            arvore.insere(int(info.split(";")[0]))

main()