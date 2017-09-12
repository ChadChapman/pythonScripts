
#! python3
# mapNow takes cl args or clipboard contents, maps address in browser
# if no cl args given for location, will default to clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	#cl has args, get them
	mapAddress = ''.join(sys.argv[1:])
	
else:
	
# no cl args, get address from clipboard
	mapAddress = pyperclip.paste()
	
#now open browser, pass in url
webbrowser.open('https://google.com/maps/place/'+mapAddress)
