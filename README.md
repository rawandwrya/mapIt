# mapIt
Python program that copies long,lat coordinates of an address from the clipboard and open the google map's online page of that coordinate on a browser.

# Instructions
Copy the adress
  the adress is recommended tobe <longtitude>,<lattitude>
  although names and other forms of addresses might work, but accurate results will not be guaranteed
Run mapIt.py from a terminal

# Documentations

## Dependencies
The program needs to import "webbrowser" and "pyperclip" python modules

## Running the Program
when running the mapIt.py from a terminal:
  ### imports all the necessary modules
  ### the adress value will be stored
  ### google map's URL link will be constructed and stored in a variable
  ### webbrowser module's open() function will be called to launch the the google maps URL

## Limitations
the programs is subject to webbrowser module limitations such as scanning only UNICODE characters.




