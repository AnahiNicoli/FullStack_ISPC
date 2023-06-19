import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


export class Usuario 
{
  nombre:string="";
  apellido:string="";
  dni:string="";
  fechaNac:string="";
  celular:string="";
  mail:string="";
  password:string="";
  id:number=0;
  token: any;

  //acá ponemos los atributos del login. 
  
}

@Injectable({
  providedIn: 'root' 
 })

export class UsuarioService {

 url="http://regres.in/api/users/1";

 constructor(private http:HttpClient) { 
  console.log("servicio Usuarios funcionando");
 }

 //Acá va el método al que el componente se suscribe recibe un objeto
 //usuario como parámetro y devuelve un Obj Usuario modificado en el ID

 onCrearUsuario (usuario:Usuario): Observable<Usuario>{
  return this.http.post<Usuario>(this.url, usuario)
 }
}
