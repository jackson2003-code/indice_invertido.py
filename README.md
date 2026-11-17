# indice_invertido.py
MINI-PROJETO HASTING FEITOS PELOS ALUNOS JACKSON VICTOR E SUZANY VALESKA

## Como rodar o código

1. **Baixe os arquivos:** Faça o download do código (indice_invertido.py) e do texto do livro (dom_casmurro.txt) aqui do repositório.
2. **Deixe tudo junto:** Coloque os dois arquivos dentro da mesma pasta no seu computador.
3. **Execute o script:** Abra essa pasta no VS Code ou no terminal do seu computador e rode o comando:

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
   Para **1 busca única**, a **varredura** foi mais rápida (34.87 ms vs 56.40 ms), pois lê o texto uma vez sem montar o índice antes. Para **várias buscas** (`10` ou mais), o **índice invertido** vence de longe, mantendo o tempo quase constante (~56 ms) enquanto a varredura passa de 31 segundos.

2. **A partir de aproximadamente quantas consultas a indexação passou a ser vantajosa?**
   A partir de 2 consultas, pois duas varreduras (~69 ms) já custam mais caro do que montar o índice e buscar (~56 ms).

3. **Qual é a vantagem de utilizar conjuntos (set) em vez de listas (list) para armazenar as linhas?**
   O set evita números de linha repetidos automaticamente e torna operações de interseção (E, como na busca "justina e capitu") e união (OU) muito mais rápidas do que comparar listas.

4. **Qual é a complexidade esperada da busca de uma chave em um dicionário Python?**
   (tempo constante) no caso médio, já que o dicionário usa uma tabela hash por baixo dos panos.

5. **Qual é a complexidade da construção do índice e das operações de união e interseção?**
   * Construção do índice: pois passa uma vez por todas as palavras do texto.
   * União: somando o tamanho dos dois conjuntos juntados.
   * Interseção: pois basta percorrer o menor conjunto e checar o que existe no maior.

6. **Qual é a principal desvantagem da indexação em relação ao consumo de memória?**
   Gasta mais memória RAM, pois precisa guardar todas as palavras únicas do livro e todas as suas linhas na memória durante a execução.

   ## Diário de Bordo 

Durante o trabalho, usei a IA para tirar dúvidas, resolver uns erros que deram no VS Code e adaptar o código para os testes do professor:

* **1. Medindo o tempo dos testes**
  * **O que perguntei:** Como funcionava o `import time` e como medir o tempo em milissegundos (pegando a mediana de 3 execuções) para preencher a tabela do Experimento 2.
  * **O que a IA explicou:** Mostrou como usar o `time.perf_counter()` tipo um cronômetro e deu a dica de fazer um arquivo separado só para rodar essas medições sem bagunçar o código principal.
  * **Como conferi:** Rodei o teste no VS Code com o *Dom Casmurro* usando primeiro a busca `"justina e capitu"` já escrita no código, e anotei os tempos reais que apareceram no terminal.

* **2. Arrumando erros e colocando `input()`**
  * **O que perguntei:** Por que estava dando erro de função não definida (`NameError`) no arquivo de teste e como trocar a busca fixa (`"justina e capitu"`) por um `input()` para qualquer pessoa digitar a palavra que quiser.
  * **O que a IA explicou:** Mostrou que eu tinha esquecido de colocar as funções no arquivo separado de teste e ensinou a usar `input().strip().lower()` para limpar espaços e letras maiúsculas do que o usuário digitar.
  * **Como conferi:** Corrigi o código, fui digitando várias palavras diferentes no terminal e conferi se as linhas do índice batiam com a busca normal no livro.

* **3. Adaptando o código para passar nos testes**
  * **O que perguntei:** Se o meu código já passava nos testes do PDF e como ajustar o que faltava sem mudar o jeito que eu tinha programado.
  * **O que a IA explicou:** Avisou que o corretor automático importa exatamente os nomes `construir_indice`, `buscar`, `buscar_e` e `buscar_ou`, que o `input()` precisava ficar dentro de `if __name__ == "__main__":` para não travar a importação, e que precisava limpar todo tipo de pontuação e tratar textos/listas vazias nos testes reservados.
  * **Como conferi:** Renomeei as funções mantendo minha lógica original e rodei os testes do enunciado junto com casos extras (textos vazios, pontuações variadas e palavras com letra maiúscula), vendo que tudo passou sem erro. Além disso, testando a palavra `"capitu"` depois da correção, notei na prática que o tempo da varredura completa aumentou mais da metade em relação à versão antiga (subiu de `13.9439s` para `32.6853s`, já que agora ela limpa todas as pontuações do livro inteiro a cada consulta), enquanto o índice invertido continuou praticamente igual e instantâneo (`0.0150s` antes e `0.0149s` depois).

* **4. Revisando a teoria e organizando o GitHub**
  * **O que perguntei:** Qual era a complexidade (Big-O) das buscas no dicionário e das operações de união e interseção dos conjuntos, além de como arrumar a formatação do `README.md`.
  * **O que a IA explicou:** Explicou de um jeito simples por que a busca é $O(1)$ e como ficam os tempos de construção, união  e interseção, além de ajudar a tirar uns blocos de código que tinham quebrado a formatação no GitHub.
  * **Como conferi:** Comparei a teoria com os tempos da minha tabela (vendo na prática que o índice não fica lento mesmo com 1.000 buscas) e conferi como ficou a página final no GitHub.
