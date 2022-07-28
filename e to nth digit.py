import math
places = int(input('How many decimal places?: '))
if places > 15:
    places = 15
print(f'{math.e:.{places}f}')
