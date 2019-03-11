/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package programacion.visual;
import java.util.*;
/**
 *
 * @author kiuub
 */
public class ExamenDiagnostico {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        int[][] matriz = {{1,3,5,7},{4,7,9,7},{2,6,8,0},{2,4,5,2}};
	int x=3,y=3;
        int cont=0;
	int inicio=0,fin=0;
        for(int o=0;o<matriz.length;o++){
            for(int p=0;p<matriz.length;p++){
                System.out.print(matriz[o][p]+(","));
            }
            System.out.println();
        }
        System.out.println();
    for(int i=0; i<matriz.length;i++){
            if(cont%2==0){
                for(int abajo=0;abajo<matriz.length;abajo++){
                    System.out.print(matriz[abajo][cont]+(","));
                }
                cont++;
            }
            else if(cont%2==1){
                for(int arriba=matriz.length-1;arriba>=0;arriba--){
                    System.out.print(matriz[arriba][cont]+(","));
                }
                cont++;
            }
            
        }
    }
    
}
