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
public class Progenitor {
    private int id_progenitor;
    private int edad_progenitor;
    private String nombre_progrenitor;
    private String apellido_p_progrenitor;
    private String apellido_m_progenitor;

    public Progenitor() {
    }

    public Progenitor(int id_progenitor, int edad_progenitor, String nombre_progrenitor, String apellido_p_progrenitor, String apellido_m_progenitor) {
        setId_progenitor(id_progenitor);
        setEdad_progenitor(edad_progenitor);
        setNombre_progrenitor(nombre_progrenitor);
        setApellido_p_progrenitor(apellido_p_progrenitor);
        setApellido_m_progenitor(apellido_m_progenitor);
    }

    public int getId_progenitor() {
        return id_progenitor;
    }

    public void setId_progenitor(int id_progenitor) {
        this.id_progenitor = id_progenitor;
    }

    public int getEdad_progenitor() {
        return edad_progenitor;
    }

    public void setEdad_progenitor(int edad_progenitor) {
        this.edad_progenitor = edad_progenitor;
    }

    public String getNombre_progrenitor() {
        return nombre_progrenitor;
    }

    public void setNombre_progrenitor(String nombre_progrenitor) {
        this.nombre_progrenitor = nombre_progrenitor;
    }

    public String getApellido_p_progrenitor() {
        return apellido_p_progrenitor;
    }

    public void setApellido_p_progrenitor(String apellido_p_progrenitor) {
        this.apellido_p_progrenitor = apellido_p_progrenitor;
    }

    public String getApellido_m_progenitor() {
        return apellido_m_progenitor;
    }

    public void setApellido_m_progenitor(String apellido_m_progenitor) {
        this.apellido_m_progenitor = apellido_m_progenitor;
    }
    
    
}
