import pyautogui as pt # Import the pyautogui library as pt
import time # Import the time library

limit = int(input("Enter Limit: ")) # Get the limit from the user and convert it to integer
message = input("Enter Message: ") # Get the message from the user

i = 0 # Initialize a variable i to 0, which will be used as a counter in the loop

time.sleep(3) # Pause the program for 3 seconds

# Start a while loop that will run as long as i is less than limit
while i < limit:
    
    pt.typewrite(message) # Type the message using the typewrite function from pyautogui library
    pt.press("enter") # Press the enter key using the press function from pyautogui library
    
    i+=1 # Increment i by 1 after each iteration of the loop
