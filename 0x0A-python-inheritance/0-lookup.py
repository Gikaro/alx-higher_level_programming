
dule to lookup for available methds"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj (object): the given object

    Returns:
        (list): objects list

    """
    return dir(obj)
