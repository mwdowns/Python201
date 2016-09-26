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

print "Pring a Box"
height = int(raw_input("Height? "))
width = int(raw_input("Width? "))
for i in range(height):
    print ("*" * width)
