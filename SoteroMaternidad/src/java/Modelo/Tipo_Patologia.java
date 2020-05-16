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
public class Tipo_Patologia {
    private int id_tipo_patologia;
    private String descrip_tipo_pat;

    public Tipo_Patologia() {
    }

    public Tipo_Patologia(int id_tipo_patologia, String descrip_tipo_pat) {
        setId_tipo_patologia(id_tipo_patologia);
        setDescrip_tipo_pat(descrip_tipo_pat);
    }

    public int getId_tipo_patologia() {
        return id_tipo_patologia;
    }

    public void setId_tipo_patologia(int id_tipo_patologia) {
        this.id_tipo_patologia = id_tipo_patologia;
    }

    public String getDescrip_tipo_pat() {
        return descrip_tipo_pat;
    }

    public void setDescrip_tipo_pat(String descrip_tipo_pat) {
        this.descrip_tipo_pat = descrip_tipo_pat;
    }
    
}
