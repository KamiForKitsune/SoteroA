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
public class Actividad {
    private int id_actividad;
    private String descrip_actividad;

    public Actividad() {
    }

    public Actividad(int id_actividad, String descrip_actividad) {
        setId_actividad(id_actividad);
        setDescrip_actividad(descrip_actividad);
    }
    
    

    public int getId_actividad() {
        return id_actividad;
    }

    public void setId_actividad(int id_actividad) {
        this.id_actividad = id_actividad;
    }

    public String getDescrip_actividad() {
        return descrip_actividad;
    }

    public void setDescrip_actividad(String descrip_actividad) {
        this.descrip_actividad = descrip_actividad;
    }
    
}
