import cv2
import numpy as np
from datetime import date
import xlwt
from xlwt import Workbook
import xlrd
from xlutils.copy import copy as xl_copy

# Function to detect faces in a frame using Haar Cascade
def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces

# Function to extract face descriptors (dummy function here, replace with actual method if available)
def encode_face(face):
    # Dummy function, replace with actual face encoding method
    return np.random.rand(128)  # Example random 128-dimensional vector

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Initialize Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize workbook
rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True)
wb = xl_copy(rb)
inp = input('Please give current subject lecture name')
sheet1 = wb.add_sheet(inp)
sheet1.write(0, 0, 'Name/Date')
sheet1.write(0, 1, str(date.today()))
row = 1
col = 0
already_attendance_taken = ""

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Failed to capture video")
        break

    # Detect faces using Haar Cascade
    faces = detect_faces(frame, face_cascade)

    face_names = []
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]

        # Dummy encoding for demonstration
        face_encoding = encode_face(face_roi)

        # Compare with known face encodings (replace with actual comparison logic)
        # Here, we simulate matching by checking a dummy condition
        match_person1 = np.random.choice([True, False])  # Dummy match condition
        match_person2 = np.random.choice([True, False])  # Dummy match condition

        if match_person1:
            name = "Rahul"
        elif match_person2:
            name = "Sneha"
        else:
            name = "Unknown"

        if name not in face_names:
            face_names.append(name)

            if name not in already_attendance_taken and name != "Unknown":
                sheet1.write(row, col, name)
                col += 1
                sheet1.write(row, col, "Present")
                row += 1
                col = 0
                print(f"{name} attendance taken")
                wb.save('attendence_excel.xls')
                already_attendance_taken = name

        # Draw bounding box around detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Data saved")
        break

video_capture.release()
cv2.destroyAllWindows()
