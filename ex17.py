from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

# We could do these two on one line, how?
in_file = open(from_file, "r")
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "ready, hit RETURN to contune, CTRL-C to abort."
raw_input()

out_file = open(to_file, "w+")
out_file.write(indata)

print "Alright, all done. \n"

in_file.close()
out_file.close()

in_file = open(from_file, "r")
out_file = open(to_file, "r")

print "in_file data: \n %r" % in_file.read()
print "out_file data: \n %r" % out_file.read()

in_file.close()
out_file.close()
