# About the Program 

This code is written in Python and uses the PyAutoGUI library to automate keyboard and mouse input. 
The code inputs a limit and a message from the user, then types the message and presses the "enter" 
key that many times.

Here is a detailed explanation of the code:

1. Import statements:
- The code imports the "pyautogui" library as "pt" and the "time" library.

2. Inputting limit and message:
- The code uses the "input" function to prompt the user to enter a "limit" (the number of times the message will be typed) 
  and a "message" (the text that will be typed).
  The "limit" is converted from a string to an integer using the "int" function.

3. Initializing the loop:
- The code initializes a variable "i" to 0, which will be used as a counter for the loop.
  The code then uses the "sleep" function from the "time" library to pause the program for 3 seconds.

4. The loop:
- The code uses a "while" loop that will run as long as "i" is less than "limit".
  Inside the loop, the code uses the "typewrite" function from the "pyautogui" library to type the message.
  The code then uses the "press" function from the "pyautogui" library to press the "enter" key.


## How to run?

To run this project use the following commands as shown.

```python
  cd spamtyper

  pip install -r requirements.txt

  python3 typer.py
```

