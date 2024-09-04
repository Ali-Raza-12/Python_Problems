# Python Program to Convert Centimeters to Feet and Inches

cm = int(input('Ente num:'))

# 1cm = 0.3937 inches
# 1cm = 0.03281 feet

feet = cm * 0.03281
inches = cm * 0.3937

print("The length in inches",round(inches,2))
print("The length in feet",round(feet,2))