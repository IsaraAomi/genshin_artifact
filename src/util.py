import sys

def print_info(object):
    print("[INFO] {0}".format(object))


def print_warning(object):
    print("[WARNING] {0}".format(object))


def print_error(object):
    print("[ERROR] {0}".format(object))
    sys.exit(1)
