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
public class Anticonceptivo {
    private int id_conceptivo;
    private String descripc_anticonceptivo;

    public Anticonceptivo() {
    }

    public Anticonceptivo(int id_conceptivo, String descripc_anticonceptivo) {
        setId_conceptivo(id_conceptivo);
        setDescripc_anticonceptivo(descripc_anticonceptivo);
    }

    public int getId_conceptivo() {
        return id_conceptivo;
    }

    public void setId_conceptivo(int id_conceptivo) {
        this.id_conceptivo = id_conceptivo;
    }

    public String getDescripc_anticonceptivo() {
        return descripc_anticonceptivo;
    }

    public void setDescripc_anticonceptivo(String descripc_anticonceptivo) {
        this.descripc_anticonceptivo = descripc_anticonceptivo;
    }
    
    
}
