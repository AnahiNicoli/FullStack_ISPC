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

  
  myCart$ = this.storeService.myCart$;

  viewCart : boolean = false;

  constructor(private storeService:StoreService) {}

  updateUnits(operation:string, id:string){
    const product = this.storeService.findProductById(id)
    if(product){
      if(operation === 'minus' && product.cantidad> 0){
      product.cantidad = product.cantidad - 1;
    }
    if (operation === 'add'){
      product.cantidad = product.cantidad + 1;
    }
    if(product.cantidad === 0){
      this.deleteProduct(id);
    }
  }

}

  ngOnInit(): void {
  }

  totalProduct(price:number, units: number){
    return price * units
  }

  deleteProduct(id:string){
    this.storeService.deleteProduct(id);
  }


totalCart(){
  const result = this.storeService.totalCart();
  return result
}

}