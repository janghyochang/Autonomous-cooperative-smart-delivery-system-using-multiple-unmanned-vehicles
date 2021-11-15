import Vue from 'vue';
import Vuex from 'vuex';
import firebase from "firebase/app";
import "firebase/auth";
import db from "../firebase/firebaseInit";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    sampleBlogCards: [
      {
        blogTitle: "Blog Card #1",
        blogCoverPhoto: "stock-1",
        blogDate: "May 1, 2021",
      },
      {
        blogTitle: "Blog Card #2",
        blogCoverPhoto: "stock-2",
        blogDate: "May 1, 2021",
      },
      {
        blogTitle: "Blog Card #3",
        blogCoverPhoto: "stock-3",
        blogDate: "May 1, 2021",
      },
      {
        blogTitle: "Blog Card #4",
        blogCoverPhoto: "stock-4",
        blogDate: "May 1, 2021",
      },
    ],
    photoFileURL: null,
    photoPreview: null,
    editPost: null,
    user: null,
    profileEmail: null,
    profileName: null,
    profileUsername: null,
    profileId: null,
    profileShipping: null,
    profileInitials: null,
  },
  mutations: {
    toggleEditPost(state, payload){
      state.editPost = payload;
    },
    updataUser(state, payload){
      state.user = payload;
    },
    setProfileInfo(state, doc){
      state.profileId = doc.id;
      state.profileEmail = doc.data().email;
      state.profileName = doc.data().Name;
      state.profileUsername = doc.data().username;
      state.profileShipping = doc.data().shipping;
      
    },
    setProfileInitials(state) {
      state.profileInitials = 
      state.profileFirstName.match(/(\b\S)?/g).join("") +
      state.profileLastName.match(/(\b\S)?/g).join("");

    },
    changeName(state, payload){
      state.profileName = payload;
    },
    changeUsername(state, payload){
      state.profileUsername = payload;
    },
    changeShipping(state, payload){
      state.profileShipping = payload;
    },
    
  },
  actions: {
    async getCurrentUser({commit}) {
      const dataBase = await db.collection("users").doc(firebase.auth().currentUser.uid);
      const dbResults = await dataBase.get();
      commit("setProfileInfo", dbResults);
      commit("setProfileInitials");
      console.log(dbResults);
    },
    async updateUserSetting({commit, state}) {
      const dataBase = await db.collection('users').doc(state.profileId);
      await dataBase.update({
        Name: state.profileName,
        username: state.profileUsername,
        shipping: state.profileShipping,
      });
      commit("setProfileInitials");
    },
    async updateUserSettings({commit, state}) {
      const dataBase = await db.collection('users').doc(state.profileId);
      await dataBase.update({
        Name: state.profileName,
        username: state.profileUsername,
        shipping: state.profileShipping,
      });
      commit("setProfileInitials");
    }
  },
  modules: {
  }
});
