/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package TPV2doParcial;

import Pv2doParcial.Panel;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileFilter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JEditorPane;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.plaf.OptionPaneUI;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;
import javax.swing.tree.TreePath;


/**
 *
 * @author kiuub
 */
public class ExamenTaller extends javax.swing.JFrame {

    /**
     * Creates new form Practica1
     */
    private Panel e;
    private JFileChooser selector;
    private FileNameExtensionFilter filtro;
    private File archivo;
   private String rutaSeleccionada;
   
    
   
    public ExamenTaller() {
        initComponents();
        archivo = new File("C:\\Users\\kiuub\\OneDrive\\Documentos\\NetBeansProjects\\Progamacion visual");
        selector = new JFileChooser(new File("C:\\Users\\kiuub\\OneDrive\\Documentos\\NetBeansProjects\\Programacion visual"));
        filtro = new FileNameExtensionFilter("archivos planos", "txt", "java","xml");
        selector.addChoosableFileFilter(filtro);
    
       
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jToolBar1 = new javax.swing.JToolBar();
        jTabbedPane1 = new javax.swing.JTabbedPane();
        jPanel1 = new javax.swing.JPanel();
        btnNuevo = new javax.swing.JButton();
        btnAbrir = new javax.swing.JButton();
        btnGuardar = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();
        jPanel2 = new javax.swing.JPanel();
        button3 = new java.awt.Button();
        button4 = new java.awt.Button();
        tapContenedor = new javax.swing.JTabbedPane();
        jMenuBar1 = new javax.swing.JMenuBar();
        jMenu1 = new javax.swing.JMenu();
        jMenu2 = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setPreferredSize(new java.awt.Dimension(813, 500));

        jToolBar1.setRollover(true);

        jTabbedPane1.setPreferredSize(new java.awt.Dimension(800, 78));

        btnNuevo.setText("Crear archivo");
        btnNuevo.setToolTipText("Crear Nuevo");
        btnNuevo.setPreferredSize(new java.awt.Dimension(100, 40));
        btnNuevo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnNuevoActionPerformed(evt);
            }
        });
        jPanel1.add(btnNuevo);

        btnAbrir.setText("Abrir");
        btnAbrir.setToolTipText("Abrir");
        btnAbrir.setPreferredSize(new java.awt.Dimension(90, 40));
        btnAbrir.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAbrirActionPerformed(evt);
            }
        });
        jPanel1.add(btnAbrir);

        btnGuardar.setText("Guardar");
        btnGuardar.setToolTipText("Guardar");
        btnGuardar.setPreferredSize(new java.awt.Dimension(90, 40));
        btnGuardar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGuardarActionPerformed(evt);
            }
        });
        jPanel1.add(btnGuardar);

        jButton1.setText("Agregar cadena");
        jButton1.setPreferredSize(new java.awt.Dimension(109, 40));
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        jPanel1.add(jButton1);

        jTabbedPane1.addTab("tab1", jPanel1);

        button3.setLabel("button3");
        jPanel2.add(button3);

        button4.setLabel("button4");
        jPanel2.add(button4);

        jTabbedPane1.addTab("tab2", jPanel2);

        jToolBar1.add(jTabbedPane1);

        getContentPane().add(jToolBar1, java.awt.BorderLayout.PAGE_START);
        getContentPane().add(tapContenedor, java.awt.BorderLayout.CENTER);

        jMenu1.setText("File");
        jMenuBar1.add(jMenu1);

        jMenu2.setText("Edit");
        jMenuBar1.add(jMenu2);

        setJMenuBar(jMenuBar1);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnGuardarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGuardarActionPerformed
        // TODO add your handling code here:
        try{
            e = (Panel) tapContenedor.getSelectedComponent();
            String content = e.getjEditorPane1().getText();

            guardar(content);
        }catch(NullPointerException e){

        }
    }//GEN-LAST:event_btnGuardarActionPerformed

    private void btnAbrirActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAbrirActionPerformed
        // TODO add your handling code here:
        /*int seleccion = */

        //System.out.println(seleccion);
        try{
            selector.showOpenDialog(this);
            archivo = selector.getSelectedFile();
            System.out.println(archivo.getAbsolutePath());
            abrir(archivo);
        }catch(NullPointerException e){

        }
        /*
        BufferedReader br=null;
        try{

            br = new BufferedReader(new FileReader(archivo));
            String texto="";
            String cadena;
            while((cadena=br.readLine())!=null){
                texto+=cadena+"\n";
            }
            e=new Editor(archivo, texto);
            br.close();
        }catch(Exception ex){
            ex.printStackTrace();
        }
        tapContenedor.add(archivo.getName(),e);

        */
    }//GEN-LAST:event_btnAbrirActionPerformed

    private void btnNuevoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnNuevoActionPerformed
        // TODO add your handling code here:
        /*String nombre =  JOptionPane.showInputDialog(this, "¿Cual es el nombre del archivo? ");
        nombre = nombre.concat(".lsr");
        e =  new Editor(nombre);
        tapContenedor.add(nombre, e);
        */
        try{
            int resultado = selector.showSaveDialog(null);
            if (resultado == JFileChooser.APPROVE_OPTION) {
                String nombre = selector.getSelectedFile().getName();
                nombre = nombre.concat(".txt");//JOptionPane.showInputDialog(this, "¿Cuál es el nombre del archivo y su extensión?");

                if (nombre.contains("#") || nombre.contains("$") || nombre.contains("%") || nombre.contains("&")
                    || nombre.contains("/") || nombre.contains("(") || nombre.contains(")") || nombre.contains("=")
                    || nombre.contains("|") || nombre.contains("°") || nombre.contains("¬") || nombre.contains("@")
                    || nombre.contains("<") || nombre.contains(">") || nombre.contains("[") || nombre.contains("]")
                    || nombre.contains("{") || nombre.contains("}") || nombre.contains("+") || nombre.contains("*")
                    || nombre.contains("~")) {

                    JOptionPane.showMessageDialog(null, "No se permiten caracters especiales para el nombre de un archivo");

                } else {

                    e = new Panel(nombre);
                    tapContenedor.add(nombre, e);

                }

            }
        }catch(NullPointerException e){

        }
    }//GEN-LAST:event_btnNuevoActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
      
        Timestamp ts = new Timestamp(System.currentTimeMillis());
        String cadena = JOptionPane.showInputDialog(null, "Ingrese la cadena");
        cadena += " :: "+ ts;
        ArrayList <String> caracteres = new ArrayList<String>();
        
       try{
          int resultado = selector.showOpenDialog(null);
          if (resultado == JFileChooser.APPROVE_OPTION) {
                File f = selector.getSelectedFile();
                
            
                   caracteres.add( cadena);
              
       
      
        
        guardar(caracteres,f);
          }
       }catch(NullPointerException e){
           
       }
                
    }//GEN-LAST:event_jButton1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
             //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(ExamenTaller.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ExamenTaller.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ExamenTaller.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ExamenTaller.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new ExamenTaller().setVisible(true);
            }
        });
    }
    public void guardar(String content){
        try (FileWriter writer = new FileWriter(e.getArchivo().getName());
                BufferedWriter bw = new BufferedWriter(writer)) {
                bw.write(content);
                JOptionPane.showMessageDialog(this, "archivos guardados");
            } catch (IOException e) {
                System.err.format("IOException: %s%n", e);
            }
    }
     public void guardar(ArrayList <String> content, File archivo){
        try (FileWriter writer = new FileWriter(archivo);
                BufferedWriter bw = new BufferedWriter(writer)) {
                bw.write(content.toString());
                JOptionPane.showMessageDialog(this, "Cadena guardada");
            } catch (IOException e) {
                System.err.format("IOException: %s%n", e);
            }
    }
    public void abrir(File archivo){
        BufferedReader br=null;
       try{
           
           br = new BufferedReader(new FileReader(archivo));
           String texto="";
           String cadena;
           while((cadena=br.readLine())!=null){
               texto+=cadena+"\n";
           }
               e=new Panel(archivo, texto);
           br.close();
       }catch(Exception ex){
           ex.printStackTrace();
       }
     tapContenedor.add(archivo.getName(),e);
       
    }
    
    public void actualizarArbol(){
      
    }
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAbrir;
    private javax.swing.JButton btnGuardar;
    private javax.swing.JButton btnNuevo;
    private java.awt.Button button3;
    private java.awt.Button button4;
    private javax.swing.JButton jButton1;
    private javax.swing.JMenu jMenu1;
    private javax.swing.JMenu jMenu2;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JTabbedPane jTabbedPane1;
    private javax.swing.JToolBar jToolBar1;
    private javax.swing.JTabbedPane tapContenedor;
    // End of variables declaration//GEN-END:variables
}