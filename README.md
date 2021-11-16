# Project Outline
![image](https://user-images.githubusercontent.com/79128042/141941607-d4eaae8f-a0de-435f-97a4-c6f351dc148a.png)

These days, most people want to receive a package by non-face-to-face delivery because of the COVID-19. In addition, the conflict between the courier and the recipient is getting worse day by day. Exhaust gases generated during delivery can cause environmental pollution. As the problem of delivery intensifies, the demand for unmanned delivery systems is increasing.

Therefore, we decided to implement an unmanned delivery system by using drones and turtlebots that can help our society.
![image](https://user-images.githubusercontent.com/79128042/141941892-f20d8ae9-4dec-48fe-b422-418e62e884cf.png)

While implementing delivery as an unmanned system, users can obtain real-time information on the transportation situation of drones and turtlebots through Mobius servers.

In addition to turtlebots and drones, we have implemented IoT devices using raspberry pi in elevators and drone stations so that they can actually run services.

# Prerequisites (Framework / module )
- Mobius Server (Rental or installation)
- nCube Thyme, nCube MUV
- ROS 1 (SLAM, NAVIGATION)
- OpenCV(Color detection)
- Haar(Face recognition)

# Prerequisites (Hardware / self-made)

- Drone x 1

- Turtlebot3 waffle x 1

- Drone Station

<p>
<img src="https://user-images.githubusercontent.com/79128042/141942444-abc3a6e0-f706-4249-916c-09baebe7e0cf.png" align="left" height="200px" width="450px">
<img src="https://user-images.githubusercontent.com/79128042/141942500-fafad351-4a37-4acd-b57f-7af0dbe7d143.png" align="left" height="200px" width="450px">
</p>


We have created a station that facilitates the exchange of goods between drones and turtlebots. The DC motor in the station operates through communication with the Mobius server and opens and closes the door when the drone arrives.

The important point at this time is that you have to make a slope at the entrance of the station so that the delivery robot can go inside and pick up the goods using the robot arm.

- Drone Carrier 
A space not to touch the floor at the bottom of the drone was set as a space to store goods. The electromagnet was installed because the electromagnet module was installed to arrive at the target position and the voltage was not applied to the electromagnet when the power was turned off.

- Physical button (EV)
![image](https://user-images.githubusercontent.com/79128042/141942708-1ca24e37-e31a-450f-964b-1a186a29248f.png)

The ideal system is to operate the elevator directly, but given the realistic conditions, we could complete our project if we could install only one physical button. Therefore, a physical button with a camera module and a servo motor was created. The camera module operates the servo motor according to the lighting status of a specific floor within the elevator and sends commands to the Mobius server to help the turtle bot drive autonomously.

# System Architecture

![image](https://user-images.githubusercontent.com/79128042/141943276-b8b6469a-422b-4ae8-8ae6-5669dc19ba43.png)

Basically, our system is aimed at unmanned systems. Therefore, if the existing member information is included in the face information of the person who wants to receive additional delivery, the information will be sent to the Mobius server through base64 encoding.

The information is delivered to drones, drone stations, elevators, and delivery robots during delivery. Each piece of information is used through the mqtt communication method and we made a demo video using one school building.

![image](https://user-images.githubusercontent.com/79128042/141943667-61bd00dc-1617-4a93-92f4-f149d4601d11.png)


# nCube-MUV
Start Guide

### Install dependencies
```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -

$ sudo apt-get install -y nodejs

$ node -v

$ sudo npm install -g pm2

$ git clone https://github.com/IoTKETI/nCube-MUV

$ cd /home/pi/nCube-MUV

$ npm install
```

### Install MQTT-broker
```
$ wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
$ sudo apt-key add mosquitto-repo.gpg.key
$ cd /etc/apt/sources.list.d/
$ sudo wget http://repo.mosquitto.org/debian/mosquitto-buster.list 
$ sudo apt-get update
$ sudo apt-get install -y mosquitto
```
