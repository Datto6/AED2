import java.util.Scanner;
import java.util.Arrays;
public class Selectionsort{
    public static int minimo(int[] vetor,int ini, int n){
        int min=vetor[ini];
        int index=ini;
        for(int i=ini;i<n;i++){
            if (vetor[i]<min){
                min=vetor[i];
                index=i;
            }
        }
        return index;
    }
    public static void selectionSort(int[] vetor,int ini, int fim){
        if (ini>=fim){
            return;
        }
        int index=Selectionsort.minimo(vetor,ini,fim);
        int minimo=vetor[index];
        vetor[index]=vetor[ini];
        vetor[ini]=minimo;
        Selectionsort.selectionSort(vetor, ini+1, fim);
    }
        public static void main(String[] args){
        
        int desordenado[]=new int[10];
        int n=10;
        Scanner scan=new Scanner(System.in);
        for(int i=0;i<n;i++){
            System.out.println("Escreva um numero");
            int input=scan.nextInt();
            desordenado[i]=input;
        }
        System.out.println(Arrays.toString(desordenado));
        Selectionsort.selectionSort(desordenado, 0, n);
        System.out.println(Arrays.toString(desordenado));
    }
}
