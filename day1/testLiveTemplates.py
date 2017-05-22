import math
class Point:
    """
    Represents a point in a 2-D geometric space.
    """
    def __init__(self, x=0, y=0):
        """
        Initializes the position of a new point.
        If they are not specifie dthe point defaults to the origin.
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the point to the origin location.
        :return: nothing
        """
        self.move(0,0)

    def move(self, x, y):
        """
        Move a point to a new location in 2 - D space.
        :param x: x coordinate
        :param y: y coordinate
        :return: nothing
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance between this point and another point passed as a parameter.
        This function uses the pythagorean theorem to calculate the distance.
        :param other_point: The second point to calcualte the distance.
        :return: The distance between two points (float).
        """
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)



def main():
    p1 = Point()
    print(p1.x, p1.y)

    p2 = Point(5, 8)
    print(p2.x, p2.y)
    #test distance
    print(p1.calculate_distance(p2))
    #test tool (assert)
    #program will exit if False (or Zero, empty, none)
    assert (p2.calculate_distance(p1) ==
            p1.calculate_distance(p2))


if __name__ == '__main__':
    main()
    exit(0)