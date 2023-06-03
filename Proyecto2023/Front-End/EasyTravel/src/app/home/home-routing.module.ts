import { NgModule } from '@angular/core';

import { LoginComponent } from './pages/login/login.component';

import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path:'',
    children:[
      { path:'login', component: LoginComponent}
     
    ]
  }
]


@NgModule({
  declarations: [],
  imports: [
    RouterModule.forChild (routes)
  ]
})
export class HomeRoutingModule { }
