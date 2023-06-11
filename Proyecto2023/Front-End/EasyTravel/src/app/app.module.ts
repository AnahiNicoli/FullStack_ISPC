import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CabeceraComponent } from './cabecera/cabecera.component';
import { MenuComponent } from './menu/menu.component';
import { FiltroComponent } from './filtro/filtro.component';
import { CuerpoComponent } from './cuerpo/cuerpo.component';
import { PieComponent } from './pie/pie.component';
import { DestacadosComponent } from './destacados/destacados.component';
import { LogoETComponent } from './logo/logo-et/logo-et.component';
import { CarruselComponent } from './carrusel/carrusel/carrusel.component';
import { ProductosComponent } from './productos/productos/productos.component';
import { EmpresasComponent } from './empresas/empresas/empresas.component';
import { ContactanosComponent } from './contactanos/contactanos/contactanos.component';
import { CarritoComponent } from './carrito/carrito.component';
import { CarritoTotalComponent } from './carritoTotal/carrito-total/carrito-total.component';
import { CarritoPagarComponent } from './carritoPagar/carrito-pagar/carrito-pagar.component';
import { PerfilComponent } from './perfil/perfil.component';
import { LoginComponent } from './login/login/login.component';
import { RegistroComponent } from './login/registro/registro.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { ResultadosFiltroComponent } from './pages/resultados-filtro/resultados-filtro.component';
import { productsComponent } from './pages/products/products.component';
import { EmpresaComponent } from './pages/empresa/empresa.component';
import { ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    CabeceraComponent,
    MenuComponent,
    FiltroComponent,
    CuerpoComponent,
    PieComponent,
    DestacadosComponent,
    LogoETComponent,
    CarruselComponent,
    ProductosComponent,
    EmpresasComponent,
    ContactanosComponent,
    CarritoComponent,
    CarritoTotalComponent,
    CarritoPagarComponent,
    PerfilComponent,
    LoginComponent,
    RegistroComponent,
    DashboardComponent,
    ResultadosFiltroComponent,
    productsComponent,
    EmpresaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }