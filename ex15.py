# Program to open a file and read it's content

from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r: " % filename
print txt.read()

print "Type your filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()