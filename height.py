inches =[]
print ("Enter heights in inches. Type 'done' when finished.")
while True:
    x = input("Enter height in inches(or 'done' to finish): ")
    if x.lower() == 'done':
        break
    try:
        height_inch = float(x)
        inches.append(height_inch)
    except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
centimeters = [height * 2.54 for height in inches]
print("Heights in Inches:", inches)
print("Heights in centimeters:", centimeters)
