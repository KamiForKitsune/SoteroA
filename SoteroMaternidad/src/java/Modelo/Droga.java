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
public class Droga {
    private int id_droga;
    private String descrip_droga;

    public Droga() {
    }

    public Droga(int id_droga, String descrip_droga) {
        setId_droga(id_droga);
        setDescrip_droga(descrip_droga);
    }

    public int getId_droga() {
        return id_droga;
    }

    public void setId_droga(int id_droga) {
        this.id_droga = id_droga;
    }

    public String getDescrip_droga() {
        return descrip_droga;
    }

    public void setDescrip_droga(String descrip_droga) {
        this.descrip_droga = descrip_droga;
    }
    
}
