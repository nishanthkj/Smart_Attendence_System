
# Facial Recognition-based Attendance Tracking System

## Overview

This Python script is designed to perform facial recognition for attendance tracking during lectures or classes. It detects faces using OpenCV's Haar Cascade classifier, matches them against pre-defined images, and records attendance in an Excel file.

## Prerequisites

- Python 3.x installed on your system.
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

Save the above content into a file with a `.md` extension (e.g., `README.md`). This Markdown file now includes the correct repository URL, providing a comprehensive guide for setting up, running, and using your facial recognition-based attendance tracking system. Adjust the content further based on your specific project details and formatting preferences before using or distributing it.
