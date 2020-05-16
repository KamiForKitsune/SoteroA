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
public class Tipo_emb_Previo {
    private int id_tipo_emb_previo;
    private String descrip_tipo_emb;
    private String rn_otra_malform;

    public Tipo_emb_Previo() {
    }

    public Tipo_emb_Previo(int id_tipo_emb_previo, String descrip_tipo_emb, String rn_otra_malform) {
        setId_tipo_emb_previo(id_tipo_emb_previo);
        setDescrip_tipo_emb(descrip_tipo_emb);
        setRn_otra_malform(rn_otra_malform);
    }

    public int getId_tipo_emb_previo() {
        return id_tipo_emb_previo;
    }

    public void setId_tipo_emb_previo(int id_tipo_emb_previo) {
        this.id_tipo_emb_previo = id_tipo_emb_previo;
    }

    public String getDescrip_tipo_emb() {
        return descrip_tipo_emb;
    }

    public void setDescrip_tipo_emb(String descrip_tipo_emb) {
        this.descrip_tipo_emb = descrip_tipo_emb;
    }

    public String getRn_otra_malform() {
        return rn_otra_malform;
    }

    public void setRn_otra_malform(String rn_otra_malform) {
        this.rn_otra_malform = rn_otra_malform;
    }
    
    
}
