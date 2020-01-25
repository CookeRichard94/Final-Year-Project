import { Injectable } from  '@angular/core';
import {Router} from '@angular/router';

import * as firebase from 'firebase/app';
import {AngularFireAuth} from 'angularfire2/auth';
import {AngularFireStore, AngularFirestoreDocument} from 'angularfire2/firestore';

import { Observable} from 'rxjs';
import 'rxjs/add/operator/switchMap';

interface User {
  uid: string;
  email: string;
  userDisplayName: string;
}

@Injectable()
export class AuthService {

  user: Observable<User>
  constructor(private afAuth: AngularFireAuth,
              private afs: AngularFireStore,
              private router: Router) {
    this.user = this.afAuth.authState.switchMap(user => {
      if (user) {
        return this.afs.doc<User>(`users/${user.uid}`).valueChanges()
      } else {
        return new Observable(null);
      }
    });
  }

  googleLogin() {
    const provider = new firebase.auth.GoogleAuthProvider()
    return this.oAuthLogin(provider);
  }
  private oAuthLogin(provider){
    return this.afAuth.auth.signInWithPopup(provider)
      .then((credential) => {
        this.updateUserData(credential.user)
      })
  }
  private updateUserData(user){
    const userRef: AngularFirestoreDocument<User> = this.afs.doc(`users/${user.uid}`);

    const data: User = {
      uid: user.uid,
      email: user.email,
      userDisplayName: user.userDisplayName
    }

    return userRef.set(data)
  }
}
