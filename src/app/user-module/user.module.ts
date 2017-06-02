import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {RouterModule} from '@angular/router';
import {RegisterComponent} from './register/register.component';
import {LoginComponent} from './login/login.component';
import {NgForm, FormsModule, FormBuilder, FormGroup, Validators} from '@angular/forms';

@NgModule({
  imports: [
    RouterModule.forChild([
      {path: 'register', component: RegisterComponent},
      {path: 'login', component: LoginComponent}
    ]),
    BrowserModule,
    FormsModule
  ],
  declarations: [
    RegisterComponent,
    LoginComponent
  ],
  providers: []
})
export class UserModule { }
