Real-Time Face Detection & Attendance System

Overview:-

A real-time face recognition system that detects and identifies individuals using a webcam feed and logs attendance automatically into a MySQL database with timestamps. It uses OpenCV for face detection and encoding-based recognition for matching identities.

Features:-
Real-time face detection via webcam
Face recognition using facial embeddings
Automatic attendance logging into MySQL
Duplicate entry prevention per session
Lightweight and runs on standard systems


Tech Stack:-
Python
OpenCV
face_recognition (dlib)
NumPy
MySQL
mysql-connector-python
(create a known_faces folder for the known images)


Architecture:-

Webcam → Face Detection → Face Encoding → Face Matching → MySQL Attendance Logging

Database Schema (MySQL):-

CREATE DATABASE face_attendance;

USE face_attendance;

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    date DATE,
    time TIME
);
