from random import randrange

def test_random():
    #random # between 0 and 99.
    number = randrange(100)
    while True:
        guess = int(input("? "))
        if guess == number:
            print("You guessed it!")
            break


def exception_hierarchy():
    S = [1, 4, 6]
    #print (S[28])
    d = dict(a = 65, b = 66, c = 67)
    #print(d('g'))

def lookups():
    s = [1, 2, 3]
    try:
        item = s[5]
    #except IndexError:
    except LookupError:
        print("Got an IndexError")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    #except KeyError:
    except LookupError:
        print("Got an KeyError")

def median(iterable):
    """
    Obtain the median value of a series. Sort the iterable and returns
    the middle value if there is an odd number of elements. Or the
    arithmetic mean of the middle two lements if there are an even number of elements.
    :param iterable: a series of irderable items.
    :return: the median of the series.
    """
    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError("median() arg is an empty list.")

    median_index = (len(items)-1)//2
    if len(items)%2 != 0: # odd number of members
        return items[median_index]
    #even number of members
    return ((items[median_index]+ items[median_index+1])/2.0)

def test_median():
    """"
    Exception payloads are strings and are passed as a single arguement to an exception constructor.
    Use args exception attribute.

    Output: a single element tuple containing the message that was passed to the constructor.
    Another way is to use the str() constructor method.
    Reference PEP 352
    """
    try:
        median([])
    except ValueError as e:
        print("Payload:", e.args)
        print(str(e))

def more_info():
    try:
        b'\x81'.decode('utf-8')
    except UnicodeError as e:
        print(e)
        print('encoding: ', e.encoding)
        print('reason: ', e.reason)
        print('object: ', e.object)
        print('end: ', e.end)

def main():
    #test_median()
    more_info()

    #test_random()
    #exception_hierarchy()
    #lookups()
    #print(median([5, 2, 1, 4, 3]))

    #print(median([5, 2, 1, 4, 3, 9]))

    #print(median([]))


if __name__ == '__main__':
    main()
    exit(0)