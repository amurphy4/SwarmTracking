from coord import *

class Bot:
    """Abstract class to represent a swarm robot and its position in the frame"""

    def __init__(self, tl, tr, br, bl, bot_id=None):
        # Corners
        self.__tl = tl
        self.__tr = tr
        self.__br = br
        self.__bl = bl

        # ID from ArUco tag
        self.__id = bot_id

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

    def get_centre(self):
        if self.__centre_point is None:
            # Calculate center point
            x = int((self.__tl.x + self.__tr.x + self.__br.x + self.__bl.x) / 4)
            y = int((self.__tl.y + self.__tr.y + self.__br.y + self.__bl.y) / 4)

            self.__centre_point = coord(x, y)
        
        return self.__centre_point

    def set_centre(self, x, y):
        self.__centre_point = coord(x, y)

    def set_front_point(self, x, y):
        self.__front_point = coord(x, y)

    def get_front_point(self):
        return self.__front_point
