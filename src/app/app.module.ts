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

import { SharedService } from './services/shared.service';
import { ApiService } from './services/api.service';
import {AppRoutingModule} from './app-routing.module';
import {ProductModule} from './products-module/product.module';

import {UserModule} from './user-module/user.module';

@NgModule({
  declarations: [
    AppComponent,
    NavBoxComponenet,
    MenuComponent,
    SearchBoxComponent,
    ContainerMainComponent
  ],
  imports: [
    AlertModule.forRoot(),
    ProductModule,
    UserModule,
    AppRoutingModule,
    
    BrowserModule,
    FormsModule,
    HttpModule,
  ],
  providers: [SharedService,
              ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
