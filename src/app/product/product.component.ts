import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {StoreInfoService} from '../store-info.service';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import {MatDialog} from '@angular/material';
import {FirebaseService} from '../services/firebase.service';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  exampleForm: FormGroup;
  index: number;
  productInfo: any;

  validation_messages = {
    'name': [
      {type: 'required', message: 'Name is required.'}
    ]
  };

  constructor(
    private route: ActivatedRoute,
    private storeInfo: StoreInfoService,
    private fb: FormBuilder,
    // public dialog: MatDialog,
    private router: Router,
    public firebaseService: FirebaseService
  ) { }

  ngOnInit() {
    this.route.params.subscribe(params =>{
      this.index = params.id;
      this.productInfo = this.storeInfo.tiles.reduce((obj, item) => {
        // tslint:disable-next-line:triple-equals
        return +this.index == item.id ? item : obj;
      }, {});
    });
    //this.createForm()
  }

  // createForm() {
  //   this.exampleForm = this.fb.group({
  //     name: ['', Validators.required]
  //   });
  // }
  //
  // resetFields(){
  //   this.exampleForm = this.fb.group({
  //     name: new FormControl('', Validators.required)
  //   });
  // }
  //
  // onSubmit(value){
  //   this.firebaseService.addProduct(value)
  //     .then(
  //       res => {
  //         this.resetFields();
  //         this.router.navigate(['/home']);
  //       }
  //     )
  // }

}
