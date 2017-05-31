import { Component, Input, Output, EventEmitter } from '@angular/core'
import {SharedService} from '../../services/shared.service'


@Component({
  selector: 'search-box',
  templateUrl: 'search-box.component.html',
  styleUrls: ['search-box.component.scss']
})

export class SearchBoxComponent{

  constructor(private sharedService:SharedService){}

sendSearchQuery(searchQuery:string){
  this.sharedService.change(searchQuery);
}

}
