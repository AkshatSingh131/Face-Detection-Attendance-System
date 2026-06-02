import cv2
import pickle
from database import mark_attendance
import face_recognition
# Initialize video capture from the default camera (index 0)
cap = cv2.VideoCapture(0)
with open("encodings.pkl","rb") as f:
    known_encodings=pickle.load(f)


while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
        
    # Display the resulting frame
    
    
    # Break the loop if 'q' is pressed or Esc is hit (key 27)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    face=face_recognition.face_locations(frame)
    encodings=face_recognition.face_encodings(frame, face)
    known_encoding_list = list(known_encodings.values())
    known_names_list = list(known_encodings.keys())
   
    for encoding, face_location in zip(encodings, face):
        top, right, bottom, left = face_location
        matches=face_recognition.compare_faces(known_encoding_list,  encoding)
        if True in matches:
            index=matches.index(True)
            name=known_names_list[index]
            mark_attendance(name)
            cv2.rectangle(frame,(left,top),(right,bottom), (0, 255, 0), 2)
            cv2.putText(  frame, name,(left,top-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2 )
    cv2.imshow('Attendance System', frame)      
            
# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()   