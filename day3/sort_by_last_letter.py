store = []

def sort_by_last_letter(stringy):
    """
    Task Define a function that takes a list of strings as input parameter.
    Define a local function that returns the last letter of the string.
    :param stringy: a list of strings
    :return: Main fucntion returns a sorted list based on the last letter.
    """

    # a local function
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)

    # hint use the local fucntion as a lambda to the sorted built-in fucntion
    return sorted(stringy, key=last_letter)


def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message


def html_tag(tag):
    """
    Creates an HTML tag based on input
    :param tag: Tag
    :return: a callable function
    """
    def wrap_text(msg):
        print ("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text



def main():
    names = ["Tim", "John", "Peter", "El Chapo", "Erica"]
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))

if __name__ == '__main__':
    main()
    exit(0)