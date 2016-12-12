from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again: \n >",
file_again = raw_input()

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
