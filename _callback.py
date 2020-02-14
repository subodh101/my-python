from typing import Callable, Optional


def callback(sum: int):
    """
    As the name suggests call back. It's like calling something in the end or in the thread.

    Args:
        sum: just a variable

    """
    print("Sum = {}".format(sum))


def main(x: int, y: int, callback: Optional[Callable[[None], None]] = None):
    """
    Calling the call back function in the end.

    Args:
        x: variable
        y: variable
        callback: function

    """

    print("adding {} + {}".format(x, y))
    if callback:
        callback(x + y)


if __name__ == '__main__':
    main(2, 9, callback)
