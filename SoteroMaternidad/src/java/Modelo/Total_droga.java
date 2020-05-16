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
public class Total_droga {
    private int id_droga;
    private int id_embarazo;
    private int cant_drogas;

    public Total_droga() {
    }

    public Total_droga(int id_droga, int id_embarazo, int cant_drogas) {
        setId_droga(id_droga);
        setId_embarazo(id_embarazo);
        setCant_drogas(cant_drogas);
    }

    public int getId_droga() {
        return id_droga;
    }

    public void setId_droga(int id_droga) {
        this.id_droga = id_droga;
    }

    public int getId_embarazo() {
        return id_embarazo;
    }

    public void setId_embarazo(int id_embarazo) {
        this.id_embarazo = id_embarazo;
    }

    public int getCant_drogas() {
        return cant_drogas;
    }

    public void setCant_drogas(int cant_drogas) {
        this.cant_drogas = cant_drogas;
    }
    
}
