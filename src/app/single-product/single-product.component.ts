import {ProductModel} from '../models/product/product.model';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'single-product',
  templateUrl: 'single-product.component.html',
  styleUrls: ['single-product.component.scss']
})

export class SingleProductComponent{
  @Input()
  product:ProductModel;

  get getName():string{
    return this.product.name;
  }

}
