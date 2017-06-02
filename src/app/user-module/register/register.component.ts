import { Component, OnInit } from '@angular/core';
import {User} from '../../models/user.model';
import {ApiService} from '../../services/api.service';
import { Router } from '@angular/router';
import {NgForm, FormsModule, FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'register',
  templateUrl: 'register.component.html',
  styleUrls: ['register.component.scss']
})
export class RegisterComponent implements OnInit {
  user:User;

  constructor(private api:ApiService, private router:Router) {  }

  ngOnInit() {
    this.user = new User('', '', '', '');
  }

  onSubmit(form:NgForm){
    this.createUser();


  }

  private createUser(){
    this.api.createUser(this.user);
    this.router.navigate(['products']);
  }

}
