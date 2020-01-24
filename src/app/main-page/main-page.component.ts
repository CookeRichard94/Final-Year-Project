import { Component, OnInit } from '@angular/core';
import {StoreInfoService} from '../store-info.service';
import {Tile} from '../models/tile';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {

  tiles: Tile[];
  constructor(private storeInfo: StoreInfoService) { }

  ngOnInit() {
    console.log(this.storeInfo);
    this.tiles = this.storeInfo.tiles;
  }
}
