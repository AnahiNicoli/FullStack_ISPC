import { Component, OnDestroy, OnInit } from '@angular/core';
import { LoginService } from '../services/auth/login.service';
import { User } from '../services/auth/user';

@Component({
  selector: 'app-filtro',
  templateUrl: './filtro.component.html',
  styleUrls: ['./filtro.component.css']
})
export class FiltroComponent implements OnInit, OnDestroy {
  userLoginOn:boolean=true;
  userData?:User;
constructor(private loginService:LoginService){}

ngOnDestroy(): void {
  this.loginService.currentUserData.unsubscribe();
}

ngOnInit(): void {
    this.loginService.currentUserLoginOn.subscribe({
      next: (userLoginOn) => {
        this.userLoginOn=userLoginOn;
      }
    });

    this.loginService.currentUserData.subscribe({
      next:(userData) =>{
        this.userData=this.userData;
      }
    })
}
}
