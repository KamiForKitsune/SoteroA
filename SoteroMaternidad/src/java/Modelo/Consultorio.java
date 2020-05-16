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
public class Consultorio {
    private int id_consultorio;
    private String nombre_consultorio;
    private String direccion_consultorio;

    public Consultorio() {
    }

    public Consultorio(int id_consultorio, String nombre_consultorio, String direccion_consultorio) {
        setId_consultorio(id_consultorio);
        setNombre_consultorio(nombre_consultorio);
        setDireccion_consultorio(direccion_consultorio);
    }

    public int getId_consultorio() {
        return id_consultorio;
    }

    public void setId_consultorio(int id_consultorio) {
        this.id_consultorio = id_consultorio;
    }

    public String getNombre_consultorio() {
        return nombre_consultorio;
    }

    public void setNombre_consultorio(String nombre_consultorio) {
        this.nombre_consultorio = nombre_consultorio;
    }

    public String getDireccion_consultorio() {
        return direccion_consultorio;
    }

    public void setDireccion_consultorio(String direccion_consultorio) {
        this.direccion_consultorio = direccion_consultorio;
    }
    
}
