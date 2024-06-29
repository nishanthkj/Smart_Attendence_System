import cv2

# Set the camera port (usually 0 for the default camera, adjust if necessary)
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# Prompt user for person name
inp = input('Enter person name: ')

# Check if the camera opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
else:
    # Capture an image from the camera
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('Press Space to take a picture', frame)

        # Wait for user to press the space bar
        key = cv2.waitKey(1)
        if key % 256 == 32:  # Space bar key code is 32
            # Save the captured image
            img_name = f"{inp}.png"
            cv2.imwrite(img_name, frame)
            print(f"Image {img_name} taken")
            break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
