import { Component, Input, Output } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent {
  @Input()
  searchName:string;

  title = 'app works!';
}
