<template>
  <div class="form-wrap">
    <form class="register">
      <p class="login-register">
        Already have an account?
        <router-link class="router-link" :to="{ name: 'Login' }"
          >Login</router-link
        >
      </p>
      <h2>Create Your AISL Account</h2>
      <div class="inputs">
        <div class="input">
          <input type="text" placeholder="Name" v-model="Name" />
          <user class="icon" />
        </div>
        <div class="input">
          <input type="text" placeholder="Username" v-model="username" />
          <user class="icon" />
        </div>
        <div class="input">
          <input type="text" placeholder="Email" v-model="email" />
          <email class="icon" />
        </div>
        <div class="input">
          <input type="password" placeholder="Password" v-model="password" />
          <password class="icon" />
        </div>

        <div class="inputs">
          <div class="input">
            <input type="text" placeholder="address" v-model="address" />
            <user class="icon" />
          </div>

          <div class="input">
            <input
              type="text"
              v-model="extraAddress"
              placeholder="extraAddress"
            />
            <user class="icon" />
          </div>
          <input
            type="button"
            @click="execDaumPostcode()"
            value="       address Search        "
          /><br />
          <!-- <input type="text" v-model="postcode" placeholder="우편번호" />
          <input
            type="button"
            @click="execDaumPostcode()"
            value="우편번호 찾기"
          /><br /> -->
          <!-- <input type="text" id="address" placeholder="주소" /> -->
        </div>

        <!-- <div class="container mt-10">
          <div class="card bg-white">
            <img :src="image" alt="card_image" />
            <input
              @change="handleImage"
              class="custom-input"
              type="file"
              accept="image/*"
            />
          </div>
        </div> -->

        <button @click.prevent="openTextFile()">Image File Open</button>
        <div>
          <img id="targetImg" />
        </div>

        <div v-show="error" class="error">{{ this.errorMsg }}</div>
      </div>
      <button @click.prevent="register">Sign Up</button>
      <div class="angle"></div>
    </form>
    <div class="background"></div>
  </div>
</template>

<script>
var res_img = "";
import email from "../assets/Icons/envelope-regular.svg";
import password from "../assets/Icons/lock-alt-solid.svg";
import user from "../assets/Icons/user-alt-light.svg";
import firebase from "firebase/app";
import "firebase/auth";
import db from "../firebase/firebaseInit";
//import axios from "axios";
import wait from "waait";

//import post from "../post_email";

