# Created by: David Wang
# Created on: 7-Nov-2017
# Created for: ICS3U
# Daily Assignment - Unit4-05
# This program displays the volume of a cylinder, given radius and height

PI = 3.14

def calculate_volume(user_height, user_radius):
    #When called this function uses radius and height to calculate volume
    
    user_volume = PI * (user_radius**2) * user_height
    
    return user_volume

while True:
    height = raw_input('Enter the height of the cylinder in cm: ')
    try:
        height = float(height)
        break
    except:
        print('Please enter a valid number')

while True:
    radius = raw_input('Input the radius of the cylinder in cm: ')
    try:
        radius = float(radius)
        volume = calculate_volume(height, radius)
        print('The volume of the cylinder is: ' + str(volume) + 'cm^3')
        break
    except:
        print('Please enter a valid number')
