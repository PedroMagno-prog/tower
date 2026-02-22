from models.models import *
"""
segment = []
segment.append(CharacterSheetField("Strength", 5, "How strong and tough the character is!"))
segment.append(CharacterSheetField("Dexterity", 3, "How fast and agile the character is!"))
sheet = Sheet(segment)

# sheet = segments[]
# segments[field
#field index: 0
# field = {name:"Strength", value:5, description:"How strong and tough the character is!"}

for i in range(len(sheet.segments)):
    print(sheet.segments[i])
for x in range(sheet):
    #for each field in sheet
    print(sheet[x].name)
    print(sheet[x].value)
    print(sheet[x].description)
    """

from scipy.interpolate import lagrange
import numpy as np
from random import choice

# Usage example with scipy
x = [1, 50, 100]
y = [80, 55, 10]

# Create the interpolating polynomial function
# poly = lagrange(x, y)
#
# # Estimate a value
# print(poly(90))
#
# print("="*56)

# C = 80
# D = int(input("Dif: --> "))
# #D goes from 0 to 100
# D_reducer = C -(C * (D/100))
# print(D_reducer)
# print(C-D_reducer)

