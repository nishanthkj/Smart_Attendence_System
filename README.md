
# Facial Recognition-based Attendance Tracking System

## Overview

This Python script is designed to perform facial recognition for attendance tracking during lectures or classes. It detects faces using OpenCV's Haar Cascade classifier, matches them against pre-defined images, and records attendance in an Excel file.

## Prerequisites

- Python 3.10.10 installed on your system.
- Required Python libraries:
  - `numpy`
  - `opencv-python`
  - `xlrd`
  - `xlwt`
  - `xlutils`
  
  You can install these libraries using pip:
  ```
  pip install numpy opencv-python xlrd xlwt xlutils
  ```

- Ensure you have a webcam connected to your computer for live video capture.

## Setup

1. **Clone the Repository**

   Clone this repository to your local machine:
   ```
   git clone https://github.com/nishanthkj/Smart_Attendence_System
   cd Smart_Attendence_System
   ```

2. **Install Dependencies**

   Install the required Python libraries using pip:
   ```
   pip install -r requirements.txt
   ```
   (If `requirements.txt` is unavailable, manually install the packages listed above.)

3. **Download Required Files**

   - Place the images (`rahul.png`, `sneha.png`) in the same directory as the script.
   - Ensure `haarcascade_frontalface_default.xml` (Haar Cascade file for face detection) is available in OpenCV's data directory. If not, download it from the OpenCV GitHub repository or adjust the path in the script accordingly.

4. **Excel Setup**

   - Create an Excel file `attendence_excel.xls` in the same directory as the script.
   - The script will automatically create a new sheet for each lecture/session specified.

## Running the Script

# Creating Images for Facial Recognition

## Capture Images Using `capture_image_from_camera.py`

To create the required images (`rahul.png` and `sneha.png`) for facial recognition:

1. **Run the `capture_image_from_camera.py` Script**

   Use the provided script to capture images from your webcam:

2. **Follow On-Screen Instructions**

- When prompted, position the person (e.g., Rahul or Sneha) in front of the camera.
- Ensure good lighting and clear visibility of the person's face.
- Capture multiple images to ensure different angles and lighting conditions are covered.

3. **Save Images**

- The script will save the captured images as `rahul.png` and `sneha.png` in the current directory.
- These images will be used for facial recognition in the attendance tracking system (`face_recognition_code.py`).

4. **Ensure Quality**

- Review the captured images to ensure they are clear and representative of the person's face.
- Adjust camera settings or re-capture images if needed for better accuracy in facial recognition.

## Usage in Facial Recognition System

Once the images (`rahul.png` and `sneha.png`) are created and saved in the same directory as `face_recognition_code.py`, they will be automatically used by the facial recognition script to identify and record attendance during lectures or sessions.

- Open a terminal or command prompt and navigate to the directory containing the script (`face_recognition_code.py`).

- Run the script using Python:
  ```
  python face_recognition_code.py
  ```

- Follow the on-screen instructions to input the current subject lecture name when prompted.

## Usage

- The script will capture video from your webcam and detect faces using Haar Cascade.
- For recognition, detected faces are compared against known images (`rahul.png`, `sneha.png`).
- Attendance is recorded in the Excel file (`attendence_excel.xls`) under the respective lecture/session name.

## Notes

- Ensure good lighting conditions and clear visibility of faces for accurate detection.
- Adjust face recognition parameters or use more advanced models for improved accuracy as needed.
- Exit the script by pressing `q` on the keyboard to save data and close the video window.
```
**Disclaimer**: This code has been adapted and updated with the help of AI tools to simplify its execution process.

