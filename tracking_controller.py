import cv2, threading

from camera import *
from tag_detection import *

class TrackingController:
    
    # Set up singleton pattern
    __instance = None

    @staticmethod
    def getInstance():
        """Singleton getInstance method"""
        
        if TrackingController.__instance == None:
            TrackingController()

        return TrackingController.__instance

    def __init__(self):
        # Set up singleton instance
        if TrackingController.__instance != None:
            raise Exception('Invalid invocation of singleton class "TrackingController"')
        else:
            TrackingController.__instance = self
        
        # Set up constants
        self.__camera = Camera()
        self.__tag_detection = TagDetection()

        # Tag offset angle
        self.__tag_offset = 0

        # Callback for returning data from tracking thread
        self.__callback = None

        # Used to stop the tracking thread
        self.__looping = True
		
	self.__show_frame = False

    def set_callback(self, callback):
        """Set callback method to be used to return data from tracking thread"""
        
        self.__callback = callback

    def set_tag_offset(self, offset):
        self.__tag_offset = offset
		
    def set_show_frame(self, show_frame):
	self.__show_frame = show_frame

    def start(self):
        """Start the tracking thread"""
        
        thread = TrackingThread(1, "tracking", 1)
        thread.start()

    def once(self):
        """Run SwarmTracking for only one frame"""
        
        self.__looping = False
        self._track()

    def stop(self):
        """Stop the tracking thread"""
        
        self.__looping = False

    def _track(self):
        """Track ArUco tags in the camera frame and trigger callback to return data about the detected bots"""
        
        while self.__looping:
            frame = self.__camera.get_frame()

            # Get a list of bots (each ArUco tag is a bot)
            bots = self.__tag_detection.detect_tags(frame, self.__tag_offset)

            # Trigger callback
            self.__callback(bots, frame)

            # Emulate do-while loop
            if not self.__looping:
                break
			
	    if self.__show_frame:
            	# Display image with tag outlines & other augments - resize to fit screen
	        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
	        cv2.resizeWindow("Camera", 1280, 720)
	        
	        cv2.imshow("Camera", frame)

	        if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break

### Threading necessary to prevent the tracking function from blocking on the main thread ###
class TrackingThread(threading.Thread):
    """Thread to run the tag detection without blocking all other functionality"""
    
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        TrackingController.getInstance()._track()
    

if __name__ == "__main__":
    controller = TrackingController()
    controller.start()
