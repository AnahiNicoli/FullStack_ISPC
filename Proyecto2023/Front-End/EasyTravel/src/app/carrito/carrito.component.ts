import { Component, OnInit } from '@angular/core';
import { StoreService } from '../services/auth/store.service';
import { Product } from '../pages/products/product.interface';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {

  products:Product[]=[];

  constructor(private storeService: StoreService) {}

  ngOnInit(): void {

    this.getProducts();
  }

//Método para traer la lista de productos
getProducts(){
  this.storeService.getAllProducts().subscribe((data)=>
  {
    return this.products = data;
  })
}

addToCart(product:Product){
  return this.storeService.addProduct(product);
}
}
