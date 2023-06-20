import { Component, OnInit } from '@angular/core';
import { Product } from './product.interface';
//import { CarritoService } from 'src/app/services/auth/carrito.service';
import { StoreService } from 'src/app/services/auth/store.service';


@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css'] 
})
export class ProductsComponent implements OnInit {

//creo un array para que me importe acá

products:Product[]=[];

constructor (private storeService: StoreService) { }
//carritoService: CarritoService,

ngOnInit(): void {
  this.storeService.getAllProducts().subscribe((data)=>{
    this.products = data;
    console.log(this.products);
  })
    
}


}