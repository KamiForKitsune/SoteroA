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
public class Alcohol {
    private int id_alcohol;
    private String descrip_alcohol;
    private int grado_etilico;

    public Alcohol() {
    }

    public Alcohol(int id_alcohol, String descrip_alcohol, int grado_etilico) {
        setId_alcohol(id_alcohol);
        setDescrip_alcohol(descrip_alcohol);
        setGrado_etilico(grado_etilico);
    }
    

    public int getId_alcohol() {
        return id_alcohol;
    }

    public void setId_alcohol(int id_alcohol) {
        this.id_alcohol = id_alcohol;
    }

    public String getDescrip_alcohol() {
        return descrip_alcohol;
    }

    public void setDescrip_alcohol(String descrip_alcohol) {
        this.descrip_alcohol = descrip_alcohol;
    }

    public int getGrado_etilico() {
        return grado_etilico;
    }

    public void setGrado_etilico(int grado_etilico) {
        this.grado_etilico = grado_etilico;
    }
    
     
   
}
