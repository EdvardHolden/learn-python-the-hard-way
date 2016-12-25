# Program to introduce the basic logic operators

print True and True # EO: T
print False and True # EO: -
print 1 == 1 and 2 == 1 # EO: -
print "test" == "test" # EO: T
print 1 == 1 or 2 != 1 # EO: T
print True and 1 == 1 # EO: T
print False and 0 != 0 # EO: -
print True or 1 == 1 # EO: T
print "test" == "testing" # EO: -
print 1 != 0 and 2 == 1 # EO: -
print "test" != "testing" # EO: T
print "test" == 1 # EO: -
print not (True and False) # EO: T
print not (1 == 1 and 0 != 1) # EO: -
print not (10 == 1 or 1000 == 1000) # EO: -
print not (1 != 10 or 3 == 4) # EO: -
print not ("testing" == "testing" and "Zed" == "Cool Guy") # EO: T
print 1 == 1 and (not ("testing" == 1 or 1 == 0)) # EO: T
print "chunky" == "bacon" and (not (3 == 4 or 3 == 3)) # EO: -
print 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) # EO: -