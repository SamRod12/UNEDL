/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package examen3erparcial;


import java.util.Scanner;

/**
 *
 * @author kiuub
 */
public class Examen3erParcial {

    /**
     * @param args the command line arguments
     */
    public int cont=0;
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner in = new Scanner (System.in);
        System.out.println("Ingresa el tamaño del arreglo: ");
        int tamaño;
        tamaño = in.nextInt();
        int [] arreglo = new int[tamaño];
        
        for(int x=0;x<arreglo.length;x++){
            System.out.println("Ingresa el valor: "+(x+1));
            arreglo[x]=in.nextInt();
        }
          Examen3erParcial  ob = new Examen3erParcial();
      
        ob.bubbleSort(arreglo);
        System.out.println("primer elemento: "+arreglo[0]+"\nUltimo elemento: "+arreglo[arreglo.length-1]);
      
    }
    
public  void bubbleSort(int arr[])
    {
        cont=0;
        int n = arr.length;
        for (int i = 0; i < n-1; i++)
            for (int j = 0; j < n-i-1; j++)
                if (arr[j] > arr[j+1])
                {
                    // swap temp and arr[i]
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    cont++;
                    printArray(arr, cont);
                }
        System.out.println("permutas: "+cont);
    }
public void printArray(int arr[], int cont)
    {
        int n = arr.length;
        for (int i=0; i<n; ++i)
            System.out.print(arr[i] + " ");
        System.out.print("permuta "+cont+"\n");
    }
 
}
