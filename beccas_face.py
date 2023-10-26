import face_recognition
import cv2
import os

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

# Load images from the "levi" folder and encode them
levi_folder = "becca"
for image_filename in os.listdir(levi_folder):
    image_path = os.path.join(levi_folder, image_filename)
    levi_image = face_recognition.load_image_file(image_path)
    levi_face_encoding = face_recognition.face_encodings(levi_image)[0]
    known_face_encodings.append(levi_face_encoding)
    known_face_names.append("Levi C. C")

# Initialize camera
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Initialize list to store names of detected faces
    face_names = []

    for face_encoding in face_encodings:
        # Compare face encoding with known face encodings using a tolerance threshold
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            matched_indices = [i for i, match in enumerate(matches) if match]
            first_match_index = matched_indices[0]
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Display face recognition results on the frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw rectangle around the face
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)  # Red for "Unknown"
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        
        # Draw label below the face
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
video_capture.release()
cv2.destroyAllWindows()
