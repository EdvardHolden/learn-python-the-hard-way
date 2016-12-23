# Program to introduce functions

def print_two_1(*args):
    arg1, arg2 = args
    print "arg1: %s arg2: %s" % (arg1, arg2)

def print_two_2(arg1, arg2):
    print "arg1: %s arg2: %s" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %s" % arg1

def print_none():
    print "None"


print_two_1("Zed","Shaw")
print_two_2("Zed","Shaw")
print_one("First!")
print_none()