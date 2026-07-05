from avl import AvlTree

def main():
    palavras = AvlTree()
    caminho_do_arquivo = "trabalhoed2/texto_origem.txt"
    insere_na_arvore(caminho_do_arquivo, palavras)
    

#antes fazer um texte como uma lista
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