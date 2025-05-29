import time
import math

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menor = [x for x in arr[1:] if x <= pivot]
    maior = [x for x in arr[1:] if x > pivot]
    return quick_sort(menor) + [pivot] + quick_sort(maior)

def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_desvio_padrao(valores, media):
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return math.sqrt(variancia)

def ler_lista_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip().split(',')
        lista = [int(num.strip()) for num in conteudo if num.strip().isdigit()]
    print(f"{len(lista)} números lidos do arquivo '{nome_arquivo}'.")
    return lista

def medir_tempo(lista, repeticoes):
    tempos = []
    for i in range(repeticoes):
        lista_copia = lista.copy()
        inicio = time.time()
        quick_sort(lista_copia)
        fim = time.time()
        duracao = fim - inicio
        tempos.append(duracao)
        print(f"Execução {i + 1} / {repeticoes} : {duracao:.5f}s")
    return tempos

def main():
    nome_arquivo = "lista_numeros.txt"
    repeticoes = int(input("Quantas vezes deseja repetir o teste? "))

    lista = ler_lista_arquivo(nome_arquivo)
    tempos = medir_tempo(lista, repeticoes)
    media = calcular_media(tempos)
    desvio = calcular_desvio_padrao(tempos, media)

    print(f"\nResultados para vetor com {len(lista)} elementos:")
    print(f"Média do tempo: {media:.5f}s")
    print(f"Desvio padrão: {desvio:.5f}s")

if __name__ == "__main__":
    main()
