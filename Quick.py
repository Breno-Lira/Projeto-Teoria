import random
import time
import math

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menor = [x for x in arr[1:] if x <= pivot]
    maior = [x for x in arr[1:] if x > pivot]
    return quick_sort(menor) + [pivot] + quick_sort(maior)

def medir_tempo(n, repeticoes):
    tempos = []
    for i in range(repeticoes):
        lista = [random.randint(1, 1000000) for _ in range(n)]
        inicio = time.time()
        quick_sort(lista)
        fim = time.time()
        duracao = fim - inicio
        tempos.append(duracao)
        print(f"Execução {i + 1} / {repeticoes} (tamanho {n}) : {duracao:.5f}s")
    return tempos

def calcular_media(valores):
    soma = sum(valores)
    return soma/len(valores)

def calcular_desvio_padrao(valores, media):
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return math.sqrt(variancia)

tamanhos = [500, 5000, 50000, 500000]
repeticoes = 20

for tamanho in tamanhos:
    tempos = medir_tempo(tamanho, repeticoes)
    media = calcular_media(tempos)
    desvio = calcular_desvio_padrao(tempos,media)
    print(f"Tamanho {tamanho} : média = {media:.5f}s, desvio padrão = {desvio:.5f}s")










