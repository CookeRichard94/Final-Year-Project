import { Component, OnInit } from '@angular/core';
import {StoreInfoService} from '../store-info.service';
import {Tile} from '../models/tile';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {MatDialog,MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';
import {FirebaseService} from '../services/firebase.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {
  exampleForm: FormGroup;
  index: number;
  productInfo: any;
  names: Array<any>;

  validation_messages = {
    'name': [
      {type: 'required', message: 'Name is required.'}
    ]
  };

  constructor(
    private route: ActivatedRoute,
    private storeInfo: StoreInfoService,
    private fb: FormBuilder,
    // public MatDialog,
    private router: Router,
    public firebaseService: FirebaseService
  ) { }

  ngOnInit() {
    this.createForm();
    this.route.params.subscribe(params =>{
      this.index = params.id;
      this.productInfo = this.storeInfo.tiles.reduce((obj, item) => {
        // tslint:disable-next-line:triple-equals
        return +this.index == item.id ? item : obj;
      }, {});
    });
  }

  getData(){
    this.firebaseService.getProducts()
      .subscribe(result => {
        this.names = result;
      })
  }

  createForm() {
    this.exampleForm = this.fb.group({
      name: ['', Validators.required]
    });
  }

  resetFields(){
    this.exampleForm = this.fb.group({
      name: new FormControl('', Validators.required)
    });
  }

  onSubmit(value){
    this.firebaseService.addProduct(value)
      .then(
        res => {
          this.resetFields();
          // this.router.navigate(['/home']);
        }
      )
  }

}
