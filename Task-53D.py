# Importing the libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
redled = LED(18)

# GUI Definitions: Create the main window
win = Tk()
win.title("MORSECODE BLINKER")

# Define a custom font for the GUI
myFont = tkinter.font.Font(family='poppins', size=20, weight="bold")

def dot():   # Define a function to turn on the LED for a dot in Morse code
    redled.on()
    time.sleep(2)
    redled.off()
    time.sleep(1)
    
def dash():  # Define a function to turn on the LED for a dash in Morse code
    redled.on()
    time.sleep(3)
    redled.off()
    time.sleep(2)
    
  # Define a dictionary to map characters to their Morse code representations  
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..'
}

# Define a function to handle when the entry field is clicked (focus in)
def placeholder_in(event):
    if text_box.get() == placeholder:
        text_box.delete(0, "end")  # Remove the placeholder text when the user clicks on the entry field
        text_box.config(fg='black')  # Change the text color to black

# Define a function to handle when the entry field loses focus (focus out)
def placeholder_out(event):
    if text_box.get() == "":
        text_box.insert(0, placeholder)  # Add back the placeholder text when focus is lost
        text_box.config(fg='grey')  # Change the text color to grey

# Define a function to convert user input text to Morse code and blink the LED accordingly
def Morsecode():
    word = text_box.get().upper()  # Convert the input text to uppercase
    if len(word) > 12:
        print("Name exceeds the character limit of 12. LED will not blink.")
        return

    print(word)
    for element in word:
        if element in morse_code:  # Check if the character is in your Morse code dictionary
            for symbol in morse_code[element]:
                if symbol == '.':
                    dot()
                elif symbol == '-':
                    dash()
                else:
                    time.sleep(0.5)
        else:
            # Handle the case where the character is not in the Morse code dictionary
            time.sleep(1)  # You can add your own behavior here

    print("The name you have entered is blinked !")

# Define a function to clean up GPIO and close the application window
def Exit():
    # Cleanup GPIO and close the application window
    GPIO.cleanup()
    win.destroy()
    
Label(win, text='Enter the name', bg='pink', font=myFont, height=1, width=30).grid(row=0, column=1)

placeholder = "Enter your text here!!"  # The placeholder text

# Create the entry widget with a grey text color for the placeholder
text_box = Entry(win, width=30, bg='lightslategrey', font= myFont, fg='black')
text_box.insert(0, placeholder)  # Set the initial text to the placeholder
text_box.grid(row=1, column=1)
text_box.bind("<FocusIn>", placeholder_in)
text_box.bind("<FocusOut>", placeholder_out)

# Define a function to clean up GPIO and close the application window
submitButton = Button(win, text='Submit', font=myFont, command=Morsecode, bg='teal', width = 10)
submitButton.grid(row=3, column=1)

# Create an exit button that triggers the Exit function
Exit_Button = Button(win, text='Exit', font=myFont, command=Exit, height=1, width=10, bg='lightblue')
Exit_Button.grid(row=4, column=1)

win.mainloop()
