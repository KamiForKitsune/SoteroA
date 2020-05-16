/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Modelo;

import java.util.Date;

/**
 *
 * @author Kami
 */
public class Paciente {
    private int id_paciente;
    private int rut_paciente;
    private int dv_paciente;
    private Date fecha_nacimiento_paciente;
    private String nombre_paciente;
    private String apellido_paterno_paciente;
    private String apellido_materno_paciente;
    private String telefono_paciente;

    public Paciente() {
    }

    public Paciente(int id_paciente, int rut_paciente, int dv_paciente, Date fecha_nacimiento_paciente, String nombre_paciente, String apellido_paterno_paciente, String apellido_materno_paciente, String telefono_paciente) {
        setId_paciente(id_paciente);
        setRut_paciente(rut_paciente);
        setDv_paciente(dv_paciente);
        setFecha_nacimiento_paciente(fecha_nacimiento_paciente);
        setNombre_paciente(nombre_paciente);
        setApellido_paterno_paciente(apellido_paterno_paciente);
        setApellido_materno_paciente(apellido_materno_paciente);
        setTelefono_paciente(telefono_paciente);
    }

    public int getId_paciente() {
        return id_paciente;
    }

    public void setId_paciente(int id_paciente) {
        this.id_paciente = id_paciente;
    }

    public int getRut_paciente() {
        return rut_paciente;
    }

    public void setRut_paciente(int rut_paciente) {
        this.rut_paciente = rut_paciente;
    }

    public int getDv_paciente() {
        return dv_paciente;
    }

    public void setDv_paciente(int dv_paciente) {
        this.dv_paciente = dv_paciente;
    }

    public Date getFecha_nacimiento_paciente() {
        return fecha_nacimiento_paciente;
    }

    public void setFecha_nacimiento_paciente(Date fecha_nacimiento_paciente) {
        this.fecha_nacimiento_paciente = fecha_nacimiento_paciente;
    }

    public String getNombre_paciente() {
        return nombre_paciente;
    }

    public void setNombre_paciente(String nombre_paciente) {
        this.nombre_paciente = nombre_paciente;
    }

    public String getApellido_paterno_paciente() {
        return apellido_paterno_paciente;
    }

    public void setApellido_paterno_paciente(String apellido_paterno_paciente) {
        this.apellido_paterno_paciente = apellido_paterno_paciente;
    }

    public String getApellido_materno_paciente() {
        return apellido_materno_paciente;
    }

    public void setApellido_materno_paciente(String apellido_materno_paciente) {
        this.apellido_materno_paciente = apellido_materno_paciente;
    }

    public String getTelefono_paciente() {
        return telefono_paciente;
    }

    public void setTelefono_paciente(String telefono_paciente) {
        this.telefono_paciente = telefono_paciente;
    }
    
}
