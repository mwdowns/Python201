import sys
my_string = "this is a string"
back_string = ""
secret_string = "lbh zhfg hayrnea jung lbh unir yrnearq"

print my_string
print str.upper(my_string)
print str.capitalize(my_string)
#print my_string[::-1]
for char in my_string:
    back_string = char + back_string
print back_string

print ord("a"), ord("a") + 13, chr(ord("a") + 13)
#print chr((ord("a") + 1)), chr((ord("b") + 1)), chr((ord("c") + 1))

#for i in my_string:
#    new_string = chr(ord(i) + 1)
#    sys.stdout.write(new_string)

#for i in secret_string:
#    new_secret_string = chr(ord(i) - 2)
#    sys.stdout.write(new_secret_string)

paragraph = "This is my paragraph. And it's great. I fee like a dumbass. And I'm having a hard time. It's not as fun today."
leetList = ["A", "E", "G", "I", "O", "S", "T"]
leetSpeak = ["4", "3", "6", "1", "0", "5", "7"]
newList = list(str.upper(paragraph))
for char in newList:
    if 
