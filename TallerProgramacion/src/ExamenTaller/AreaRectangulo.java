/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ExamenTaller;

/**
 *
 * @author kiuub
 */
public class AreaRectangulo  {
    protected double alto;
    protected double ancho;
    protected double area;
    public AreaRectangulo() {
    }
    
    public AreaRectangulo(double area){
        this.area=area;
    }
    public AreaRectangulo(double alto, double ancho) {
        this.alto = alto;
        this.ancho = ancho;
    }

    public double getAlto() {
        return alto;
    }

    public void setAlto(double alto) {
        this.alto = alto;
    }

    public double getAncho() {
        return ancho;
    }

    public void setAncho(double ancho) {
        this.ancho = ancho;
    }

    public double getArea() {
        return area;
    }

    public void setArea(double area) {
        this.area = area;
    }
    
    
}
