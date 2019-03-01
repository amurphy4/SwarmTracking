import cv2, math
import cv2.aruco as aruco

from objects import Bot, coord

class TagDetection:

    def __init__(self):
        # ArUco tag detection constants
        self.ARUCO_PARAMS = aruco.DetectorParameters_create()
        self.ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_1000)

        self.bots = []

    def detect_tags(self, frame, offset):
        # Ensure we have a clean bot array - also keeps on top of memory usage
        del self.bots[:]
        
        # Convert image to greyscale
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect tags
        tags, ids, rejects = aruco.detectMarkers(grayscale, self.ARUCO_DICT, parameters=self.ARUCO_PARAMS)

        if ids is not None:
            # Tags were found
            # Outline tags on frame
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
                bot = Bot(tl, tr, br, bl, ids[index])
                self.bots.append(bot)

                # Get centre of the tag
                cX, cY = bot.get_center()

                # Draw circle on center point
                cv2.circle(frame, (cX, cY), 5, (0, 255, 0), -1)

                # Get corners as coordinates - easier to work with
                tl, tr, br, bl = bot.get_corners()

                # Get centre of top of tag
                tX = int((tl.x + tr.x) / 2)
                tY = int((tl.y + tr.y) / 2)

                radius = math.sqrt(math.pow((tX - cX), 2) + math.pow((tY - cY), 2))
                theta = 45

                #offX = int(tX + radius * math.cos(math.radians(90)))
                #offY = int(tY + radius * math.sin(math.radians(90)))
                #offX = int(radius * math.sin(math.radians(45)))
                #offY = int(radius * math.sin(math.radians(90 - 45)))
                #offX = int(radius / math.cos(theta))
                #offY = int((2 * radius * math.sin(theta / 2)) / (math.cos(((180 - theta) / 2) - 90 - theta)))
                #offY = int(radius * math.sin(theta))

                #nX = int(tX - (radius - offX))
                #nY = int(tY + offY)

                #print("X: {0} Y: {1} Theta: {2}".format(offX, offY, theta))

                #a = radius
                #b = radius
                #c = int(2 * radius * math.sin(90 / 2))
                #x = int((c*c - b*b + a*a) / (2*a))
                #y = int(math.sqrt(c*c - x*x))

                # Draw circle on centre of top line
                #cv2.arrowedLine(frame, (cX, cY), (nX, nY), (0, 255, 0), 2)
    
                # Increment index for next pass through
                index = index + 1

        return self.bots
