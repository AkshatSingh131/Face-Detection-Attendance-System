import os
import face_recognition
import pickle

KNOWN_FACES_DIR = r"C:\Users\KIIT\Face Attendance System\known_faces" #image directory(need to add images here)

known_encodings = {}

for image in os.listdir(KNOWN_FACES_DIR):

    if image.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(KNOWN_FACES_DIR, image)

        loaded_image = face_recognition.load_image_file(image_path)

        face_locations = face_recognition.face_locations(loaded_image)

        face_encodings = face_recognition.face_encodings(
            loaded_image,
            face_locations
        )

        name = os.path.splitext(image)[0]

        if face_encodings:

            known_encodings[name] = face_encodings[0]

            print(f"Encoding saved for {name}")

        else:
            print(f"No face found in {image}")

with open("encodings.pkl", "wb") as file:
    pickle.dump(known_encodings, file)

print("All encodings saved successfully")