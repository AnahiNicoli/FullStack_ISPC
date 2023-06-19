import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs';
import { map } from 'rxjs';
import { LoginService } from './login.service';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ErrorInterceptor implements HttpInterceptor {

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
      return next.handle(req).pipe(catchError(err => {
        if (err.status === 401) {
          location.reload();
        }

        const error = err.error.message || err.statusText;

        return throwError(error);
      }));
  }

  constructor() { }
}
