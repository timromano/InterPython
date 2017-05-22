class MyFirstClass:
    #We are following PEP8
    pass #pass does nothing

class Point:
    def reset(self):
        self.x = 0
        self.y = 0


def main():
#print(__name__)
#makes code more reusable
    p1 = Point()
    p2 = Point()

    # <object>.<attribute> = value
    p1.x = 5
    p1.y = 4

    print(p1.x, p1.y)

    p1.reset()
    print(p1.x, p1.y)


if __name__ == "__main__":
    main()
    exit(0)

