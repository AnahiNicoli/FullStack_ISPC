import { Component, OnDestroy, OnInit } from '@angular/core';
import { LoginService } from '../services/auth/login.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit, OnDestroy{

  mostrarCart: boolean = false;

  userLoginOn:boolean=false 
  constructor (private loginService:LoginService) {}

ngOnDestroy(): void {
    this.loginService.currentUserLoginOn.unsubscribe();
}

ngOnInit(): void {
    this.loginService.currentUserLoginOn.subscribe(
      {
      next:(userLoginOn) => {
        this.userLoginOn=userLoginOn;
      }
    }
  )
}

onToggleCart(){
  this.mostrarCart = !this.mostrarCart
}

}
