import time

def criar_indice(texto_livro):
    indice = {}
    linhas_livro = texto_livro.split('\n')
    
    for num_linha, frase in enumerate(linhas_livro, start=1):
        frase_limpa = frase.lower().replace(",", " ").replace(".", " ").replace("!", " ")
        lista_palavras = frase_limpa.split()
        
        for palavra in lista_palavras:
            if palavra not in indice:
                indice[palavra] = set()
            indice[palavra].add(num_linha)
            
    return indice

def pesquisar_palavra(indice, palavra_procurada):
    if palavra_procurada in indice:
        return sorted(indice[palavra_procurada])
    else:
        return []

def pesquisar_todas(indice, palavras_procuradas):
    if palavras_procuradas[0] in indice:
        linhas_em_comum = set(indice[palavras_procuradas[0]])
    else:
        linhas_em_comum = set()
        
    for palavra in palavras_procuradas[1:]:
        if palavra in indice:
            linhas_em_comum = linhas_em_comum.intersection(indice[palavra])
        else:
            linhas_em_comum = set()
            break
            
    return sorted(linhas_em_comum)

def pesquisar_qualquer(indice, palavras_procuradas):
    linhas_juntas = set()
    for palavra in palavras_procuradas:
        if palavra in indice:
            linhas_juntas = linhas_juntas.union(indice[palavra])
    return sorted(linhas_juntas)

def ler_livro_todo(texto_livro, palavra_procurada):
    onde_apareceu = []
    linhas_livro = texto_livro.split('\n')
    
    for num_linha, frase in enumerate(linhas_livro, start=1):
        frase_limpa = frase.lower().replace(",", " ").replace(".", " ").replace("!", " ")
        lista_palavras = frase_limpa.split()
        
        if palavra_procurada in lista_palavras:
            onde_apareceu.append(num_linha)
            
    return onde_apareceu


with open("dom_casmurro.txt", "r", encoding="utf-8") as arquivo:
    historia = arquivo.read()

meu_indice = criar_indice(historia)
alvo = "observar e capitu"

inicio_rapido = time.perf_counter()
for _ in range(1000):
    pesquisar_palavra(meu_indice, alvo)
fim_rapido = time.perf_counter()
tempo_com_indice = fim_rapido - inicio_rapido

inicio_lento = time.perf_counter()
for _ in range(1000):
    ler_livro_todo(historia, alvo)
fim_lento = time.perf_counter()
tempo_sem_indice = fim_lento - inicio_lento

print(f"Tempo do Índice Invertido: {tempo_com_indice:.4f} segundos")
print(f"Tempo da Varredura Completa: {tempo_sem_indice:.4f} segundos")