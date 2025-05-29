#include <stdio.h>
#include <time.h>  // Para medir o tempo

void trocar(int *a, int *b);
int particao(int vetor[], int inicio, int fim);
void quicksort(int vetor[], int inicio, int fim);
void imprimir(int vetor[], int tamanho);

int main() {
    int vetor[] = {10, 7, 8, 9, 1, 5};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    clock_t inicio, fim;
    double tempo_execucao;

    inicio = clock();  

    quicksort(vetor, 0, tamanho - 1);

    fim = clock();    

    tempo_execucao = (double)(fim - inicio) / CLOCKS_PER_SEC;

    printf("Vetor ordenado: ");
    // imprimir(vetor, tamanho);

    printf("Tempo de execucao do QuickSort: %.6f segundos\n", tempo_execucao);

    return 0;
}

void trocar(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int particao(int vetor[], int inicio, int fim) {
    int pivo = vetor[fim];
    int i = inicio - 1;

    for (int j = inicio; j < fim; j++) {
        if (vetor[j] < pivo) {
            i++;
            trocar(&vetor[i], &vetor[j]);
        }
    }

    trocar(&vetor[i + 1], &vetor[fim]);
    return i + 1;
}

void quicksort(int vetor[], int inicio, int fim) {
    if (inicio < fim) {
        int indicePivo = particao(vetor, inicio, fim);
        quicksort(vetor, inicio, indicePivo - 1); 
        quicksort(vetor, indicePivo + 1, fim);    
    }
}

void imprimir(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}
