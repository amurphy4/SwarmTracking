import cv2, sys

class Camera:
	
    def __init__(self):
        # Open camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened:
            # Unable to open camera
	    print("Unable to find camera")
	    sys.exit(0)

	# Set camera resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3072) # Change to 4096 for 4k resolution
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1680) # Change to 2160 for 4k resolution
        self.cap.set(cv2.CAP_PROP_FPS, 30)

    def get_frame(self):
        # Read from camera
        ret, frame = self.cap.read()

        # Return only the frame
        return frame
