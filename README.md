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
<img src="https://user-images.githubusercontent.com/79128042/141942444-abc3a6e0-f706-4249-916c-09baebe7e0cf.png" align="left" height="200px" width="460px">
<img src="https://user-images.githubusercontent.com/79128042/141942500-fafad351-4a37-4acd-b57f-7af0dbe7d143.png" align="right" height="200px" width="460px">
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

# Our Mobius System
Step 1) We provide these functons by using Vue.js
- Sign up / Sign in
- realtime monitor the shippment state using Kakaomap API

![image](https://user-images.githubusercontent.com/79128042/141946648-d103475e-78ba-40fc-95fe-2ac80556134d.png)

![image](https://user-images.githubusercontent.com/79128042/141946705-8026e4f1-4047-417e-ac7e-9b1c53ccccf8.png)

![image](https://user-images.githubusercontent.com/79128042/141947563-1cc1306f-e499-4392-b471-030bcd0760c2.png)


Step 2) We are using nCube MUV to show Drone's battery state, GPS, velocity and so on

![image](https://user-images.githubusercontent.com/79128042/141947671-0e9b45be-1de7-4737-b1b2-e59f2d7d7bbb.png)
We can set the origin and destination to set the waypoint and control the drone through mavlink. The drones moved in this way aim to land at the station.

We used nCube MUV to use drone status information and GPS information. As the information is delivered, it is transmitted to the Mobius server in real time and communicates with the web and station through the data to bring in a turtlebot in a state where driving inside the building is possible. We tried to implement the precision landing of the drone as a challenge, but this part was not successful.

Step 3) Turtlebot / Elevator Physical Button

![image](https://user-images.githubusercontent.com/79128042/141948065-a59ab865-b45a-4487-a988-d42680af1f1f.png)

What is essential for the driving of the delivery robot is the result of the slam in the building. This consists of two image files and yaml files and coincides with the starting point of the delivery robot to start driving. This presupposes that the building is located in the building through a slam in advance.

![image](https://user-images.githubusercontent.com/79128042/141948121-1fe7e19b-17b4-4be0-ac77-c99640897c78.png)

It is the navigation part of the building that runs autonomously. Using the map provided through the slam, it's LiDAR. Through the sensor, the driving is started by calculating the part that matches the map stochastically.

![image](https://user-images.githubusercontent.com/79128042/141948252-85c4ec9f-09f0-41d4-b0b4-aa8c76d97bf1.png)

The moving delivery robot arrives at the elevator in the building and sends a signal to the Mobius server to use the elevator. Delivery in high-rise buildings can also be carried out without difficulty.

![image](https://user-images.githubusercontent.com/79128042/141948314-66fb1b30-4d92-4690-bf4b-fb12b08f2a1d.png)

Physical buttons that depend on the inside and outside determine whether to operate the servo motor according to the lighting state of the button. This result is sometimes given or received commands from the Mobius server.

Both the SLAM and NAVIGATION functions of ROS are far from the words unmanned and autonomous in that nodes must be executed one by one at the terminal. Therefore, we made this part autonomous by processing it with shell(.sh).

Step 4) Face Recognition

![image](https://user-images.githubusercontent.com/79128042/141948373-ff7b343a-1dbe-4528-9ad7-f2e5b451409b.png)

The corresponding driving robot reaches the target layer and performs autonomous driving to the destination based on the map in the target layer. The turtlebot arrives at the user and recognizes the face through the camera module.

![image](https://user-images.githubusercontent.com/79128042/141948443-9448f4de-b68e-45f4-973b-bdac267b0e7c.png)

Photos of recipients received from users on the web are stored in the Mobius server. The server learns a face with the stored photo dataset. The learning model is also stored in the server. When the turtlebot autonomously drives and arrives at the recipient's place, it recognizes people's faces through OpenCV and delivers packages if the recipient is correct.

# Our Full scenario demo Video

https://youtu.be/D0m_2dkOxs8

# More Detail

- hackster.io
https://www.hackster.io/cssrj/onem2m-autonomous-cooperative-smart-delivery-system-7040d6

- AISL LaB
http://aisl.sejong.ac.kr/


# Award
1st Prize (과학기술정보통신부 장관상) 
