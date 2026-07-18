from avl import AvlTree
from livro import Livro

def main():
    palavras = AvlTree()
    nome_documento_livros = 'trabalhoed2/acervo.txt' #Note, aqui a escolha txt é puramente pela natureza do trabalho e indicação no campo
                                         # de entrega do moodle. Poderia ser um JSON, por exemplo.
    documentar_livro(nome_documento_livros)
    
    
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


#antes fazer um texto como uma lista
def insere_na_arvore(arquivo_path, arvore):
    with open(arquivo_path,'r') as arquivo:
        texto = arquivo.readlines()
        for t in range(len(texto)):
            arvore.insere(retorna_palavras(texto[0]))
        
       
def retorna_palavras(texto_completo):
    for i in range(len(texto_completo)):
        for p in texto_completo[i].split(" "):
            return p[:]


main()