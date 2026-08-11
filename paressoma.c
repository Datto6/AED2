#include <stdio.h>
void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int leftArr[n1], rightArr[n2];
    for (i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        rightArr[j] = arr[mid + 1 + j];

    // Merge the temporary arrays back into arr[left..right]
    i = 0;
    j = 0;
    k = left;
    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        }
        else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}
int ContarCruzados(int A[], int ini, int mid, int fim, int lo, int hi){
    int p1 = mid+1;
    int p2 = mid+1;
    int cont = 0;
    for(int i=mid;i>=ini;i--){
        while(p1<=fim && A[p1]<lo-A[i]){
            p1++;
        }
        while(p2<=fim && A[p2]<=hi-A[i]){
            p2++;
        }
        cont = cont + (p2 - p1);
    }
    return cont;
}
int ContarPares(int A[], int ini,int fim, int lo, int hi){
    if (ini>=fim){
        return 0;
    }
    int mid=(ini+fim)/2;
    int c1 = ContarPares(A, ini, mid, lo, hi);
    int c2 = ContarPares(A, mid+1, fim, lo, hi);
    int c3 = ContarCruzados(A, ini, mid, fim, lo, hi);
    merge(A, ini, mid, fim);
    return c1+c2+c3;
}
void printArray(int A[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d", A[i]);
        if (i < n - 1)
            printf(", ");
    }
    printf("]");
}

void test(int A[], int n, int lo, int hi, int expected) {
    printf("A = ");
    printArray(A, n);

    printf(", lo = %d, hi = %d\n", lo, hi);

    int result = ContarPares(A, 0, n - 1, lo, hi);

    printf("Expected: %d\n", expected);
    printf("Got:      %d\n", result);

    printf("Sorted A: ");
    printArray(A, n);
    printf("\n");

    if (result == expected)
        printf("PASS\n");
    else
        printf("FAIL\n");

    printf("-----------------------------\n");
}

int main() {

    int A1[] = {1, 2, 3, 4};
    test(A1, 4, 5, 6, 3);

    int A2[] = {1, 2, 3, 4, 5};
    test(A2, 5, 100, 200, 0);

    int A3[] = {1, 2, 3, 4};
    test(A3, 4, 3, 7, 6);

    int A4[] = {1, 2, 3, 4};
    test(A4, 4, 5, 5, 2);

    int A5[] = {1, 1, 2, 2};
    test(A5, 4, 3, 3, 4);

    int A6[] = {-5, -2, 1, 4};
    test(A6, 4, -4, 0, 3);

    int A7[] = {4, 1, 3, 2};
    test(A7, 4, 5, 6, 3);

    int A8[] = {42};
    test(A8, 1, 0, 100, 0);

    int A9[] = {7, 3};
    test(A9, 2, 10, 10, 1);

    return 0;
}