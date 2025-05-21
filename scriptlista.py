import random

def gerar_lista(tamanho, max_valor):
    return [random.randint(0, max_valor) for _ in range(tamanho)]


def salvar_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for numero in lista:
            arquivo.write(f"{numero},\n")
    print(f"Lista salva com sucesso em '{nome_arquivo}'.")


def main():

    print("Escolha o tamanho da lista (quantidade de numeros)\n1- 100\n2- 5000\n3- 50000\n4- 100000")
    escolha = input("Opção: ")

    tamanho = {"1": 100 , "2": 5000 , "3": 50000, "4": 100000}
    max_valor = 1000000
    tam = tamanho.get(escolha)
    

    lista = gerar_lista(tam, max_valor)
    salvar_em_arquivo(lista, "lista_numeros.txt")
    
    print("Lista gerada, procure pelo arquivo lista_numeros.txt")
    

if __name__ == "__main__":
    main()


