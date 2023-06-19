import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Usuario, UsuarioService } from './usuario.service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class AuthService {

currentUserSubject: BehaviorSubject<Usuario>;
currentUser: Observable<Usuario>;
//loggedIn: BehaviorSubject<boolean>;


url="http://request.in/api/login"
  loggedIn: any;

  constructor(private http:HttpClient) { 
    console.log("Servicio de autenticación corriendo");

    this.currentUserSubject = new 
    BehaviorSubject<Usuario> (JSON.parse(localStorage.getItem('currentUser') || '{}'));
    this.currentUser = this.currentUserSubject.asObservable();
    //this.loggedIn: new BehaviorSubject<boolean> (false);
  }

  login(usuario: Usuario): Observable<any>{
    return this.http.post<any>(this.url, usuario)
    .pipe(map(data => {

      localStorage.setItem('currentUser', JSON.stringify(data));
      this.currentUserSubject.next(data);
   //en data va la api
      this.loggedIn.next(true);
      return data;
    })
    );
  }

logout(): void {
    localStorage.removeItem('currentUser');
    this.loggedIn.next(false);
  }


get usuarioAutenticado(): Usuario {
    return this.currentUserSubject.value;
  }

get estaAutenticado(): Observable<boolean> {

    return this.loggedIn.asObservable();
  }

}



   
//function logout() {
//  throw new Error('Function not implemented.');
//}

