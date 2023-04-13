import math
import sys

# calculates the height into inches
def heightcal(feet, inches):
    heighttotal = (feet * 12) + inches
    return heighttotal
# gets the bmi
def bmi_cal(weight, height):
    bmi = weight / (height)
    return bmi

if __name__ == "__main__":
    height_ft = float(sys.argv[1])
    height_in = float(sys.argv[2])
    weight_pounds = float(sys.argv[3])
    
    # does the conversion to meters
    height = (heightcal(height_ft, height_in) * 0.025)**2
    # does the coversion to metric system
    weight = weight_pounds * 0.45
    # calls the bmi cal
    BMI = bmical(weight, height)

    print("Your BMI is: ")
    # makes bmi a whole number
    print(round(BMI))

    # compares bmi to all of these to find the correct one
    if BMI>0:
        if BMI<=18.5:
            print("You are underweight.")
        elif BMI<=25:
            print("You are the normal weight.")
        elif BMI<=30:
            print("You are overweight.")
        else:
            print("You are obese.")
