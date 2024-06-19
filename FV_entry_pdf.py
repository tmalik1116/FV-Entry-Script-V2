# Modified Python script for automation of adding deficiencies to Field View V2.0

# V1.0 read Excel data from a .csv file and required more logic in order to convert a task to its subtrade,
# and for correctly identifying and selecting the location of the deficiency within the building based on its description.

# This version reads from a .txt file (which I had already converted from a pdf using different Python code),
# and assigns all deficiencies to Chandos, due to the absence of the correct subtrade in the Field View list.

# This is not a plug and play solution, it was designed to work with my specific computer setup. However it can be adapted 
# quite easily to be much more broadly applicable.

# Talha Malik, June 19, 2024

import pynput
from pynput.mouse import Button, Controller
import time
import keyboard

# Converts subtrade to expected 'Package' by Field View
def convert_trade(name):
    match name:
        case "Benmar":
            return "drywall"
        # case "Branch A/V":
        #     return "" ### not in FV
        case "CCL":
            return "chandos"
        # case "EN3":
        #     return  ### not in FV
        case "JDA":
            return "miscellaneous"
        case "Lab Flooring":
            return "flooring"
        case "Ladson":
            return "millwork"
        case "PPG":
            return "electrical"
        # case "SDR Seating":
        #     return "" ### not in FV
        case "Swift":
            return "mechanical"
        case "Tuygun":
            return "painting"
        case "Upper Canada":
            return "doors"
        case "Westmount":
            return "glazing"
        case default:
            return "nothing"
        
def location(item):
    if item[2].startswith('B'):
        mouse.click(Button.left, 1)
    elif item[2].startswith('1'):
        mouse.move(0, 35)
        mouse.click(Button.left)
        mouse.move(0, -35)
    elif item[2].startswith('2'):
        mouse.move(0, 70)
        mouse.click(Button.left, 1)
        mouse.move(0, -70)
    else:
        mouse.move(0, 105)
        mouse.click(Button.left, 1)
        mouse.move(0, -105)

mouse = Controller()
mouseX = 1330

fp = open("pdftext.txt", 'r')
text = fp.read()
data = text.split('\n')

counter = 0


for i in range(len(data)): # item is a row
    counter += 1

    mouse.position = (mouseX, -300) # Add task
    time.sleep(0.5)
    mouse.click(Button.left, 1) # click
    time.sleep(0.5)

    # select deficiency
    mouse.move(0, 50) # change relative position
    time.sleep(0.25)
    mouse.click(Button.left, 1) # click
    time.sleep(0.25)


    mouse.move(0, 70)
    time.sleep(0.5)
    mouse.click(Button.left, 1)

    # click on text box
    time.sleep(0.5)
    mouse.move(0, 30)
    time.sleep(0.25)
    mouse.click(Button.left, 1)

    # desc = data[i][3]
    keyboard.write(data[i])

    # selecting location CC (can change later)
    mouse.move(0, 115)
    time.sleep(0.25)
    mouse.click(Button.left, 1)

    
    mouse.move(100, 170)
    mouse.click(Button.left, 1)

    # Selecting architectural
    mouse.move(0, -30)
    mouse.click(Button.left, 1)

    mouse.move(-100, 0)

    time.sleep(0.25)
    mouse.move(0, 150)
    mouse.click(Button.left, 1)

    
    # Positioning over search bar (trade type) and type value
    time.sleep(0.25)
    mouse.move(0, 30)
    mouse.click(Button.left, 1)

    keyboard.write("chandos")

    # Select Package
    time.sleep(0.25)
    mouse.move(0, 50)
    time.sleep(0.25)
    mouse.click(Button.left, 1)


    # Scroll down
    time.sleep(0.25)
    for k in range(10):
        keyboard.send("down")

    # Click on Priority
    time.sleep(0.25)
    mouse.move(0, -20)
    time.sleep(0.25)
    mouse.click(Button.left, 1)

    # Select medium priority (can be changed)
    time.sleep(0.25)
    mouse.move(0, 100)
    time.sleep(0.25)
    mouse.click(Button.left, 1)


    time.sleep(0.25)
    mouse.move(0, 80)
    mouse.click(Button.left, 1)

    # This delay may need to be lengthened on systems with a slow internet connection. If the page does not reload within 2.5s the program behave unexpectedly.
    time.sleep(2.5)
