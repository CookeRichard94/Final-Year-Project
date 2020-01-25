import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import {AuthService} from '../services/auth.service';
import {AngularFireAuthModule} from 'angularfire2/auth';
import {AngularFireStoreModule} from 'angularfire2/firestore';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    AngularFireAuthModule,
    AngularFireStoreModule
  ],
  providers: [AuthService]
})
export class CoreModule { }
