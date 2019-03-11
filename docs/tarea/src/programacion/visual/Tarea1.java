
package programacion.visual;

/**
 *
 * @author kxuub
 */
import java.util.*;
public class Tarea1 {
    public static void main (String args[]){
    int[][] matriz = {{-9,-9,-9, 1, 1, 1},
                      { 0,-9, 0, 4, 3, 2},
                      {-9,-9,-9, 1, 2, 3},
                      { 0, 0, 8, 6, 6, 0},
                      { 0, 0, 0,-2, 0, 0},
                      { 0, 0, 1, 2, 4, 0}};
   int[][] resultado = new int [4][4];
  
        for(int x=0;x<matriz.length;x++){
            for(int y=0;y<matriz.length;y++){
                System.out.print(matriz[x][y]+(" , "));
            }
            System.out.println();
        }
        System.out.println();
        for(int filas=0; filas<4;filas++){
            for(int columnas=0;columnas<4;columnas++){
                        
                    resultado[filas][columnas]=matriz[filas][columnas]+matriz[filas][columnas+1]+matriz[filas][columnas+2]+matriz[filas+1][columnas+1]+matriz[filas+2][columnas]+matriz[filas+2][columnas+1]+matriz[filas+2][columnas+2];
                    System.out.print(resultado[filas][columnas]+(", "));        
            }
            System.out.println();
        }
           
        
    }
}
        
         

