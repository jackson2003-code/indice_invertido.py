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

Para testar na prática se vale a pena gastar um tempo inicial montando o índice antes de começar a pesquisar, fizemos várias buscas pela palavra `"capitu"` no livro *Dom Casmurro* (Machado de Assis). Cada teste foi rodado 3 vezes e pegamos o valor do meio (mediana) em milissegundos (`ms`):

| Quantidade de consultas | Varredura completa (ms) | Construção do índice + consultas (ms) |
| :--- | :---: | :---: |
| **1** | 38.13 | 58.88 |
| **10** | 379.41 | 57.62 |
| **100** | 3316.87 | 53.89 |
| **1.000** | 32268.15 | 54.09 |

---

### Análise dos Resultados

**1. Qual estratégia foi mais rápida? Em quais situações?**
* Se a ideia for fazer **apenas 1 busca isolada**, a **varredura completa** ganha (`38.13 ms` contra `58.88 ms`), porque ela lê o livro uma vez e pronto, sem precisar montar nenhuma estrutura antes.
* Porém, quando fazemos **várias buscas seguidas** (`10`, `100` ou `1.000`), o **índice invertido** vence de lavada. Enquanto a varredura vai acumulando tempo a cada nova pesquisa (passando de 32 segundos em 1.000 buscas), o índice fica praticamente parado na casa dos `54 ms` a `58 ms`. Isso acontece porque quase todo esse tempo vai só para criar o índice na primeira vez; depois disso, as buscas saem praticamente de graça.

**2. A partir de aproximadamente quantas consultas a indexação passou a ser vantajosa?**
Logo na **2ª consulta**. Como cada varredura completa leva cerca de `38 ms` (duas buscas já dão uns `76 ms`) e montar o índice + buscar leva por volta de `54 ms` a `58 ms`, na segunda pesquisa o esforço inicial já se paga.

**3. Qual é a vantagem de utilizar conjuntos (`set`) em vez de listas (`list`) para armazenar as linhas?**
Tem duas vantagens bem claras no dia a dia do código:
* **Não repete linhas:** Se a palavra `"capitu"` aparecer duas vezes na mesma linha, o `set` guarda o número daquela linha só uma vez automaticamente, sem a gente precisar ficar checando se já estava lá.
* **Cruzar buscas fica muito mais rápido:** Quando queremos achar linhas que tenham *palavra A* **E** *palavra B* (ou *A* **OU** *B*), juntar ou cruzar conjuntos no Python é bem mais rápido do que ficar comparando duas listas item por item.

**4. Qual é a complexidade esperada da busca de uma chave em um dicionário Python?**
No caso médio, é **$O(1)$** (tempo constante). Como o dicionário (`dict`) do Python funciona como uma **tabela hash**, ele calcula direto onde a palavra está guardada na memória, sem precisar sair procurando de um em um (só no pior caso teórico de muitas colisões é que iria para $O(n)$, mas na prática fica em $O(1)$).

**5. Qual é a complexidade da construção do índice e das operações de união e interseção?**
* **Construção do índice:** **$O(N)$**, onde $N$ é o total de palavras do texto, já que precisamos passar pelo livro inteiro uma única vez e ir guardando cada palavra no dicionário em tempo médio $O(1)$.
* **União ($A \cup B$):** **$O(|A| + |B|)$**, onde $|A|$ e $|B|$ são o tamanho dos dois conjuntos de linhas, porque precisamos juntar todos os elementos dos dois lados no resultado.
* **Interseção ($A \cap B$):** **$O(\min(|A|, |B|))$** no caso médio, pois o Python pega o menor conjunto e apenas checa em tempo $O(1)$ quais daquelas linhas também aparecem no conjunto maior.

**6. Qual é a principal desvantagem da indexação em relação ao consumo de memória?**
Ela **gasta bem mais memória RAM**. Enquanto a varredura lê o texto sem precisar guardar quase nada extra, o índice invertido precisa manter na memória todas as palavras diferentes do livro junto com todas as linhas em que elas aparecem. Se fossem milhares de livros gigantes, o índice poderia ocupar tanto ou até mais espaço na memória do que os próprios textos.
