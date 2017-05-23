import math

def triangle_area(a, b, c):
    p = ((a + b + c )/ 2)
    a = math.sqrt(p*(p-a)* (p-b)* (p-c))
    return a

def main():
    #works for legitimate triangles
    print(triangle_area(3, 4, 5))


if __name__ == '__main__':
    main(   )
    exit(0)