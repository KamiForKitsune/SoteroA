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
public class Total_Alcohol {
    
    private int id_alcohol;
    private int id_embarazo;

    public Total_Alcohol() {
    }

    public Total_Alcohol(int id_alcohol, int id_embarazo) {
        setId_embarazo(id_embarazo);
        setId_alcohol(id_alcohol);
    }

    public int getId_alcohol() {
        return id_alcohol;
    }

    public void setId_alcohol(int id_alcohol) {
        this.id_alcohol = id_alcohol;
    }

    public int getId_embarazo() {
        return id_embarazo;
    }

    public void setId_embarazo(int id_embarazo) {
        this.id_embarazo = id_embarazo;
    }
    
}
