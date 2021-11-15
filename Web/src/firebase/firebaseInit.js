import firebase from "firebase/app";
import "firebase/firestore";

var firebaseConfig = {
  apiKey: "AIzaSyCpEtp80ZlQ-s9RBP-uum6shv0ianQSYkk",
  authDomain: "donghun-4f39a.firebaseapp.com",
  projectId: "donghun-4f39a",
  storageBucket: "donghun-4f39a.appspot.com",
  messagingSenderId: "45543490324",
  appId: "1:45543490324:web:c291398d45b0cd07213801"
};

const firebaseApp = firebase.initializeApp(firebaseConfig);
const timestamp = firebase.firestore.FieldValue.serverTimestamp;

export {timestamp};
export default firebaseApp.firestore();


