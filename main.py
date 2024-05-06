# importing libraries
from math import pi
from numpy import cos, sin
from sympy import symbols, Eq, solve
intError = 'Error: integer expected'

# welcome message
print('Welcome to the static tension problem solver for ropes!')
print()
print('Please note that all inputs to the program must be integers. Decimals are not supported.')
print()

# input prompt for sig figs
sigDig = input('Please enter your desired number of significant digits: ')

# checking if input is valid
if sigDig.isdigit():
    sigDig = int(sigDig)
    print('Accepted:', sigDig, 'significant digits.')
else:
    print(intError)
    exit()

# input prompt for object's weight
timmyWeight = input('Enter weight of load in kg: ')
if timmyWeight.isdigit():
    timmyWeight = int(timmyWeight)
    print('Accepted:', timmyWeight, 'kg')
else:
    print(intError)
    exit()

# converting kg to kN
timmyForce = timmyWeight * .00980665
print('Force of gravity acting on load:', timmyForce, 'kN')

# input prompt for rope angle A
angleA = input('Enter first rope angle in degrees: ')

# checking if input is valid
if angleA.isdigit():
    angleA = int(angleA)
else:
    print(intError)
    exit()

if 0 < angleA < 90:
    print('Accepted:', angleA, 'degrees')
else:
    print('Domain Error: Angle must be between 0 and 90 degrees.')
    exit()

# input prompt for rope angle B
angleB = input('Enter second rope angle in degrees: ')

# checking if input is valid
if angleB.isdigit():
    angleB = int(angleB)
else:
    print(intError)
    exit()

if 0 < angleB < 90:
    print('Accepted:', angleB, 'degrees')
else:
    print('Domain Error: Angle must be between 0 and 90 degrees.')
    exit()

# final validity check
tAngle = angleA + angleB
if tAngle > 180:
    print('Error: sum of both angles is greater than 180')
    exit()

# converting degrees to radians
radFactor = pi / 180
angleA = angleA * radFactor
angleB = angleB * radFactor

# calculating solutions
A, B = symbols('A B')
eq1 = Eq(-A*cos(angleA) + B*cos(angleB), 0)
eq2 = Eq(A*sin(angleA) + B * sin(angleB)-timmyForce, 0)
solnDict = solve((eq1,eq2),(A,B))

# printing solutions
print(f'Tension on first rope: {round(solnDict[A],sigDig)} kN')
print(f'Tension on second rope: {round(solnDict[B],sigDig)} kN')

# exit message
print('Thank you for using this program! I hope you found it helpful ;)')
