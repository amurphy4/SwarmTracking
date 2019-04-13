import cv2, math
import cv2.aruco as aruco

from objects import Bot, coord

class TagDetection:

    def __init__(self):
        # ArUco tag detection constants
        self.ARUCO_PARAMS = aruco.DetectorParameters_create()
        self.ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_1000)

        self.bots = []

    def detect_tags(self, frame, offset, augment_frame):
        # Ensure we have a clean bot array - also keeps on top of memory usage
        del self.bots[:]
        
        # Convert image to greyscale
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect tags
        tags, ids, rejects = aruco.detectMarkers(grayscale, self.ARUCO_DICT, parameters=self.ARUCO_PARAMS)

        if ids is not None:
            # Tags were found

            if augment_frame:
                # Outline tags on frame if augment_frame is enabled
                aruco.drawDetectedMarkers(frame, tags, borderColor = (0, 255, 0))

            index = 0
            
            for tag in tags:
                corners = tag.tolist()[0]

                # Individual corners (e.g. tl = top left corner in relation to the tag, not the camera)
                tl = coord(corners[0][0], corners[0][1])
                tr = coord(corners[1][0], corners[1][1])
                br = coord(corners[2][0], corners[2][1])
                bl = coord(corners[3][0], corners[3][1])

                # Create bot instance
                bot = Bot(tl, tr, br, bl, ids[index][0], offset)
                self.bots.append(bot)

                # Get centre of the tag
                centre = bot.get_centre()
                cX = centre.x
                cY = centre.y

                if augment_frame:
                    # Draw circle on center point if augment_frame is enabled
                    cv2.circle(frame, (cX, cY), 5, (0, 255, 0), -1)

                # Get corners as coordinates - easier to work with
                tl, tr, br, bl = bot.get_corners()

                # Get centre of top of tag
                tX = int((tl.x + tr.x) / 2)
                tY = int((tl.y + tr.y) / 2)

                # Translate top point around negative of centre (pivot) point
                tX = tX - cX
                tY = tY - cY

                # Angle to rotate point by
                theta = math.radians(offset)
                
                nX = int(tX * math.cos(theta) - tY * math.sin(theta))
                nY = int(tX * math.sin(theta) + tY * math.cos(theta))

                # Translate back
                nX = nX + cX
                nY = nY + cY

                bot.set_front_point(nX, nY)

                if augment_frame:
                    # Draw arrowed line from centre point to front of bot (shows direction of movement) if augment_frame is enabled
                    cv2.arrowedLine(frame, (cX, cY), (nX, nY), (0, 255, 0), 2)
    
                # Increment index for next pass through
                index = index + 1

        return self.bots
