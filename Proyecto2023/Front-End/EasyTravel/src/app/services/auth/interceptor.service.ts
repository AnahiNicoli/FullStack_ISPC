import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { AuthService } from './auth.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class JwtInterceptor implements HttpInterceptor {


  constructor(
    private authService:AuthService) { }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    const currentUser = this. authService.usuarioAutenticado;

    if (currentUser && currentUser.token) {
      req = req.clone({
        setHeaders: {
          Authorization: `Bearer ${currentUser.token}`
        }
      });
    }

      console.log("INTERCEPTOR:" + currentUser?.token);
      return next.handle(req);
  }
  
}
