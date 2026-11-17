import time
import string

def limpar_palavras(frase):
    frase_limpa = frase.lower()
    for pontuacao in string.punctuation + "«»“”—–":
        frase_limpa = frase_limpa.replace(pontuacao, " ")
    return frase_limpa.split()

def construir_indice(texto_livro):
    indice = {}
    if not texto_livro:
        return indice
        
    linhas_livro = texto_livro.split('\n')
    for num_linha, frase in enumerate(linhas_livro, start=1):
        lista_palavras = limpar_palavras(frase)
        for palavra in lista_palavras:
            if palavra not in indice:
                indice[palavra] = set()
            indice[palavra].add(num_linha)
    return indice
    
def buscar(indice, palavra_procurada):
    palavra_limpa = palavra_procurada.strip().lower()
    if palavra_limpa in indice:
        return sorted(indice[palavra_limpa])
    else:
        return []
        
def buscar_e(indice, palavras_procuradas):
    if not palavras_procuradas:
        return []
        
    primeira = palavras_procuradas[0].strip().lower()
    if primeira in indice:
        linhas_em_comum = set(indice[primeira])
    else:
        return []
        
    for palavra in palavras_procuradas[1:]:
        palavra_limpa = palavra.strip().lower()
        if palavra_limpa in indice:
            linhas_em_comum = linhas_em_comum.intersection(indice[palavra_limpa])
        else:
            return []

    return sorted(linhas_em_comum)
    
def buscar_ou(indice, palavras_procuradas):
    linhas_juntas = set()
    for palavra in palavras_procuradas:
        palavra_limpa = palavra.strip().lower()
        if palavra_limpa in indice:
            linhas_juntas = linhas_juntas.union(indice[palavra_limpa])
    return sorted(linhas_juntas)

def ler_livro_todo(texto_livro, palavra_procurada):
    onde_apareceu = []
    palavra_limpa = palavra_procurada.strip().lower()
    linhas_livro = texto_livro.split('\n')

    for num_linha, frase in enumerate(linhas_livro, start=1):
        lista_palavras = limpar_palavras(frase)

        if palavra_limpa in lista_palavras:
            onde_apareceu.append(num_linha)

    return onde_apareceu

if __name__ == "__main__":
    with open("dom_casmurro.txt", "r", encoding="utf-8") as arquivo:
        historia = arquivo.read()

    meu_indice = construir_indice(historia)
    alvo = input("Digite a palavra que deseja buscar: ").strip().lower()

    inicio_rapido = time.perf_counter()
    for _ in range(1000):
        buscar(meu_indice, alvo)
    fim_rapido = time.perf_counter()
    tempo_com_indice = fim_rapido - inicio_rapido

    inicio_lento = time.perf_counter()
    for _ in range(1000):
        ler_livro_todo(historia, alvo)
    fim_lento = time.perf_counter()
    tempo_sem_indice = fim_lento - inicio_lento

    print(f"Tempo do Índice Invertido: {tempo_com_indice:.4f} segundos")
    print(f"Tempo da Varredura Completa: {tempo_sem_indice:.4f} segundos")
