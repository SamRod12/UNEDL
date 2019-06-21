/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Rotacion;

import javax.swing.JOptionPane;

/**
 *
 * @author kiuub
 */
public class Rotacion {
    private static int[] arr ;
 
    public static void main(String args[]){
        Rotacion rota = new Rotacion();
        int tamaño;
        tamaño = Integer.parseInt(JOptionPane.showInputDialog(null, "ingrese el tamaño del arreglo"));
         arr = new int[tamaño];
        for(int x = 0; x<arr.length;x++){
            arr[x] = Integer.parseInt(JOptionPane.showInputDialog("ingrese el valor en la posicion : "+ x));
        }
       int  rot = Integer.parseInt(JOptionPane.showInputDialog("cuantas veces quiere rotar a la izquierda el arreglo?")); 
        rota.imprimir();
       rota.rotarIzda(rot);
       rota.imprimir();
    }
    
  void rotarIzda(int pos){
        for(int i=1;i<=pos;i++){
            rotarIzda1Pos();
        }
    }
     
    void rotarIzda1Pos(){
        int temp = arr[0];
        for(int i=0;i<arr.length-1;i++){
            arr[i] = arr[i+1];
        }
        arr[arr.length-1] = temp;
    }
    void imprimir(){
        for(int x = 0;x<arr.length;x++){
            System.out.print(arr[x]);
        }
        System.out.println();
    }
}
