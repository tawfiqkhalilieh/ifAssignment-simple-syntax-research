x: int  = 5

# This code crashes
if x = 10:
    print ("Hello")
else:
    print("No")

# but we have a nice syntax in python
if x := 10:
    print ("Hello")
else:
    print("No")
