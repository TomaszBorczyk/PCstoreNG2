import {Component, Injectable,Input,Output,EventEmitter} from '@angular/core'

@Injectable()
export class SharedService {
  @Output() searchString: EventEmitter<string> = new EventEmitter();

   change(search:string) {
    console.log('change started');
     this.searchString.emit(search);
   }

   getEmittedValue() {
     return this.searchString;
   }

}
