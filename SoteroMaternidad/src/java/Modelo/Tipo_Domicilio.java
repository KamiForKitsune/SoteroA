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
public class Tipo_Domicilio {
    private int id_tipo_domicilio;
    private String descrip_tipo_dom;

    public Tipo_Domicilio() {
    }

    public Tipo_Domicilio(int id_tipo_domicilio, String descrip_tipo_dom) {
        setId_tipo_domicilio(id_tipo_domicilio);
        setDescrip_tipo_dom(descrip_tipo_dom);
    }

    public int getId_tipo_domicilio() {
        return id_tipo_domicilio;
    }

    public void setId_tipo_domicilio(int id_tipo_domicilio) {
        this.id_tipo_domicilio = id_tipo_domicilio;
    }

    public String getDescrip_tipo_dom() {
        return descrip_tipo_dom;
    }

    public void setDescrip_tipo_dom(String descrip_tipo_dom) {
        this.descrip_tipo_dom = descrip_tipo_dom;
    }
    
}
