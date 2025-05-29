import random

def gerar_lista(tamanho, max_valor):
    return [random.randint(0, max_valor) for _ in range(tamanho)]

def gerar_melhor_caso_quicksort(lista):
    if not lista:
        return []
    meio = len(lista) // 2
    return [lista[meio]] + \
           gerar_melhor_caso_quicksort(lista[:meio]) + \
           gerar_melhor_caso_quicksort(lista[meio+1:])

def salvar_em_arquivo(lista, nome_arquivo, descricao):
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista:
            arquivo.write(f"{numero},\n")
    print(f"{descricao} salvo com sucesso em '{nome_arquivo}'.")

def main():
    print("Escolha o tamanho da lista (quantidade de números):")
    print("1 - 500\n2 - 5000\n3 - 50000\n4 - 500000")
    escolha_tam = input("Opção: ")

    tamanhos = {"1": 500, "2": 5000, "3": 50000, "4": 500000}
    tam = tamanhos.get(escolha_tam)
    
    if tam is None:
        print("Opção inválida de tamanho.")
        return

    print("\nEscolha o tipo de caso para salvar:")
    print("1 - Caso médio (aleatório)")
    print("2 - Melhor caso (quicksort balanceado)")
    print("3 - Pior caso (ordenado decrescente)")
    escolha_caso = input("Opção: ")

    max_valor = 1000000
    lista_base = gerar_lista(tam, max_valor)

    if escolha_caso == "1":
        salvar_em_arquivo(lista_base, "lista_numeros.txt", "CASO MÉDIO (lista aleatória)")
    elif escolha_caso == "2":
        lista_ordenada = sorted(lista_base)
        melhor_caso = gerar_melhor_caso_quicksort(lista_ordenada)
        salvar_em_arquivo(melhor_caso, "lista_numeros.txt", "MELHOR CASO (quicksort balanceado)")
    elif escolha_caso == "3":
        salvar_em_arquivo(sorted(lista_base, reverse=True), "lista_numeros.txt", "PIOR CASO (lista ordenada decrescente)")
    else:
        print("Opção inválida de caso.")

if __name__ == "__main__":
    main()
