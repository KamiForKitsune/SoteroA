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
public class Causa_Parto {
    private int id_parto;
    private int descrip_parto;

    public Causa_Parto() {
    }

    public Causa_Parto(int id_parto, int descrip_parto) {
        setId_parto(id_parto);
        setDescrip_parto(descrip_parto);
    }

    public int getId_parto() {
        return id_parto;
    }

    public void setId_parto(int id_parto) {
        this.id_parto = id_parto;
    }

    public int getDescrip_parto() {
        return descrip_parto;
    }

    public void setDescrip_parto(int descrip_parto) {
        this.descrip_parto = descrip_parto;
    }
    
    
}
