import {Injectable} from '@angular/core';
import {Inject} from '@angular/core';
import {Http, Response, Headers, RequestOptions} from "@angular/http";
import {Observable} from "rxjs";
import {ProductModel} from '../models/product/product.model'
import {User} from '../models/user.model';
import 'rxjs/Rx';

@Injectable()
export class ApiService{
  apiServer:string = 'http://127.0.0.1:8000/api/';

  constructor(private http:Http){}

  fetchProducts(searchQuery:string):Promise<Array<ProductModel>>{
    return this.http.get(this.apiServer+'products/?search='+searchQuery)
                    .toPromise()
                    .then((res:Response) => res.json()
                    .map(json => {
                      let product:ProductModel = Object.assign(new ProductModel(), json);
                      return product;
                    }));
  }

  getBestsellers():Promise<Array<ProductModel>>{
    return this.http.get(this.apiServer+'orders/bestsellers/')
                    .toPromise()
                    .then((res:Response) => res.json()
                    .map(json => {
                      let product:ProductModel = Object.assign(new ProductModel(), json);
                      return product;
                    }));
                  }

    createUser(user:User){
      let body = JSON.stringify(user);
      let headers = new Headers({ 'Content-Type': 'application/json' });
      let options = new RequestOptions({ headers: headers });
      this.http.post(this.apiServer+'users/create/', body, options)
                            .subscribe(
                              data => {alert('ok');},
                              error => {console.log(JSON.stringify(error.json()));}
                            );
    }

    // loginUser()


    private extractData(res: Response) {
        let body = res.json();
        return body.data || {};
    }

    private handleError(error: Response) {
        console.error(error);
        return Observable.throw(error.json().error || 'Server Error');
    }


}
