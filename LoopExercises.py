# print "1 through 10"
# for i in range(1, 11):
#     print i
#
# start = int(raw_input("Starting number? "))
# finish = int(raw_input("Ending number? "))
# print "n to m"
# for i in range(start, (finish + 1)):
#     print i
#
# print "Odd Numbers"
# for i in range(1, 10, +2):
#     print i
#
# print "Print a Square"
# size = 5
# for i in range(size):
#     print ("*" * size)
#
# print "Print a Square II"
# size = int(raw_input("What size box do you want? "))
# for i in range(size):
#     print ("*" * size)

# print "Print a Box"
# height = int(raw_input("Height? "))
# width = int(raw_input("Width? "))
# print ("*" * width)
# for i in range(height - 2):
#     print ("*" + (" " * (width - 2)) + "*")
# print ("*" * width)

# print "Print a Triangle"
# print "   *"
# print "  ***"
# print " *****"
# print "*******"
#
# print "Print a Triangle 2"
# height = int(raw_input("Height? "))
# for i in range(height):
#     stars = (i * 2) + 1
#     spaces = (height - i) - 1
#     #print stars
#     print (spaces * " ") + (stars * "*")

# print "Multiplication Table"
# myNumber = int(raw_input("What number would you like to multiply? "))
# myRange = 10
# for i in range(myRange + 1):
#     print "%r X %r = %r" % (i, myNumber, (i * myNumber))

# print "Print a Banner"
#
# message = str(raw_input("What's your message? "))
#
# print ("**" + ("*" * len(message)) + "**")
# print ("* " + message + " *")
# print ("**" + ("*" * len(message)) + "**")
#
# for i in range(100):
#     print (i * (i + 1))/2

my_number = int(raw_input("What's your number? "))

for i in range(my_number):
    if my_number % (i + 1) == 0:
        print (i + 1)

import math
for i in range(my_number):
    factor = math.ceil(math.sqrt(my_number))
    
