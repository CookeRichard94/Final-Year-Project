import { Injectable } from '@angular/core';
import {Tile} from './models/tile';

@Injectable({
  providedIn: 'root'
})
export class StoreInfoService {
  tiles: Tile[] = [
    {
      text: 'Home',
      cols: 1,
      rows: 2,
      class: 'one-tile',
      id: 0
    },
    {
      text: 'Health',
      cols: 1,
      rows: 1,
      class: 'two-tile',
      id: 1
    },
    {
      text: 'Electronics',
      cols: 2,
      rows: 2,
      class: 'three-tile',
      id: 2
    },
    {
      text: 'Outdoors',
      cols: 1,
      rows: 1,
      class: 'five-tile',
      id: 3
    },
    {
      text: 'Clothes',
      cols: 2,
      rows: 1,
      class: 'five-tile',
      id: 4
    },
    {
      text: 'Sports',
      cols: 1,
      rows: 2,
      class: 'six-tiles',
      id: 5
    }
  ];

  constructor() { }
}
