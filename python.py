#!/bin/python
file = open("fullname.txt", "r")
#print file.read()

for line in file:
        #print line
        name =  line.rstrip().split(":",)
        print "last name : ", name[1]
