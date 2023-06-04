import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor() { }

  login(Credentials:LoginRequest) {
    console.log(Credentials);

  }
}
