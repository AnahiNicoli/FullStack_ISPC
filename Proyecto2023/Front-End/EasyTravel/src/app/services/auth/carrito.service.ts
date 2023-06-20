import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Product } from 'src/app/pages/products/product.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CarritoService {

  baseUrl = 'https://fakestoreapi.com/'
  constructor(private httpClient: HttpClient) {}

  getAllProducts(): Observable<Product[]> {
    const response = this.httpClient.get<Product[]>('${this.baseUrl}products')
    console.log(response);
    return response
  }

  //esta funcion la llamo desde el componente que va a optener todos mis productos

  //getPromise(): Promise<any[]> {
  //  return lastValueForm (this.httpClient.get<any[]>('$ {this.https://api.escuelajs.co/api/v1/products?limit=3&offset=3} products'))
  //}

}
