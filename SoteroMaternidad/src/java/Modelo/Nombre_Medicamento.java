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
public class Nombre_Medicamento {
    private int id_nombre_med;
    private String nombre_medicamento;

    public Nombre_Medicamento() {
    }

    public Nombre_Medicamento(int id_nombre_med, String nombre_medicamento) {
        setId_nombre_med(id_nombre_med);
        setNombre_medicamento(nombre_medicamento);
    }

    public int getId_nombre_med() {
        return id_nombre_med;
    }

    public void setId_nombre_med(int id_nombre_med) {
        this.id_nombre_med = id_nombre_med;
    }

    public String getNombre_medicamento() {
        return nombre_medicamento;
    }

    public void setNombre_medicamento(String nombre_medicamento) {
        this.nombre_medicamento = nombre_medicamento;
    }
    
}
