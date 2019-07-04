/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package OperacionArreglos;

import java.util.Scanner;

/**
 *
 * @author kiuub
 */
public class Operaciones {
    public static void arrayExercise(){
        Scanner scan = new Scanner(System.in);
        System.out.println("ingrese el tamaño del arreglo: ");
        int arraysize = scan.nextInt();
        System.out.println("ingrese el numero de operaciones: ");
        int nOperarciones = scan.nextInt();
        
        long[] arreglo = new long[arraysize];
        long mayor = 0;
        int a= 0 ;
        int b = 0;
        long sum = 0;

        for (int i = 0; i < nOperarciones; i++){
            System.out.println("A: ");
            a=scan.nextInt();
            System.out.println("B: ");
            b=scan.nextInt();
            System.out.println("sum: ");
            sum=scan.nextInt();
            arreglo[a-1] += sum;
            if(b < arraysize){
                arreglo[b]-=sum;
            }
        }
        for (int i = 0; i < arreglo.length; i++){
            if(arreglo[i] > mayor){
                mayor = arreglo[i];
            }
        }
        System.out.println("Resultado: " + mayor);        
    }
     public static void main(String[] args) {
          arrayExercise();
    }
}
