# Pendências e Aprendizados — Trabalho ED2 (Árvore AVL de Livros)

## Bugs corrigidos nesta sessão

- **`devolver_classe_de_cada_linha` (main.py)**: retornava `classe_livro.codigo` em vez de `classe_livro`, então a árvore só armazenava o código inteiro, não o objeto `Livro`. Corrigido para retornar o objeto inteiro.
- **Comparação de objetos `Livro`**: a `AvlTree` compara valores diretamente com `<`, `>`, `==` (não usa uma chave separada). Para inserir objetos `Livro` é preciso que a própria classe saiba se comparar. Adicionados `__lt__`, `__gt__` e `__eq__` em `Livro`, comparando pelo `codigo` — sem precisar alterar `avl.py` nem `no.py`.

## Alternativa não aplicada (fica registrada)

Outra forma de resolver a comparação sem tocar em `Livro` seria inserir tuplas `(codigo, livro)` na árvore (tuplas comparam elemento a elemento). Foi descartada em favor de implementar `__lt__`/`__gt__`/`__eq__` diretamente na classe, que é mais alinhado ao enunciado ("a árvore deverá utilizar o código do livro como chave de ordenação").

## Atenção / possível problema introduzido

- Definir `__eq__` em uma classe remove o `__hash__` padrão (Python zera automaticamente). Isso significa que objetos `Livro` **não podem mais ser usados em `set` ou como chave de `dict`**. Não afeta o uso na árvore, mas é bom não esquecer se o código crescer.
- `Livro.autor` tem um método `def autor(self): print(self.autor)` com o mesmo nome do atributo `self.autor` — o atributo de instância sobrescreve o método na prática, então esse método nunca é chamado como método. Precisa ser removido ou renomeado.

## Pendências identificadas no `avl.py` (vs. `instruções_trabalho_ed2.md`)

- [ ] Função que recebe um **código** e devolve o **objeto `Livro`** correspondente (hoje `busca`/`buscafreq` só retornam `True`/`False`), tratando o caso de não existir.
- [ ] **Contadores de rotação** separados (esquerda x direita) — nenhuma rotação é contada hoje.
- [ ] Método público de **altura da árvore** (existe só a versão privada `__altura(no)`).
- [ ] Contador de **quantidade de livros armazenados**.
- [ ] **Busca por intervalo** `[codigoInicial, codigoFinal]`, percorrendo a árvore e cortando ramos que certamente não contêm valores no intervalo.
- [ ] Revisar `remove()`/`__removeValor` com casos que forcem rotação à direita (RR/RL), não só à esquerda — os testes atuais parecem ter coberto majoritariamente LL/LR.

## Pendências no `main.py`

- [ ] Trocar o cadastro manual via `input()` por inserção automática de **pelo menos 100 livros com códigos aleatórios** (`random.randint` ou similar).
- [ ] Realizar **20 buscas** usando a futura função busca-por-código.
- [ ] **Remover 20 livros**.
- [ ] Ao final, imprimir: altura da árvore, total de rotações à esquerda, total de rotações à direita, quantidade de elementos restantes.

## Fora do código

- [ ] Relatório em **PDF** discutindo:
  - por que a AVL mantém buscas eficientes;
  - em quais situações ocorreram mais rotações;
  - vantagens da AVL sobre uma árvore binária de busca comum.
