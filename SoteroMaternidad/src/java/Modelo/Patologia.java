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
public class Patologia {
    
    private int id_patologia;
    private String descripc_patologia;

    public Patologia() {
    }

    public Patologia(int id_patologia, String descripc_patologia) {
        setId_patologia(id_patologia);
        setDescripc_patologia(descripc_patologia);
    }

    public int getId_patologia() {
        return id_patologia;
    }

    public void setId_patologia(int id_patologia) {
        this.id_patologia = id_patologia;
    }

    public String getDescripc_patologia() {
        return descripc_patologia;
    }

    public void setDescripc_patologia(String descripc_patologia) {
        this.descripc_patologia = descripc_patologia;
    }
    
    
}
