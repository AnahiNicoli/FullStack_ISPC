import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, catchError, throwError, BehaviorSubject, tap} from 'rxjs';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  currentUserLoginOn: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false);
  currentUserData: BehaviorSubject<User> = new BehaviorSubject<User>({id:0, email:''});
  //esto queda así hasta nuevo aviso, los valores son vacíos y no se guardan los datos para nuevas sesiones
//lo ideal es recuperar la info de la sesión del UserLoginOn
//Ahora llamamos al método next para que se informe a los componentes que puedan haberse suscripto
//lo trabajamos en "login"en el pipe (el operador tap, se usa para acciones adicionales)
  constructor(private http: HttpClient) { }

  login(Credentials:LoginRequest):Observable<User> {
  return this.http.get<User>('././assets/data.json').pipe(
    tap ((UserData: User) => { 
      this.currentUserData.next(UserData);
      this.currentUserLoginOn.next(true);
    }),
    catchError(this.handleError)
  );
  }

  private handleError(error:HttpErrorResponse){
    if(error.status===0){
      console.error('Se ha producido un error', error.error);
    }
    else{
      console.error('Backend retornó el código de estado ', error.status, error);
    }
    return throwError(()=> new Error ('Algo falló, intente nuevamente'));
  }

  get UserData():Observable<User>{
    return this.currentUserData.asObservable();
  }

  get UserLoginOn(): Observable<boolean>{
  return this.currentUserLoginOn.asObservable();
  }
}