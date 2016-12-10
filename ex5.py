# -*- coding: utf-8 -*-

my_name = '夏雨荷'
my_age = 23
my_height = 178 # cm
my_weight = 65  # kg
my_eyes = 'Black'
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d kg heavy."
print "Actually that's not too heavy."
print "he's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (my_age, my_weight, my_height, my_age + my_height + my_weight)
