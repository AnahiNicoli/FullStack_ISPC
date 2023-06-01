import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginComponent } from './pages/login/login.component';
import { HomeRoutingModule } from './home-routing.module';



@NgModule({
  declarations: [
   
    LoginComponent
   
  ],
  imports: [
    CommonModule,
    HomeRoutingModule
  ]
})
export class HomeModule { }
