# indice_invertido.py
MINI-PROJETO HASTING FEITOS PELOS ALUNOS JACKSON VICTOR E SUZANY VALESKA

## Como rodar o código

1. **Baixe os arquivos:** Faça o download do código (`indice_invertido.py`) e do texto do livro (`dom_casmurro.txt`) aqui do repositório.
2. **Deixe tudo junto:** Coloque os dois arquivos dentro da **mesma pasta** no seu computador.
3. **Execute o script:** Abra essa pasta no VS Code ou no terminal do seu computador e rode o comando:

```bash
python indice_invertido.py

## Relatório do Experimento

### Experimento 2 — Vantagem da Indexação

Testamos buscas pela expressão `"justina e capitu"` no livro *Dom Casmurro* (mediana de 3 execuções em milissegundos):

| Consultas | Varredura completa (ms) | Construção + consultas (ms) |
| :---:      | :---:                   | :---: |
| **1**       | 34.87                   | 56.40 |
| **10**      | 327.45                       | 56.63 |
| **100**      | 3183.77                 | 55.02 |
| **1.000**    | 31910.68                | 58.44 |

---

### Análise dos Resultados

1. **Qual estratégia foi mais rápida? Em quais situações?**
   Para **1 busca única**, a **varredura** foi mais rápida (`34.87 ms` vs `56.40 ms`), pois lê o texto uma vez sem montar o índice antes. Para **várias buscas** (`10` ou mais), o **índice invertido** vence de longe, mantendo o tempo quase constante (~56 ms) enquanto a varredura passa de 31 segundos.

2. **A partir de aproximadamente quantas consultas a indexação passou a ser vantajosa?**
   A partir de **2 consultas**, pois duas varreduras (~69 ms) já custam mais caro do que montar o índice e buscar (~56 ms).

3. **Qual é a vantagem de utilizar conjuntos (`set`) em vez de listas (`list`) para armazenar as linhas?**
   O `set` evita números de linha repetidos automaticamente e torna operações de interseção (`E`, como na busca `"justina e capitu"`) e união (`OU`) muito mais rápidas do que comparar listas.

4. **Qual é a complexidade esperada da busca de uma chave em um dicionário Python?**
   **$O(1)$** (tempo constante) no caso médio, já que o dicionário usa uma tabela hash por baixo dos panos.

5. **Qual é a complexidade da construção do índice e das operações de união e interseção?**
   * **Construção do índice:** $O(n)$, pois passa uma vez por todas as palavras do texto.
   * **União:** $O(a + b)$, somando o tamanho dos dois conjuntos juntados.
   * **Interseção:** $O(\min(a, b))$, pois basta percorrer o menor conjunto e checar o que existe no maior.

6. **Qual é a principal desvantagem da indexação em relação ao consumo de memória?**
   Gasta mais **memória RAM**, pois precisa guardar todas as palavras únicas do livro e todas as suas linhas na memória durante a execução.
