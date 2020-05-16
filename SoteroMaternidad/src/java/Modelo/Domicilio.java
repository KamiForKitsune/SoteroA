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
public class Domicilio {
    private int id_domicilio ;
    private int numero_direccion;
    private String direccion;
    private String poblacion_barrio;

    public Domicilio() {
    }

    public Domicilio(int id_domicilio, int numero_direccion, String direccion, String poblacion_barrio) {
        setId_domicilio(id_domicilio);
        setNumero_direccion(numero_direccion);
        setDireccion(direccion);
        setPoblacion_barrio(poblacion_barrio);
    }

    public int getId_domicilio() {
        return id_domicilio;
    }

    public void setId_domicilio(int id_domicilio) {
        this.id_domicilio = id_domicilio;
    }

    public int getNumero_direccion() {
        return numero_direccion;
    }

    public void setNumero_direccion(int numero_direccion) {
        this.numero_direccion = numero_direccion;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getPoblacion_barrio() {
        return poblacion_barrio;
    }

    public void setPoblacion_barrio(String poblacion_barrio) {
        this.poblacion_barrio = poblacion_barrio;
    }
    
}
