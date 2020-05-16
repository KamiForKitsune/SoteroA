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
public class Total_patologia {
    private int id_paciente;
    private int id_patologia;

    public Total_patologia() {
    }

    public Total_patologia(int id_paciente, int id_patologia) {
        setId_paciente(id_paciente);
        setId_patologia(id_patologia);
    }

    public int getId_paciente() {
        return id_paciente;
    }

    public void setId_paciente(int id_paciente) {
        this.id_paciente = id_paciente;
    }

    public int getId_patologia() {
        return id_patologia;
    }

    public void setId_patologia(int id_patologia) {
        this.id_patologia = id_patologia;
    }
    
}
