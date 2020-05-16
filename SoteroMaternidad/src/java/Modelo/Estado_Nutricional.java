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
public class Estado_Nutricional {
    private int id_estado_nutricional;
    private String descrip_nutricional;

    public Estado_Nutricional() {
    }

    public Estado_Nutricional(int id_estado_nutricional, String descrip_nutricional) {
        setId_estado_nutricional(id_estado_nutricional);
        setDescrip_nutricional(descrip_nutricional);
    }

    public int getId_estado_nutricional() {
        return id_estado_nutricional;
    }

    public void setId_estado_nutricional(int id_estado_nutricional) {
        this.id_estado_nutricional = id_estado_nutricional;
    }

    public String getDescrip_nutricional() {
        return descrip_nutricional;
    }

    public void setDescrip_nutricional(String descrip_nutricional) {
        this.descrip_nutricional = descrip_nutricional;
    }
    
}
