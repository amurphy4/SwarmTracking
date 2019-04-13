import math

from coord import *

class Bot:
    """Abstract class to represent a swarm robot and its position in the frame"""

    def __init__(self, tl, tr, br, bl, bot_id=None, offset=None):
        # Corners
        self.__tl = tl
        self.__tr = tr
        self.__br = br
        self.__bl = bl

        # ID from ArUco tag
        self.__id = bot_id

        # Tag offset
        self.__tag_offset = offset

        # Center point
        self.__centre_point = None

        # Point of front of bot
        self.__front_point = None

    def get_corners(self):
        return self.__tl, self.__tr, self.__br, self.__bl

    def set_corners(self, tl, tr, br, bl):
        self.__tl = tl
        self.__tr = tr
        self.__br = br
        self.__bl = bl

    def get_id(self):
        return self.__id

    def set_id(self, bot_id):
        self.__id = bot_id

    def get_tag_offset(self):
        if self.__tag_offset == None:
            return 0

        return self.__tag_offset

    def set_tag_offset(self, offset):
        self.__tag_offset = offset
        
    def get_centre(self):
        x = int((self.__tl.x + self.__tr.x + self.__br.x + self.__bl.x) / 4)
        y = int((self.__tl.y + self.__tr.y + self.__br.y + self.__bl.y) / 4)

        self.__centre_point = coord(x, y)
        
        return self.__centre_point

    def set_centre(self, x, y):
        self.__centre_point = coord(x, y)

    def set_front_point(self, x, y):
        self.__front_point = coord(x, y)

    def get_front_point(self):
        # Get centre of the tag
        centre = self.get_centre()
        cX = centre.x
        cY = centre.y
        
        # Get corners as coordinates - easier to work with
        tl, tr, br, bl = self.get_corners()

        # Get centre of top of tag
        tX = int((tl.x + tr.x) / 2)
        tY = int((tl.y + tr.y) / 2)

        # Translate top point around negative of centre (pivot) point
        tX = tX - cX
        tY = tY - cY

        # Angle to rotate point by
        theta = math.radians(self.get_tag_offset())
            
        nX = int(tX * math.cos(theta) - tY * math.sin(theta))
        nY = int(tX * math.sin(theta) + tY * math.cos(theta))

        # Translate back
        nX = nX + cX
        nY = nY + cY

        self.__front_point = coord(nX, nY)
        
        return self.__front_point
