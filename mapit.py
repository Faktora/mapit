#! python3
import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

url = 'google.com/maps/places' + address
webbrowser.open(url)
""" the next line uses preferred browser to open links (usedName, constructor[usually None], instance[in this case .BackgroundBroser(path to .exe)]
webbrowser.register('Chrome', None,
                    webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
webbrowser.get('Chrome').open(url)
"""

