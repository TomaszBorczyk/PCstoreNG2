import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';

//bootstrap
import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { NavBoxComponenet } from './nav-box/nav-box.component';
import { MenuComponent } from './nav-box/menu/menu.component';
import { SearchBoxComponent } from './nav-box/search-box/search-box.component';
import { ContainerMainComponent } from './container-main/container-main.component';
import { ProductsComponent } from './products/products.component';
import { SingleProductComponent } from './single-product/single-product.component';

import { ProductDetailComponent } from './product-detail/product-detail.component';

import { SharedService } from './services/shared.service';
import { ApiService } from './services/api.service';

@NgModule({
  declarations: [
    AppComponent,
    NavBoxComponenet,
    MenuComponent,
    SearchBoxComponent,
    ContainerMainComponent,
    ProductsComponent,
    SingleProductComponent,
    ProductDetailComponent
  ],
  imports: [
    AlertModule.forRoot(),
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot([
        {path: 'products/:category', component: ProductsComponent},
        {path: 'product/:id', component: ProductDetailComponent},
        {path: 'products', component: ProductsComponent},
        {path: '', redirectTo: 'products', pathMatch: 'full'},
        {path: '**', redirectTo: 'products', pathMatch: 'full'}
    ])
  ],
  providers: [SharedService,
              ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
