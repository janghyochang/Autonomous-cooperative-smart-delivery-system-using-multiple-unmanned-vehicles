<template>
  <div>
    <div id="map"></div>
    <div class="button-group">
      <!-- <button @click="changeSize(0)">Hide</button>
      <button @click="changeSize(350)">show</button> -->
      <!-- <button @click="displayMarker(markerPositions1)">marker set 1</button> -->
      <!-- <button @click="displayMarker(markerPositions1)">marker set 1</button> -->
      <button @click="displayMarker(markerPositions2)">배송지 실시간 조회</button>
      <!-- <button @click="displayMarker([])">marker set 3 (empty)</button> -->
      <button @click="displayInfoWindow">Last Delivery!</button>
    </div>
  </div>
</template>

<script>
import firebase from "firebase"; // eslint-disable-line no-unused-vars
// import Vue from "vue";
var con = "";
var a = 0;
var b = 0;

function coor1(con) {
  var a = 1;
  var i = 0;

  while (a) {
    i++;
    if (con[i] == ",") {
      var b = parseFloat(con.substring(0, i))/10000000;
      //console.log(b)
      return b;
    }
  }
}

function coor2(con) {
  var a = 1;
  var i = 0;

  while (a) {
    i++;
    if (con[i] == ",") {
      var c = parseFloat(con.substring(i + 1))/10000000;
      //console.log(c)
      return c;
    }
  }
}

export default {
  name: "KakaoMap",
  data() {
    //coor1(con);
    return {
      map: null,
      markerPositions1: [
        [37, 127],
        [37.54994417079293, 127.07452098962015],
        [37.55121805732519, 127.07476394035741],
      ],
      markerPositions2: [[37.551047331527634, 127.07577991616792]],
      markers: [],
      infowindow: null,
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.initMap();
    } else {
      const script = document.createElement("script");
      /* global kakao */
      script.onload = () => kakao.maps.load(this.initMap);
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=b922811d40237bf5dd985fb758e74363&libraries=services,clusterer,drawing";
      document.head.appendChild(script);
    }
  },
  updated(){
    this.displayMarker();
  },
  methods: {
    initMap() {

      var requestCnt = require("request");
      var optionsCnt = {
        method: "GET",
        url:
          "http://203.253.128.161:7579/Mobius/cssrj/Drone_Data/cssr/disarm/la",
        headers: {
          Accept: "application/json",
          "X-M2M-RI": "12345",
          "X-M2M-Origin": "SOrigin",
        },
      };

      requestCnt(optionsCnt, function(error, response) {
        if (error) throw new Error(error);
        con = JSON.parse(response.body)["m2m:cin"]["con"];
       // console.log(con);
        
        // Vue.set(this.markerPositions1, 2, this.widow);
       // console.log(widow);
       // console.log(police_thief);

      });

      
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(37.551047331527634, 127.07577991616792),
        level: 3,
      };
      this.map = new kakao.maps.Map(container, options);

      

    },
    changeSize(size) {
      const container = document.getElementById("map");
      container.style.width = `${size}px`;
      container.style.height = `${size}px`;
      this.map.relayout();
    },

    displayMarker(markerPositions) {

      var requestCnt = require("request");
      var optionsCnt = {
        method: "GET",
        url:
          "http://203.253.128.161:7579/Mobius/cssrj/Drone_Data/cssr/disarm/la",
        headers: {
          Accept: "application/json",
          "X-M2M-RI": "12345",
          "X-M2M-Origin": "SOrigin",
        },
      };

      requestCnt(optionsCnt, function(error, response) {
        if (error) throw new Error(error);
        con = JSON.parse(response.body)["m2m:cin"]["con"];
       // console.log(con);
         var widow = coor1(con);
         var police_thief = coor2(con);
        // Vue.set(this.markerPositions1, 2, this.widow);
         console.log(widow);
        console.log(police_thief);

      });
      a = coor1(con);
      b = coor2(con);
      this.markerPositions2[0][0] = a;
      this.markerPositions2[0][1] = b;
      //console.log(this.markerPositions2);
      var imageSrc = 'https://ifh.cc/g/eoQ9au.png', // 마커이미지의 주소입니다    
        imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
        imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
      
        // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
      var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
      if (this.markers.length > 0) {
        this.markers.forEach((marker) => marker.setMap(null));
      }

      const positions = markerPositions.map(
        (position) => new kakao.maps.LatLng(...position)
      );

      if (positions.length > 0) {
        this.markers = positions.map(
          (position) =>
            new kakao.maps.Marker({
              map: this.map,
              position,
              image: markerImage
            })
        );

        const bounds = positions.reduce(
          (bounds, latlng) => bounds.extend(latlng),
          new kakao.maps.LatLngBounds()
        );

        this.map.setBounds(bounds);
      }
    },
    displayInfoWindow() {
      if (this.infowindow && this.infowindow.getMap()) {
        //이미 생성한 인포윈도우가 있기 때문에 지도 중심좌표를 인포윈도우 좌표로 이동시킨다.
        this.map.setCenter(this.infowindow.getPosition());
        return;
      }
      


        // 인포윈도우로 장소에 대한 설명을 표시합니다
        var iwContent =
          '<div style="padding:5px; text-align: center;">배송지</div>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
        iwPosition = new kakao.maps.LatLng(
          37.551047331527634,
          127.07577991616792
        ), //인포윈도우 표시 위치입니다
        iwRemoveable = true; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다
      
      var imageSrc = 'https://ifh.cc/g/dYysrc.png', // 마커이미지의 주소입니다    
        imageSize = new kakao.maps.Size(64, 69), // 마커이미지의 크기입니다
        imageOption = {offset: new kakao.maps.Point(27, 69)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
      
        // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
      var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption);
      var marker = new kakao.maps.Marker({
            map: this.map,
            position: iwPosition,
            image: markerImage
        });
      this.infowindow = new kakao.maps.InfoWindow({
        map: this.map, // 인포윈도우가 표시될 지도
        position: iwPosition,
        content: iwContent,
        removable: iwRemoveable,
      });
      this.infowindow.open(this.map,marker)
      this.map.setCenter(iwPosition);
      
      

      // const spawn = require("child_process").spawn;
      // const result = spawn("python", ["./getcode.py"]);
      // result.stdout.on("data", function(data) {
      //   console.log(data.toString());
      // });
      // result.stderr.on("data", function(data) {
      //   console.log(data.toString());
      // });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
  width: 700px;
  height: 700px;
}

.button-group {
  margin: 10px 0px;
}

button {
  margin: 0 3px;
}
</style>
