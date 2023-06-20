import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Product } from 'src/app/pages/products/product.interface';
import { StoreService } from 'src/app/services/auth/store.service';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent  implements OnInit{

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
