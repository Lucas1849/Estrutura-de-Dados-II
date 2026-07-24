from avl import AvlTree
from livro import Livro
import random

def main():
    codigos = AvlTree()
    nome_documento_livros = 'trabalhoed2/acervo.txt' #Note, aqui a escolha txt é puramente pela natureza do trabalho e indicação no campo
                                         # de entrega do moodle. Poderia ser um JSON, por exemplo.
    codigos_gerados = gera_livros_aleatorios(100, nome_documento_livros)
    devolver_classe_de_cada_linha(nome_documento_livros, codigos)

    realiza_buscas(codigos, 20, codigos_gerados)
    remove_livros(codigos, 20, codigos_gerados)

    codigos.emOrdem()
    imprime_intervalo(codigos, 100, 200)
    imprime_relatorio_final(codigos)

#Antes o cadastro era feito digitando um por um com input(), mas o trabalho pede pelo menos 100 livros
#com código aleatório, então trocamos a digitação manual por geração automática. random.sample garante
#que não vai sair código repetido, o que já é cuidado por fora do que a árvore faz com duplicata
def gera_livros_aleatorios(quantidade, arquivo_destino):
    codigos_gerados = random.sample(range(1, quantidade * 10), quantidade)
    with open(arquivo_destino, 'w') as acervo:
        for codigo in codigos_gerados:
            livro_gerado = Livro(codigo,
                                 f'Titulo{codigo}',
                                 f'Autor{codigo}',
                                 str(random.randint(1950, 2024)))
            acervo.write(f'{livro_gerado.__str__()}\n')

    return codigos_gerados


#Ideia genial: Porque ao invez de eu cadastrar uma classe direto no arquivo eu fazer uma função para pegar as informações do
#arquivo e devolver uma classe, dessa forma eu resolvo o problema da não conseguir pegar as informaçõe do livro
#Parte do código que deu errado
"""def devolver_classe_de_cada_linha(lista):
    classe_livro = Livro(int(lista[0]),
                         lista[1],
                         lista[2],
                         lista[3]
    )
    return classe_livro"""

def devolver_classe_de_cada_linha(arquivo_leitura, arvore):
    with open(arquivo_leitura, "r") as livros:
        for info in livros.readlines():
           classe_livro = Livro(int(info.split(";")[0]),
                                info.split(";")[1],
                                info.split(";")[2],
                                info.split(";")[3])
           arvore.insere(classe_livro)

#O trabalho pede pelo menos 20 buscas por código. Usamos os próprios códigos que sabemos que foram
#gerados, senão a chance de acertar um código que exista na árvore por sorteio seria baixa
def realiza_buscas(arvore, quantidade, codigos_disponiveis):
    print('\n--- Buscas ---')
    codigos_para_buscar = random.sample(codigos_disponiveis, quantidade)
    for codigo in codigos_para_buscar:
        livro_encontrado = arvore.buscaLivro(codigo)
        if livro_encontrado is not None:
            print(f'Codigo {codigo} encontrado: {livro_encontrado}')
        else:
            print(f'Codigo {codigo} nao encontrado')


#O trabalho pede a remoção de 20 livros. Removendo pelos próprios códigos gerados, garantindo que
#eles de fato existiam na árvore antes de remover
def remove_livros(arvore, quantidade, codigos_disponiveis):
    print('\n--- Remocoes ---')
    codigos_para_remover = random.sample(codigos_disponiveis, quantidade)
    for codigo in codigos_para_remover:
        removeu = arvore.removeCodigo(codigo)
        print(f'Remocao do codigo {codigo}: {"sucesso" if removeu else "falhou"}')

#buscaIntervalo devolve só a lista de livros, então quem imprime é quem chamou, aqui no main
def imprime_intervalo(arvore, codigoInicial, codigoFinal):
    print(f'\n--- Livros com codigo entre {codigoInicial} e {codigoFinal} ---')
    livros_no_intervalo = arvore.buscaIntervalo(codigoInicial, codigoFinal)
    if len(livros_no_intervalo) == 0:
        print('Nenhum livro encontrado nesse intervalo')
    else:
        for livro in livros_no_intervalo:
            print(livro)


#Junta as informações finais pedidas no enunciado: altura, rotações à esquerda/direita e
#quantidade de elementos restantes depois das remoções
def imprime_relatorio_final(arvore):
    print('\n--- Relatorio final ---')
    print('Altura da arvore:', arvore.altura())
    print('Rotacoes a esquerda:', arvore.rotacoesEsquerda())
    print('Rotacoes a direita:', arvore.rotacoesDireita())
    print('Elementos restantes:', arvore.quantidadeElementos())

main()
