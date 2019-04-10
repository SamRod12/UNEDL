/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ExamenTaller;
import ExamenTaller.CostoMesa;
import java.util.Scanner;
/**
 *
 * @author kiuub
 */
public class DatosFinales {
    
    public static void main(String args[]){
        Scanner entrada = new Scanner(System.in);
        CostoMesa datos = new CostoMesa();
       
        System.out.println("ingrese el alto de la mesa en metros: ");
        datos.setAlto(entrada.nextDouble());
        System.out.println("ingrese el ancho de la mesa en metros: ");
        datos.setAncho(entrada.nextDouble());
        System.out.println("ingresa el costo por metro cuadrado: ");
        datos.setCosto(entrada.nextDouble());
        datos.setArea(datos.getAlto()*datos.getAncho());
        System.out.println("Costo de la mesa: "+datos.calcularCosto(datos.getArea(), datos.getCosto()));
        
        
        
        
    }
    
    
    
    
}
