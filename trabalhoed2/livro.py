class Livro:
    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def __str__(self):
        return f'{self.codigo};{self.titulo};{self.autor};{self.ano}'

    #Código gerado com auxílio de Inteligência Artificial
    #Estava com dificuldade de fazer a comparação entre dois objetos para guardá-los na avl, quando eu conseguia guardar 
    #era guardado apenas o self.codigo e não o objeto como um todo. Assim eu não conseguia acessar as outras informações
    #recorri a esse auxílio e consegui entender o seguinte:

    def __lt__(self, outro): #Método definido por mim que funciona parecido com o __str__, ou seja quando uma comparação for 
        return self.codigo < outro.codigo #chamada ele automaticamente vai usar esses métodos __lessthan__, ou __greaterthan__

    def __gt__(self, outro):
        return self.codigo > outro.codigo

    def __eq__(self, outro):
        return self.codigo == outro.codigo
#Com isso os métodos acima funcionam para que a chave de comparação da alocação do objeto na avl seja o código de cada livro 