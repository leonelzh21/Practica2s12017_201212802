package Practica2;


import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Alejandro
 */
public class Conexion {
    public static OkHttpClient webClient = new OkHttpClient();
    
    public Conexion(){}
    
    public static String InsertarLista(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertarenLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    public static String eliminarLista(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
        URL url = new URL("http://0.0.0.0:5000/eliminarenLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    public static String buscarLista(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/buscarenLista");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    //aqui empiezan los metodos de la cola
    public static String queueenCola(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/queueCola");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    public static String dqueueenCola(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/dqueueCola");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    //aqui empiezan los metodos de la Pila 
    public static String pushenPila(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/pushPila");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    public static String popenPila(String dato){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/popPila");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
    
    public static String insertarMatriz(String dato,String dato2){
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", dato)
                .add("dato2",dato2)
                .build();
        try {
            URL url = new URL("http://0.0.0.0:5000/insertarenMatriz");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            System.out.println(ex.toString());
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
       return null;
    }
}
