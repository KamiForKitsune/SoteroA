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
public class Nivel_Estudio {
    private int id_nivel_estudio;
    private String descrip_estudio;

    public Nivel_Estudio() {
    }

    public Nivel_Estudio(int id_nivel_estudio, String descrip_estudio) {
        setId_nivel_estudio(id_nivel_estudio);
        setDescrip_estudio(descrip_estudio);
    }

    public int getId_nivel_estudio() {
        return id_nivel_estudio;
    }

    public void setId_nivel_estudio(int id_nivel_estudio) {
        this.id_nivel_estudio = id_nivel_estudio;
    }

    public String getDescrip_estudio() {
        return descrip_estudio;
    }

    public void setDescrip_estudio(String descrip_estudio) {
        this.descrip_estudio = descrip_estudio;
    }
    
}
