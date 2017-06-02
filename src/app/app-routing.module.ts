import { NgModule } from '@angular/core';
import {RouterModule} from '@angular/router';

@NgModule({
  imports:[
    RouterModule.forRoot([
        {path: '', redirectTo: 'products', pathMatch: 'full'},
        {path: '**', redirectTo: 'products', pathMatch: 'full'}
    ])
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
