import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainPageComponent} from '../main-page/main-page.component';
import { ProductComponent } from '../product/product.component';


const routes: Routes = [{
  path: '',
  component: MainPageComponent
},
  {
    path: 'product/:id',
    component: ProductComponent
}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class RouteRoutingModule { }
