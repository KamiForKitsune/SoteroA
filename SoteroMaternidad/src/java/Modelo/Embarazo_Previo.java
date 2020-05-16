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
public class Embarazo_Previo {
     private int id_emb_previo;
     private int aborto_espontaneo;
     private int aborto_provocado; 
     private int parto_prematuro; 
     private int parto_termino;
     private int peso_rn_mayor_peso;
     private int muerte_natural;
     private int muerte_neonatal; 
     private int embarazo_ectopico;
     private int hijos_vivos;
     private int cesareas_previas; 
     private int embarazos_gemelares;

    public Embarazo_Previo() {
    }

    public Embarazo_Previo(int id_emb_previo, int aborto_espontaneo, int aborto_provocado, int parto_prematuro, int parto_termino, int peso_rn_mayor_peso, int muerte_natural, int muerte_neonatal, int embarazo_ectopico, int hijos_vivos, int cesareas_previas, int embarazos_gemelares) {
        setId_emb_previo(id_emb_previo);
        setAborto_espontaneo(aborto_espontaneo);
        setAborto_provocado(aborto_provocado);
        setParto_prematuro(parto_prematuro);
        setParto_termino(parto_termino);
        setPeso_rn_mayor_peso(peso_rn_mayor_peso);
        setMuerte_natural(muerte_natural);
        setMuerte_neonatal(muerte_neonatal);
        setEmbarazo_ectopico(embarazo_ectopico);
        setHijos_vivos(hijos_vivos);
        setCesareas_previas(cesareas_previas);
        setEmbarazos_gemelares(embarazos_gemelares);
    
    }

    public int getId_emb_previo() {
        return id_emb_previo;
    }

    public void setId_emb_previo(int id_emb_previo) {
        this.id_emb_previo = id_emb_previo;
    }

    public int getAborto_espontaneo() {
        return aborto_espontaneo;
    }

    public void setAborto_espontaneo(int aborto_espontaneo) {
        this.aborto_espontaneo = aborto_espontaneo;
    }

    public int getAborto_provocado() {
        return aborto_provocado;
    }

    public void setAborto_provocado(int aborto_provocado) {
        this.aborto_provocado = aborto_provocado;
    }

    public int getParto_prematuro() {
        return parto_prematuro;
    }

    public void setParto_prematuro(int parto_prematuro) {
        this.parto_prematuro = parto_prematuro;
    }

    public int getParto_termino() {
        return parto_termino;
    }

    public void setParto_termino(int parto_termino) {
        this.parto_termino = parto_termino;
    }

    public int getPeso_rn_mayor_peso() {
        return peso_rn_mayor_peso;
    }

    public void setPeso_rn_mayor_peso(int peso_rn_mayor_peso) {
        this.peso_rn_mayor_peso = peso_rn_mayor_peso;
    }

    public int getMuerte_natural() {
        return muerte_natural;
    }

    public void setMuerte_natural(int muerte_natural) {
        this.muerte_natural = muerte_natural;
    }

    public int getMuerte_neonatal() {
        return muerte_neonatal;
    }

    public void setMuerte_neonatal(int muerte_neonatal) {
        this.muerte_neonatal = muerte_neonatal;
    }

    public int getEmbarazo_ectopico() {
        return embarazo_ectopico;
    }

    public void setEmbarazo_ectopico(int embarazo_ectopico) {
        this.embarazo_ectopico = embarazo_ectopico;
    }

    public int getHijos_vivos() {
        return hijos_vivos;
    }

    public void setHijos_vivos(int hijos_vivos) {
        this.hijos_vivos = hijos_vivos;
    }

    public int getCesareas_previas() {
        return cesareas_previas;
    }

    public void setCesareas_previas(int cesareas_previas) {
        this.cesareas_previas = cesareas_previas;
    }

    public int getEmbarazos_gemelares() {
        return embarazos_gemelares;
    }

    public void setEmbarazos_gemelares(int embarazos_gemelares) {
        this.embarazos_gemelares = embarazos_gemelares;
    }
     
}
