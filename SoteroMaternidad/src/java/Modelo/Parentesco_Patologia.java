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
public class Parentesco_Patologia {
    private int id_parentesco_pat;
    private String descrip_parentesco;

    public Parentesco_Patologia() {
    }

    public Parentesco_Patologia(int id_parentesco_pat, String descrip_parentesco) {
        setId_parentesco_pat(id_parentesco_pat);
        setDescrip_parentesco(descrip_parentesco);
    }

    public int getId_parentesco_pat() {
        return id_parentesco_pat;
    }

    public void setId_parentesco_pat(int id_parentesco_pat) {
        this.id_parentesco_pat = id_parentesco_pat;
    }

    public String getDescrip_parentesco() {
        return descrip_parentesco;
    }

    public void setDescrip_parentesco(String descrip_parentesco) {
        this.descrip_parentesco = descrip_parentesco;
    }
    
}
