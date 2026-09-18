name=input("What is your name?")
height=float(input("Enter your height:"))
height_meters= (height/100)
INCH= 2.54
height_inches= (height/INCH)
print("Hi"+name)
print("Your height is:"+str(height_meters)+"m")
print("Your height is:"+ str(height_inches)+"inch")
if height > 180: 
    print("True")
else:
    print("False")

f