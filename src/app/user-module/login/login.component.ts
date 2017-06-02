import { Component, OnInit } from '@angular/core';
import {User} from '../../models/user.model';
import {ApiService} from '../../services/api.service';
import { Router } from '@angular/router';
import {NgForm, FormsModule, FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'login',
  templateUrl: 'login.component.html',
  styleUrls: ['login.component.scss']
})
export class LoginComponent implements OnInit {
  email:string;
  password:string;


  constructor() {  }

  ngOnInit() {}

  onSubmit(form:NgForm){
    
  }
}
