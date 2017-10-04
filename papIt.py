#! python3
# mapIt.py - Launches a map in the browser  use an address from
# the commandline or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
     #get address from the commandline
     address = ' '.join(sys.argv[1:])
     #print (address)
#TODO: Get address from clipboard
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
