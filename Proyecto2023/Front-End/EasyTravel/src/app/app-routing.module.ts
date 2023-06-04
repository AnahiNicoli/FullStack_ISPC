import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { LoginComponent } from './login/login/login.component';
import { PerfilComponent } from './perfil/perfil.component';
import { CarritoComponent } from './carrito/carrito.component';
import { ContactanosComponent } from './contactanos/contactanos/contactanos.component';
import { ResultadosFiltroComponent } from './pages/resultados-filtro/resultados-filtro.component';
import { FiltroComponent } from './filtro/filtro.component';
import { ProductsComponent } from './pages/products/products.component';
import { EmpresaComponent } from './pages/empresa/empresa.component';

const routes: Routes = [
  { path:'', redirectTo:'/inicio', pathMatch:'full'},
  { path:'inicio', component:DashboardComponent},
  { path:'login', component:LoginComponent},
  { path:'perfil', component:PerfilComponent},
  { path:'carrito', component:CarritoComponent},
  { path:'resultados', component:ResultadosFiltroComponent},
  { path:'filtro', component:FiltroComponent},
  { path:'productos', component:ProductsComponent},
  { path:'empresa', component:EmpresaComponent},
  { path:'contactanos', component:ContactanosComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
