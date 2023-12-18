# Autonomous-Driving-System-with-Traffic-Light-Detection
Objective: Develop an autonomous driving system capable of detecting traffic lights using machine vision and controlling vehicle movement based on the detected signals.

Components:

Machine Vision Module:

Choose between training a model or using a pre-trained one for traffic light detection.
Implement algorithms to identify and classify traffic light signals.

Communication Module:

Establish a Python serial connection or utilize Bluetooth for seamless data transfer.
Transmit detected traffic light information to the Arduino for further processing.

Arduino Processing Unit:

Integrate motor control capabilities into the Arduino.
Implement algorithms to process received traffic light data.

Motor Control:

Adjust the Pulse Width Modulation (PWM) signal based on the processed results.
Control the vehicle's movement in response to the detected traffic light signals.

Workflow:

The machine vision module captures and processes real-time images to identify traffic lights and their signals.

The detected information is transmitted to the Arduino through a Python serial connection or Bluetooth.

The Arduino, equipped with motor control capabilities, receives and processes the traffic light data using predefined algorithms.

Based on the processed results, the Arduino adjusts the motor's PWM signal to control the vehicle's movement.

The entire system works in a closed loop, continuously capturing, processing, and responding to traffic light signals, ensuring autonomous driving with compliance to traffic rules.


Expected Outcomes:

An autonomous driving system capable of reliably detecting and responding to traffic lights.
Smooth and efficient vehicle movement control based on real-time traffic light signals.
Flexibility to choose between training a custom model or utilizing a pre trained one for traffic light detection.

Future Enhancements:

Integration of additional sensors for enhanced environment perception.
Implementation of advanced algorithms for complex traffic scenarios.
Incorporation of machine learning techniques for continuous improvement in traffic light detection accuracy.

