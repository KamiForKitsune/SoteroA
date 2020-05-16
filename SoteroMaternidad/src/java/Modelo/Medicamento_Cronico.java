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
public class Medicamento_Cronico {
    
    private int id_listado_medicamento;
    private String ocacion;
    private int id_nombre_med;

    public Medicamento_Cronico(int id_listado_medicamento, String ocacion, int id_nombre_med) {
        setId_listado_medicamento(id_listado_medicamento);
        setOcacion(ocacion);
        setId_nombre_med(id_nombre_med);
    }

    public Medicamento_Cronico() {
    }

    public int getId_listado_medicamento() {
        return id_listado_medicamento;
    }

    public void setId_listado_medicamento(int id_listado_medicamento) {
        this.id_listado_medicamento = id_listado_medicamento;
    }

    public String getOcacion() {
        return ocacion;
    }

    public void setOcacion(String ocacion) {
        this.ocacion = ocacion;
    }

    public int getId_nombre_med() {
        return id_nombre_med;
    }

    public void setId_nombre_med(int id_nombre_med) {
        this.id_nombre_med = id_nombre_med;
    }

    

    
}
