import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, lastValueFrom } from 'rxjs';
import { Product } from 'src/app/pages/products/product.interface';

@Injectable({
  providedIn: 'root'
})
export class StoreService {

  baseUrl = 'https://fakestoreapi.com/'

  //lista carrito que voy a llamar

  private myList:Product[]=[];

//carrito observable

private myCart = new BehaviorSubject<Product[]>([]);
myCart$ = this.myCart.asObservable();

  constructor(private httpClient: HttpClient) { }

  //me traigo los productos con esta función y acá hago la llamada.
  //llamame al httpclient con este método.

getAllProducts(): Observable<Product[]> {

  const response = this.httpClient.get<Product[]>(`${this.baseUrl}products`);
  

  //console.log(response); -lo desactivo x ahora-
  return response
}

//getPromise(): Promise<any[]>{
//  return lastValueFrom(this.httpClient.get<any[]>('${this.baseUrl}products'))
//}


//para agregar productos al carrito y chequear si es nuevo o ya hay

addProduct(product: Product) {

  if(this.myList.length === 0 ){

    product.cantidad = 1;
    this.myList.push(product)
    this.myCart.next(this.myList);
  }
  else{
    const productMod = this.myList.find((element)=> {
    return element.id === product.id 
  })
  if(productMod) {
    productMod.cantidad = productMod.cantidad + 1;
    this.myCart.next (this.myList); }
    else {
      product.cantidad = 1;
      this.myList.push(product);
      this.myCart.next(this.myList);
    }
  } 
}
 
findProductById(id:string){
  return this.myList.find((element) => {
    return element.id === id
  })
}

deleteProduct(id:string) {
  this.myList = this.myList.filter((product)=> {
    return product.id != id
  })
  this.myCart.next(this.myList);
}



totalCart(){
  const total = this.myList.reduce(function (acc, product) {return acc + (product.cantidad * product.price);}, 0)
  return total
}
}


