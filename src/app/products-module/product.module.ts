import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {RouterModule} from '@angular/router';
import {ProductsComponent} from './products/products.component';
import {ProductDetailComponent} from './product-detail/product-detail.component';
import {SingleProductComponent} from './single-product/single-product.component';


@NgModule({
  imports: [
    RouterModule.forChild([
      {path: 'products', component: ProductsComponent},
      {path: 'products/:id', component: ProductDetailComponent}
    ]),
    BrowserModule
  ],
  declarations: [
    ProductsComponent,
    ProductDetailComponent,
    SingleProductComponent
  ],
  providers: []
})
export class ProductModule { }
