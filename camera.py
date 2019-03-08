import cv2, sys
from pkg_resources import parse_version

class Camera:
	
    def __init__(self):
        # Open camera
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened:
			# Unable to open camera
			print("Unable to find camera")
			sys.exit(0)

		if parse_version(cv2.__version__) >= parse_version(3):
			# Set camera resolution - Using OpenCV 3.0+
	        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3072) # Change to 4096 for 4k resolution
	        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1680) # Change to 2160 for 4k resolution
	        self.cap.set(cv2.CAP_PROP_FPS, 30)
		else:
			# Set camera resolution - Using OpenCV 2.4
	        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 3072) # Change to 4096 for 4k resolution
	        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1680) # Change to 2160 for 4k resolution
	        self.cap.set(cv2.cv.CV_CAP_PROP_FPS, 30)

    def get_frame(self):
        # Read from camera
        ret, frame = self.cap.read()

        # Return only the frame
        return frame
