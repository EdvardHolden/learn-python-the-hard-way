# Program for basic string formatting

name = 'Edvard Holden'
age = 20
height_metric = 176
weight_metric = 180
eye_colour = 'Blue'
hair_colour = 'Blonde'

print "Lets talk about %s." % name
print "He's %d cm tall." % weight_metric
print "He's %d kg heavy." % weight_metric
print "He's got %s eyes and %s hair." % (eye_colour, hair_colour)

print "If we add %d, %d and %d we get %d." % (age, height_metric, weight_metric,
    age + height_metric + weight_metric)


