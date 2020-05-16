/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

/**
 *
 * @author Kami
 */
public class Prevision {
    private int id_prevision;
    private String nombre_prevision;

    public Prevision() {
    }

    public Prevision(int id_prevision, String nombre_prevision) {
        setId_prevision(id_prevision);
        setNombre_prevision(nombre_prevision);
    }

    public int getId_prevision() {
        return id_prevision;
    }

    public void setId_prevision(int id_prevision) {
        this.id_prevision = id_prevision;
    }

    public String getNombre_prevision() {
        return nombre_prevision;
    }

    public void setNombre_prevision(String nombre_prevision) {
        this.nombre_prevision = nombre_prevision;
    }
    
    
}
