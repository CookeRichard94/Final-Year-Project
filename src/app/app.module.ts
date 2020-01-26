import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { MainPageComponent } from './main-page/main-page.component';
import {RouteModule} from './route/route.module';
import {RouterModule} from '@angular/router';
import { CoreModule } from './core/core.module';
import { ProductComponent } from './product/product.component';
import {MatButtonModule, MatButtonToggleModule, MatGridListModule, MatIconModule, MatListModule, MatMenuModule} from '@angular/material';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { StoreInfoService } from './store-info.service';
import { AngularFireModule } from '@angular/fire';
import { AngularFirestoreModule } from '@angular/fire/firestore';
import { AngularFireStorageModule } from '@angular/fire/storage';
import { AngularFireAuthModule } from '@angular/fire/auth';
// 2. Add your credentials from step 1
const config = {
  apiKey: "AIzaSyA7vkC_fWFz57LcVddQNNYocml3qvkDsmM",
  authDomain: "consumer-fyp-f77c6.firebaseapp.com",
  databaseURL: "https://consumer-fyp-f77c6.firebaseio.com",
  projectId: "consumer-fyp-f77c6",
  storageBucket: "consumer-fyp-f77c6.appspot.com",
  messagingSenderId: "993525606657"
};

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    MainPageComponent,
    ProductComponent
  ],
  imports: [
    BrowserModule,
    RouteModule,
    RouterModule,
    MatMenuModule,
    BrowserAnimationsModule,
    MatIconModule,
    MatGridListModule,
    CoreModule,
    MatListModule,
    MatButtonModule,
    AngularFireModule.initializeApp(config),
    AngularFirestoreModule, // firestore
    AngularFireAuthModule, // auth
    AngularFireStorageModule,
    MatButtonToggleModule,
    // storage
  ],
  providers: [StoreInfoService],
  bootstrap: [AppComponent]
})
export class AppModule { }
