import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import {Router, ActivatedRoute, Params} from '@angular/router';
import {Location} from '@angular/common';
import {SharedService} from '../services/shared.service';
import {ApiService} from '../services/api.service';
import {Subscription} from 'rxjs';
import {ProductModel} from '../models/product/product.model';
import {CategoryModel} from '../models/category.model';


@Component({
  selector: 'products',
  templateUrl: 'products.component.html',
  styleUrls: ['products.component.scss']
})

export class ProductsComponent implements OnInit{
  name:string;
  category:string;
  subscription:Subscription;
  products:Array<ProductModel>;
  bestsellers:Array<number>;
  categories:Array<CategoryModel> = [
    new CategoryModel('cpus', 'Procesory')
  ]


  constructor(private sharedService:SharedService, private api:ApiService, private activatedRoute:ActivatedRoute, private location:Location){}

  ngOnInit(){
    this.handleSearchQuery("");
    this.subscription = this.sharedService.getEmittedValue()
                      .subscribe(item => this.handleSearchQuery(item));

    this.getBestsellers();

    this.activatedRoute.params.subscribe((params: Params) => {
        let categObj:CategoryModel = this.categories.find(obj => obj.id==params['category']);
        categObj == null ? this.location.go('/products') : this.category = categObj.name;
      });
  }

  ngOnDestroy(){
    this.subscription.unsubscribe();
  }

  private handleSearchQuery(searchQuery:string){
    this.api.fetchProducts(searchQuery)
            .then(object => this.products = object);
  }

  private getBestsellers(){
    this.api.getBestsellers()
            .then(object => this.bestsellers = object );
  }

}
