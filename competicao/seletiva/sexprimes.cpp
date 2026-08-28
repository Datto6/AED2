#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int binarySearch(int arr[],int x,int definitivo,int n){
    int ini=0;
    int fim=n-1;
    while(ini<=fim){
        int meio=(ini+fim)/2;
        if (arr[meio]==x && arr[meio]<=definitivo){
            return 1;
        }
        else if(arr[meio]>x){
            fim=meio-1;
        }
        else{
            ini=meio+1;
        }
    }
    return 0;
}
int isPrimo(int n){
    for(int i=2;i<(int) sqrt(n)+1;i++){
        if (n%i==0){
            return 0;
        }
    }
    return 1;
}
int calculaprimo(int arr[],int ini,int fim){
    int indice=0;
    for (int i=ini;i<fim+1;i++){
        if(i!=1 && isPrimo(i)){
            arr[indice]=i;
            indice++;
        }
    }
    return indice+1;
}



void sexyPrimes(int ini,int fim){
    int n=(fim-ini)+1;
    int* arr=(int *) malloc(sizeof(int)*n);
    int size=calculaprimo(arr,ini,fim);
    int doubles=0; int triples=0;
    int quads=0; int quintuples=0;;
    for (int i=0;i<size;i++){
        if (arr[i]>=fim){
            break;
        }
        if (arr[i]>=ini){
            int elem=arr[i]+6;
            if(binarySearch(arr,elem,fim,size)){
                doubles+=1;
                elem=elem+6;
                if (binarySearch(arr,elem,fim,size)){
                    triples+=1;
                    elem+=6;
                    if (binarySearch(arr,elem,fim,size)){
                        quads+=1;
                        elem+=6;
                        if(binarySearch(arr,elem,fim,size)){
                            quintuples+=1;
                            elem+=6;
                        }
                    }
                }
            }
        }
    }
    printf("%d %d %d %d\n",doubles,triples,quads,quintuples);
}
int main (void){
    int vezes;
    scanf("%d",&vezes);
    for(int i=0;i<vezes;i++){
        int ini, fim;
        scanf("%d %d",&ini,&fim);
        sexyPrimes(ini,fim);
    }
    return 0;
}
