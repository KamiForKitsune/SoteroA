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
public class Comentario {
     private int id_comentario;
    private String comentario;

    public Comentario() {
    }

    public Comentario(int id_comentario, String comentario) {
        setId_comentario(id_comentario);
        setComentario(comentario);
    }
    
   
    public int getId_comentario() {
        return id_comentario;
    }

    public void setId_comentario(int id_comentario) {
        this.id_comentario = id_comentario;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }
    
}
