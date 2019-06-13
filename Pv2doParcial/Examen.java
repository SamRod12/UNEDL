/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Pv2doParcial;

import javax.swing.*;
import java.awt.event.*;
import java.util.*;



public class Examen extends JFrame implements ActionListener {
	
    private JLabel tf1,tf2,tf3,tf4;
    private JButton boton1;     
    
    public Examen() {

        setLayout(null);
        
        tf1= new JLabel("({){}({()}");
        tf1.setBounds(10,10,230,30);
        add(tf1);
         tf2= new JLabel("{(){((())}");
        tf2.setBounds(10,30,230,30);
        add(tf2);
         tf3= new JLabel("{({()()}})");
        tf3.setBounds(10,50,230,30);
        add(tf3);
         tf4= new JLabel("{()()}{()}");
        tf4.setBounds(10,70,230,30);
        add(tf4);
        boton1=new JButton("Verificar.");
        boton1.setBounds(10,100,180,30);
        add(boton1);
        boton1.addActionListener(this);

    }
    public void actionPerformed(ActionEvent e) {
        String  cadenas[] = {"({){}({()}","{(){((())}","{({()()}})","{()()}{()}"};
        if (e.getSource()==boton1) {
            for(int x=0;x<cadenas.length;x++){
           if (balanceada(cadenas[x]) ){
               String respuesta= "Está correcta.";
               cadenas[x]+="        "+respuesta;

           } else {
               String respuesta ="Esta incorrecta.";
               cadenas[x]+="        "+respuesta;

           }
           
            }
            tf1.setText(cadenas[0]);
       
            tf2.setText(cadenas[1]);
        
            tf3.setText(cadenas[2]);
       
             tf4.setText(cadenas[3]);
      
        }

    }

    public boolean balanceada(String cadena) {
    	 Pila pila1 = new Pila();    

    

    for (int f = 0 ; f < cadena.length() ; f++){
        if (cadena.charAt(f) == '(' || cadena.charAt(f) == '[' || cadena.charAt(f) == '{') {
        pila1.insertar(cadena.charAt(f));
        } else {
        if (cadena.charAt(f)==')') {
            if (pila1.extraer()!='(') {
                return false;
            }
    	    } else {
            if (cadena.charAt(f)==']') {
                if (pila1.extraer()!='[') {
                    return false;
                }
            } else {
                if (cadena.charAt(f)=='}') {
                    if (pila1.extraer()!='{') {
                        return false;
                    }
                }
            }
            }
       }   
        }
    if (pila1.vacia()) {
        return true;
    } else {
       return false;
    }
    }
    public class Pila {

    	class Nodo {
    		char simbolo;
    		Nodo sig;
    	}
    	
        private Nodo raiz;
        
        public Pila() {
            raiz=null;
        }

        public void insertar(char x) {
        Nodo nuevo;
            nuevo = new Nodo();
            nuevo.simbolo = x;
            if (raiz==null)
            {
                nuevo.sig = null;
                raiz = nuevo;
            }
            else
            {
                nuevo.sig = raiz;
                raiz = nuevo;
            }
        }

        public char extraer ()
        {
            if (raiz!=null)
            {
                char informacion = raiz.simbolo;
                raiz = raiz.sig;
                return informacion;
            }
            else
            {
                return Character.MAX_VALUE;
            }
        }  

        

        public boolean vacia() {
            if (raiz==null) {
                return true;
            } else {
                return false;
            }
        }
    }

    public static void main(String[] ar) {
        Examen ex=new Examen();
        ex.setBounds(0,0,500 ,300);
        ex.setVisible(true);
    }
}
