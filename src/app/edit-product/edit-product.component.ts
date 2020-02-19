import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {StoreInfoService} from '../store-info.service';
import {FirebaseService} from '../services/firebase.service';

@Component({
  selector: 'app-edit-product',
  templateUrl: './edit-product.component.html',
  styleUrls: ['./edit-product.component.css']
})
export class EditProductComponent implements OnInit {

  exampleForm: FormGroup;
  item: any;

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
    this.route.data.subscribe(routeData => {
      let data = routeData['data'];
      if (data) {
        this.item = data.payload.data();
        this.item.id = data.payload.id;
        this.createForm();
      }
    });
  }

  createForm() {
    this.exampleForm = this.fb.group({
      name: ['', Validators.required]
    });
  }

  onSubmit(value){
    value.name = value.name;
    this.firebaseService.updateProduct(this.item.name, value)
      .then(
        res => {
          this.router.navigate(['/main-page']);
        }
      )
  }

  delete(){
    this.firebaseService.deleteProduct(this.item.name)
      .then(
        res => {
          this.router.navigate(['/main-page']);
        },
        err => {
          console.log(err);
        }
      )
  }

}
