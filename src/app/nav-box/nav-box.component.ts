import {MenuComponent} from './menu/menu.component'
import { Component, Input, Output, EventEmitter } from '@angular/core'
import {SharedService} from '../services/shared.service'

@Component({
  selector: 'nav-box',
  templateUrl: 'nav-box.component.html',
  styleUrls: ['nav-box.component.scss']
})

export class NavBoxComponenet {
  menuCategories:Array<string> = ['Procesory', 'Karty graficzne', 'Pamięci RAM', 'Dyski SSD', 'Dyski HDD'];

  constructor(private sharedService:SharedService){}

  sendSearchQuery(searchQuery:string){
    this.sharedService.change(searchQuery);
  }

}
