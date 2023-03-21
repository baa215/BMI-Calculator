import math

def bmical(weight, height):

    bmi = weight / (height)
    return bmi


def heightcal(ft, inches):
    heighttotal = (ft * 12) + inches
    return heighttotal

heightinput = heightcal(float(input("Please enter your height in feet: ")), float(input("Please enter your height in inches: ")))

weightinput = float(input("Please enter your weight in pounds: "))

height = (heightinput * 0.025)**2
weight = weightinput * 0.45

BMI = bmical(weight, height)


print("Your BMI is: ")
print(round(BMI))

if(BMI>0):
    if(BMI<=18.5):
        print("You are underweight.")
    elif(BMI<=25):
        print("You are the normal weight.")
    elif(BMI<=30):
        print("You are overweight.")
    else: 
        print("You are obese.")