export default {
  name: "Register",
  components: {
    email,
    password,
    user,
  },

  data() {
    return {
      Name: "",
      username: "",
      email: "",
      password: "",
      shipping: "",
      image: "",
      remoteUrl: "",
      error: null,
      errorMsg: "",
      res_img: "",
      postcode: "",
      address: "",
      extraAddress: "",
    };
  },
  methods: {
    openTextFile() {
      var input = document.createElement("input");

      input.type = "file";
      input.accept = "image/*";
      input.id = "uploadInput";

      input.click();
      input.onchange = function(event) {
        processFile(event.target.files[0]);
      };
    },

    execDaumPostcode() {
      new window.daum.Postcode({
        oncomplete: (data) => {
          if (this.extraAddress !== "") {
            this.extraAddress = "";
          }
          if (data.userSelectedType === "R") {
            // 사용자가 도로명 주소를 선택했을 경우
            this.address = data.roadAddress;
          } else {
            // 사용자가 지번 주소를 선택했을 경우(J)
            this.address = data.jibunAddress;
          }

          // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
          if (data.userSelectedType === "R") {
            // 법정동명이 있을 경우 추가한다. (법정리는 제외)
            // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if (data.bname !== "" && /[동|로|가]$/g.test(data.bname)) {
              this.extraAddress += data.bname;
            }
            // 건물명이 있고, 공동주택일 경우 추가한다.
            if (data.buildingName !== "" && data.apartment === "Y") {
              this.extraAddress +=
                this.extraAddress !== ""
                  ? `, ${data.buildingName}`
                  : data.buildingName;
            }
            // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if (this.extraAddress !== "") {
              this.extraAddress = `(${this.extraAddress})`;
            }
          } else {
            this.extraAddress = "";
          }
          // 우편번호를 입력한다.
          this.postcode = data.zonecode;
        },
      }).open();
    },

    async register() {
      if (
        this.email !== "" &&
        this.password !== "" &&
        this.Name !== "" &&
        this.username !== "" &&
        this.address !== "" &&
        this.extraAddress !== ""
      ) {
        this.error = false;
        this.errorMsg = "";
        const firebaseAuth = await firebase.auth();
        const createUser = await firebaseAuth.createUserWithEmailAndPassword(
          this.email,
          this.password
        );

        const result = await createUser;
        const dataBase = db.collection("users").doc(result.user.uid);
        await dataBase.set({
          Name: this.Name,
          username: this.username,
          email: this.email,
          address: this.address,
          extraAddress: this.extraAddress,
        });

        // var request_cnt = require("request");
        // var options_cnt = {
        //   method: "POST",
        //   url: "http://203.253.128.161:7579/Mobius/ai-star/documents",
        //   headers: {
        //     Accept: "application/json",
        //     "X-M2M-RI": "12345",
        //     "X-M2M-Origin": "{{aei}}",
        //     "Content-Type": "application/vnd.onem2m-res+json; ty=3",
        //   },
        //   body: '{\n  "m2m:cnt": {\n    "rn": "' + result.user.uid + '"\n }\n}',
        // };
        // await request_cnt(options_cnt, function(error, response) {
        //   if (error) throw new Error(error);
        //   console.log(response.body);
        // });

        var const_url = "http://203.253.128.161:7579/Mobius/cssrj/Web/";

        var requestCnt = require("request");
        var optionsCnt = {
          method: "POST",
          url: "http://203.253.128.161:7579/Mobius/cssrj/Web",
          headers: {
            Accept: "application/json",
            "X-M2M-RI": "12345",
            "X-M2M-Origin": "{{aei}}",
            "Content-Type": "application/vnd.onem2m-res+json; ty=3",
          },
          body: '{\n  "m2m:cnt": {\n    "rn": "' + result.user.uid + '"\n }\n}',
        };

        var requestCntPhoto = require("request");
        var optionsCntPhoto = {
          method: "POST",
          url: const_url + result.user.uid,
          headers: {
            Accept: "application/json",
            "X-M2M-RI": "12345",
            "X-M2M-Origin": "{{aei}}",
            "Content-Type": "application/vnd.onem2m-res+json; ty=3",
          },
          body: '{\n  "m2m:cnt": {\n    "rn": "Photo"\n }\n}',
        };

        var requestCntShipping = require("request");
        var optionsCntShipping = {
          method: "POST",
          url: const_url + result.user.uid,
          headers: {
            Accept: "application/json",
            "X-M2M-RI": "12345",
            "X-M2M-Origin": "{{aei}}",
            "Content-Type": "application/vnd.onem2m-res+json; ty=3",
          },
          body: '{\n  "m2m:cnt": {\n    "rn": "Shipping"\n }\n}',
        };
        var a = 1;
        var i = 0;
        while (a) {
          i++;

          if (res_img[i] == ",") {
            res_img = res_img.substring(i + 1);
            break;
          }
        }
        console.log(res_img);
        var requestCinPhoto = require("request");

        var optionsCinPhoto = {
          method: "POST",
          url: const_url + result.user.uid + "/Photo",
          headers: {
            Accept: "application/json",
            "X-M2M-RI": "12345",
            "X-M2M-Origin": "{{aei}}",
            "Content-Type": "application/vnd.onem2m-res+json; ty=4",
          },
          body:
            '{\r\n    "m2m:cin": {\r\n        "con": " ' +
            res_img +
            '"\r\n    }\r\n\r\n}',
        };

        var requestCinShipping = require("request");

        var optionsCinShipping = {
          method: "POST",
          url: const_url + result.user.uid + "/Shipping",
          headers: {
            Accept: "application/json",
            "X-M2M-RI": "12345",
            "X-M2M-Origin": "{{aei}}",
            "Content-Type": "application/vnd.onem2m-res+json; ty=4",
          },
          body:
            '{\r\n    "m2m:cin": {\r\n        "con": " ' +
            this.extraAddress +
            '"\r\n    }\r\n\r\n}',
        };

        requestCnt(optionsCnt, function(error, response) {
          if (error) throw new Error(error);
          console.log(response.body);
        });
        await wait(500);

        requestCntPhoto(optionsCntPhoto, function(error, response) {
          if (error) throw new Error(error);
          console.log(response.body);
        });

        await wait(500);

        requestCntShipping(optionsCntShipping, function(error, response) {
          if (error) throw new Error(error);
          console.log(response.body);
        });

        await wait(500);

        requestCinPhoto(optionsCinPhoto, function(error, response) {
          if (error) throw new Error(error);
          console.log(response.body);
        });

        await wait(500);
        requestCinShipping(optionsCinShipping, function(error, response) {
          if (error) throw new Error(error);
          console.log(response.body);
        });

        try {
          // await requestCin(optionsCin, function(error, response) {
          //   if (error) throw new Error(error);
          //   console.log(response.body);
          // });
        } catch (e) {
          if (e) {
            await requestCnt(optionsCnt, function(error, response) {
              if (error) throw new Error(error);
              console.log(response.body);
            });

            // await requestCin(optionsCin, function(error, response) {
            //   if (error) throw new Error(error);
            //   console.log(response.body);
            // });
          }
        }

        this.$router.push({ name: "Home" });
        return;
      }
      this.error = true;
      this.errorMsg = "Please fill out all the field";
    },
  },
};
function processFile(file) {
  var reader = new FileReader();
  reader.onload = function() {
    res_img = reader.result;
    //output.innerText = result;
    //console.log(result);
    document.getElementById("targetImg").setAttribute("src", res_img);
  };
  reader.readAsDataURL(file);
}
</script>

