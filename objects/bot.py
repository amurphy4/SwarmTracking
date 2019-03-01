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
        self.__x = None
        self.__y = None

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

    def get_center(self):
        if self.__x is None:
            # Calculate center point
            self.__x = int((self.__tl.x + self.__tr.x + self.__br.x + self.__bl.x) / 4)
            self.__y = int((self.__tl.y + self.__tr.y + self.__br.y + self.__bl.y) / 4)
        
        return self.__x, self.__y

    def set_center(self, x, y):
        self.__x = x
        self.__y = y
