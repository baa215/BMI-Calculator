import math
import sys


def heightcal(ft, inches): # calculates the height into inches 
    heighttotal = (ft * 12) + inches
    return heighttotal

def bmical(weight, height): # gets the bmi 

    bmi = weight / (height)
    return bmi


if sys.stdin.isatty():
    # script is being run interactively, prompt for input
    heightinput = heightcal(float(input("Please enter your height in feet: ")), float(input("Please enter your height in inches: ")))
    weightinput = float(input("Please enter your weight in pounds: "))
else:
    # script is being run non-interactively, read input from command line arguments
    heightinput = heightcal(float(sys.argv[1]), float(sys.argv[2]))
    weightinput = float(sys.argv[3])

height = (heightinput * 0.025)**2 # does the conversion to meters 
weight = weightinput * 0.45 # does the coversion to metric system 

BMI = bmical(weight, height) # calls the bmi cal


print("Your BMI is: ")
print(round(BMI)) # makes bmi a whole number 

if(BMI>0): # compares bmi to all of these to find the correct one
    if(BMI<=18.5):
        print("You are underweight.")
    elif(BMI<=25):
        print("You are the normal weight.")
    elif(BMI<=30):
        print("You are overweight.")
    else: 
        print("You are obese.")