<style lang="scss" scoped>
.register {
  h2 {
    max-width: 350px;
  }
}

.imginput {
  position: absolute;
  top: 0;
  left: 0;
  width: 108px;
  height: 30px;
  opacity: 0;
}

.form-wrap {
  overflow: hidden;
  display: flex;
  height: 100vh;
  justify-content: center;
  align-self: center;
  margin: 0 auto;
  width: 90%;
  @media (min-width: 900px) {
    width: 100%;
  }

  .login-register {
    margin-bottom: 32px;

    .router-link {
      color: #000;
    }
  }

  form {
    padding: 0 10px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1;
    @media (min-width: 900px) {
      padding: 0 50px;
    }

    h2 {
      text-align: center;
      font-size: 32px;
      color: #303030;
      margin-bottom: 40px;
      @media (min-width: 900px) {
        font-size: 40px;
      }
    }

    .inputs {
      width: 100%;
      max-width: 350px;

      .input {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 8px;
        input {
          width: 100%;
          border: none;
          background-color: #f2f7f6;
          padding: 4px 4px 4px 30px;
          height: 50px;

          &:focus {
            outline: none;
          }
        }

        .icon {
          width: 12px;
          position: absolute;
          left: 6px;
        }
      }
    }

    .forgot-password {
      text-decoration: none;
      color: #000;
      cursor: pointer;
      font-size: 14px;
      margin: 16px 0 32px;
      border-bottom: 1px solid transparent;
      transition: 0.5s ease all;

      &:hover {
        border-color: #303030;
      }
    }

    .angle {
      display: none;
      position: absolute;
      background-color: #fff;
      transform: rotateZ(3deg);
      width: 60px;
      right: -30px;
      height: 101%;
      @media (min-width: 900px) {
        display: initial;
      }
    }
  }

  .background {
    display: none;
    flex: 2;
    background-size: cover;
    background-image: url("../assets/background.png");
    width: 100%;
    height: 100%;
    @media (min-width: 900px) {
      display: initial;
    }
  }
}
</style>