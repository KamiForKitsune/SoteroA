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
public class Grupo_Sanguineo {
    private int id_grupo;
    private String descrip_grupo;

    public Grupo_Sanguineo() {
    }

    public Grupo_Sanguineo(int id_grupo, String descrip_grupo) {
        setId_grupo(id_grupo);
        setDescrip_grupo(descrip_grupo);
    }

    public int getId_grupo() {
        return id_grupo;
    }

    public void setId_grupo(int id_grupo) {
        this.id_grupo = id_grupo;
    }

    public String getDescrip_grupo() {
        return descrip_grupo;
    }

    public void setDescrip_grupo(String descrip_grupo) {
        this.descrip_grupo = descrip_grupo;
    }
    
    
}
