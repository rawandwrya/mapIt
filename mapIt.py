#! /usr/bin/python3

'''
This Program will auto launch a google maps window of a copied longtitude/lattitude location

1- copy the longtitude and lattitude of the location in the following format
<long>,<lat>.
2- OPTIONAL: you can copy the name of an adress, but it is not recommended since the result might not be as accurate
3- run the program

'''
#________________________________________________________________________________________________
import webbrowser
import pyperclip


__all__ = ['google_maps_launcher']


# define a function that launches a google map window browser
def google_maps_launcher():
	# store the copied value in long_lat_value
	long_lat_value = str(pyperclip.paste())
	# construct the correct google map link and store it in __url
	__url = "https://www.google.com/maps?q="+long_lat_value
	# store webbrowser.open(__url) in googlemaps_launcher
	googlemaps_launcher = webbrowser.open(__url)
	# return the launcher
	return googlemaps_launcher

# run the google_maps_launcher function
google_maps_launcher()



