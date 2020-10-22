import sys

def arg_check(a, b):
    return((a % b == 0) or (b % a == 0))

arg_check(sys.argv[1], sys.argv[2])