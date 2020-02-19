import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';

@Injectable({
  providedIn: 'root'
})
export class FirebaseService {

  constructor(public db: AngularFirestore) {}

  addProduct(value: any) {
    return this.db.collection('products').add({
      name: value.name
    });
  }

  getUser(userKey){
    return this.db.collection('products').doc(userKey).snapshotChanges();
  }

  getProducts(){
    return this.db.collection('products').snapshotChanges();
  }

  searchProducts(searchValue){
    return this.db.collection('products',ref => ref.where('nameToSearch', '>=', searchValue)
      .where('nameToSearch', '<=', searchValue + '\uf8ff'))
      .snapshotChanges()
  }

  updateProduct(userKey, value) {
    value.nameToSearch = value.name.toLowerCase();
    return this.db.collection('products').doc(userKey).set(value);
  }

  deleteProduct(userKey){
    return this.db.collection('products').doc(userKey).delete();
  }
}
