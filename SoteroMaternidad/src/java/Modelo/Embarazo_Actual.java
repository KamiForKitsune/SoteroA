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
public class Embarazo_Actual {
    private int id_embarazo; 
    private int talla_madre;
    private int peso_madre;
    private int imc;
    private int semana_gestacion;
    private int numero_controles;
    private int edad_gestac_eco;
    private int numero_cigarrillos;
    private Date fecha_ingreso;
    private Date f_ultima_regla;
    private Date fecha_ecografia;
    private Date fur_operacional;
    private char fur_confiable;
    private char gemelar;

    public Embarazo_Actual() {
    }

    public Embarazo_Actual(int id_embarazo, int talla_madre, int peso_madre, int imc, int semana_gestacion, int numero_controles, int edad_gestac_eco, int numero_cigarrillos, Date fecha_ingreso, Date f_ultima_regla, Date fecha_ecografia, Date fur_operacional, char fur_confiable, char gemelar) {
        setId_embarazo(id_embarazo);
        setTalla_madre(talla_madre);
        setPeso_madre(peso_madre);
        setImc(imc);
        setSemana_gestacion(semana_gestacion);
        setNumero_controles(numero_controles);
        setEdad_gestac_eco(edad_gestac_eco);
        setNumero_cigarrillos(numero_cigarrillos);
        setFecha_ingreso(fecha_ingreso);
        setF_ultima_regla(f_ultima_regla);
        setFecha_ecografia(fecha_ecografia);
        setFur_operacional(fur_operacional);
        setFur_confiable(fur_confiable);
        setGemelar(gemelar);
    }

    public int getId_embarazo() {
        return id_embarazo;
    }

    public void setId_embarazo(int id_embarazo) {
        this.id_embarazo = id_embarazo;
    }

    public int getTalla_madre() {
        return talla_madre;
    }

    public void setTalla_madre(int talla_madre) {
        this.talla_madre = talla_madre;
    }

    public int getPeso_madre() {
        return peso_madre;
    }

    public void setPeso_madre(int peso_madre) {
        this.peso_madre = peso_madre;
    }

    public int getImc() {
        return imc;
    }

    public void setImc(int imc) {
        this.imc = imc;
    }

    public int getSemana_gestacion() {
        return semana_gestacion;
    }

    public void setSemana_gestacion(int semana_gestacion) {
        this.semana_gestacion = semana_gestacion;
    }

    public int getNumero_controles() {
        return numero_controles;
    }

    public void setNumero_controles(int numero_controles) {
        this.numero_controles = numero_controles;
    }

    public int getEdad_gestac_eco() {
        return edad_gestac_eco;
    }

    public void setEdad_gestac_eco(int edad_gestac_eco) {
        this.edad_gestac_eco = edad_gestac_eco;
    }

    public int getNumero_cigarrillos() {
        return numero_cigarrillos;
    }

    public void setNumero_cigarrillos(int numero_cigarrillos) {
        this.numero_cigarrillos = numero_cigarrillos;
    }

    public Date getFecha_ingreso() {
        return fecha_ingreso;
    }

    public void setFecha_ingreso(Date fecha_ingreso) {
        this.fecha_ingreso = fecha_ingreso;
    }

    public Date getF_ultima_regla() {
        return f_ultima_regla;
    }

    public void setF_ultima_regla(Date f_ultima_regla) {
        this.f_ultima_regla = f_ultima_regla;
    }

    public Date getFecha_ecografia() {
        return fecha_ecografia;
    }

    public void setFecha_ecografia(Date fecha_ecografia) {
        this.fecha_ecografia = fecha_ecografia;
    }

    public Date getFur_operacional() {
        return fur_operacional;
    }

    public void setFur_operacional(Date fur_operacional) {
        this.fur_operacional = fur_operacional;
    }

    public char getFur_confiable() {
        return fur_confiable;
    }

    public void setFur_confiable(char fur_confiable) {
        this.fur_confiable = fur_confiable;
    }

    public char getGemelar() {
        return gemelar;
    }

    public void setGemelar(char gemelar) {
        this.gemelar = gemelar;
    }
    
    
}
