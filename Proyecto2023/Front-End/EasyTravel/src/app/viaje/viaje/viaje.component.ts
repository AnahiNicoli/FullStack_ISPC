import { Component, OnInit } from '@angular/core';
import { Product } from 'src/app/pages/products/product.interface';
import { StoreService } from 'src/app/services/auth/store.service';

@Component({
  selector: 'app-viaje',
  templateUrl: './viaje.component.html',
  styleUrls: ['./viaje.component.css']
})
export class ViajeComponent implements OnInit {

products:Product[]=[];

  constructor(private storeService:StoreService) { }
  
  ngOnInit(): void{
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

