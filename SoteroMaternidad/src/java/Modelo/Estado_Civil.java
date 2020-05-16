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
public class Estado_Civil {
    private int id_estado_civil;
    private String descrip_civil;

    public Estado_Civil() {
    }

    public Estado_Civil(int id_estado_civil, String descrip_civil) {
        setId_estado_civil(id_estado_civil);
        setDescrip_civil(descrip_civil);
    }

    public int getId_estado_civil() {
        return id_estado_civil;
    }

    public void setId_estado_civil(int id_estado_civil) {
        this.id_estado_civil = id_estado_civil;
    }

    public String getDescrip_civil() {
        return descrip_civil;
    }

    public void setDescrip_civil(String descrip_civil) {
        this.descrip_civil = descrip_civil;
    }
    
}
