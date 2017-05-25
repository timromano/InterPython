import math
import sys
import traceback

class TriangleError(Exception):
    """"
    Over write methods from base class.
    """
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)


    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "TriangleError({!r}, {!r})".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)
    p = ((a + b + c )/ 2)
    a = math.sqrt(p*(p-a)* (p-b)* (p-c))
    return a

def main():
    #works for legitimate triangles

    try:
        a = triangle_area(3, 4, 10)
        print(a)
    except TriangleError as e:
        #Cause and unsupported operation experience by
        #trying to prin to the standard-in stream instead
        #of std-out
        print(e, file =  sys.stdin)


class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy/dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e


def test_inclination():
    try:
        print(inclination(0, 5))
    except InclinationError as e:
        print(e.__traceback__)
        #Don't keep a refernce to dunder traceback beyond the scope of the except block
        s = traceback.format_tb(e.__traceback__)
        print(s)

if __name__ == '__main__':
    #main()
    #print(inclination(3, 5))
    #horizontal component is zero
    #print(inclination(0, 5))
    test_inclination()
    print("Finished")

    exit(0)