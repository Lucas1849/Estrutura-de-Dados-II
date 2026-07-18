class Livro:
    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        
    def __str__(self):
        return f'{self.codigo}; {self.titulo}; {self.autor}; {self.ano}'