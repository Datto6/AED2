#include <stdlib.h>
#include <stdio.h>
int kesimo(int A[], int inia,int fima,int B[],int inib,int fimb,int k){
    int tamA=fima-inia+1;
    int tamB=fimb-inib+1; //indice inclusivo, adicionar um
    if (tamA==0){return B[inib+k];}
    if (tamB==0){return A[inia+k];}
    int i=tamA/2; int j=tamB/2;
    int meioA=A[inia+i]; int meioB=B[inib+j];
    if (i+j<k){
        if(meioA>meioB){
            return kesimo(A,inia,fima,B,inib+j+1,fimb,k-(j+1));
        }
        else{
            return kesimo(A,inia+i+1,fima,B,inib,fimb,k-(i+1));
        }
    }
    else{
        if(meioA>meioB){
            return kesimo(A,inia,inia+i-1,B,inib,fimb,k);
        }
        else{
            return kesimo(A,inia,fima,B,inib,inib+j-1,k);
        }
    }
}

int med_merge(int A[],int n,int B[],int m){
    int k=(n+m)/2;
    return kesimo(A,0,n-1,B,0,m-1,k);
}

int compara(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int esperado(int A[], int n, int B[], int m) {
    int C[n + m];

    for (int i = 0; i < n; i++)
        C[i] = A[i];

    for (int i = 0; i < m; i++)
        C[n + i] = B[i];

    qsort(C, n + m, sizeof(int), compara);

    int k = (n + m) / 2;

    return C[k];
}

void imprimir_array(int A[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d", A[i]);
        if (i < n - 1)
            printf(", ");
    }
    printf("]");
}


void teste(int A[], int n, int B[], int m) {

    printf("\nA = ");
    imprimir_array(A, n);

    printf("\nB = ");
    imprimir_array(B, m);

    int exp = esperado(A, n, B, m);

    printf("\nEsperado: %d", exp);

    int resultado = med_merge(A, n, B, m);

    printf("\nResultado: %d", resultado);

    if (resultado == exp)
        printf("  --> OK\n");
    else
        printf("  --> ERRO\n");
}


/* --------------------------------------------------
   TESTES
   -------------------------------------------------- */

int main() {

    
    // n=3, m=2 -> n+m=5
    int A1[] = {1, 3, 5};
    int B1[] = {2, 4};
    teste(A1, 3, B1, 2);


    // n=2, m=3 -> n+m=5
    int A2[] = {1, 4};
    int B2[] = {2, 3, 5};
    teste(A2, 2, B2, 3);


    // n=4, m=3 -> n+m=7
    int A3[] = {1, 4, 7, 10};
    int B3[] = {2, 5, 8};
    teste(A3, 4, B3, 3);


    // n=3, m=4 -> n+m=7
    int A4[] = {1, 5, 9};
    int B4[] = {2, 3, 7, 10};
    teste(A4, 3, B4, 4);


    // Todos os elementos de A menores
    // n=3, m=2 -> 5 elementos
    int A5[] = {1, 2, 3};
    int B5[] = {10, 20};
    teste(A5, 3, B5, 2);


    // Todos os elementos de B menores
    int A6[] = {10, 20, 30};
    int B6[] = {1, 2};
    teste(A6, 3, B6, 2);


    // Muitos elementos iguais
    int A7[] = {1, 2, 4};
    int B7[] = {2, 4};
    teste(A7, 3, B7, 2);


    // Elementos negativos
    int A8[] = {-10, -5, 0};
    int B8[] = {-8, -3};
    teste(A8, 3, B8, 2);


    // Mediano pertence a A
    // União: 1,2,3,4,5
    // k=2 -> 3
    int A9[] = {1, 3, 5};
    int B9[] = {2, 4};
    teste(A9, 3, B9, 2);


    // Mediano pertence a B
    // União: 1,2,3,4,5
    // k=2 -> 3
    int A10[] = {1, 5};
    int B10[] = {2, 3, 4};
    teste(A10, 2, B10, 3);


    // Tamanhos bastante diferentes
    // n=1, m=6 -> 7
    int A11[] = {10};
    int B11[] = {1, 2, 3, 4, 5, 6};
    teste(A11, 1, B11, 6);


    // n=6, m=1 -> 7
    int A12[] = {1, 2, 3, 4, 5, 6};
    int B12[] = {10};
    teste(A12, 6, B12, 1);

    return 0;
}