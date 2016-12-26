# Program to introduce for-loops

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricotes']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# The first for loop goes through a list
for number in the_count:
    print "This is count %d" % number

# Same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice how we have to use %r since we don't know whats in it
for i in change:
    print "I got %r" % i

# Building a list from an empty list
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

# Printing the list
for i in elements:
    print "Element was: %d" % i

