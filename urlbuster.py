import sys
from termcolor import cprint, colored



logo=colored(''' 

                    Welcome to Phishing Buster!

 ______  _     _      _     ______                               
(_____ \| |   (_)    | |   (____  \              _               
 _____) ) |__  _  ___| |__  ____)  )_   _  ___ _| |_ _____  ____ 
|  ____/|  _ \| |/___)  _ \|  __  (| | | |/___|_   _) ___ |/ ___)
| |     | | | | |___ | | | | |__)  ) |_| |___ | | |_| ____| |    
|_|     |_| |_|_(___/|_| |_|______/|____/(___/   \__)_____)_|    
                                    	Made by hei$enberg                              
                                                                                                                        

    ''', 'blue')

def help():
	ex=colored('$ python3 phishbuster.py <the url> <path/to/the/database>', 'blue')
	print(logo)
	print(f'''

This is a simple tool that checks if your provided url is in a phishing database.
To use the tool, specify the url databases location like this:

	{ex}

If you dont have a database, you can download it from here:



		''')

if sys.argv[1]=='-h' or sys.argv[1]=='--help' or sys.argv[1]=='help':
	help()
	sys.exit()


try:
	url=sys.argv[1]
	path=sys.argv[2]

	print(logo)
	with open(path, "r") as file:
	    file_contents = file.read()
	    if url in file_contents:

	        cprint('PHISHING DETECTED','red')
	    else:

	    	cprint('the URL was not found in the database.', 'blue')
except KeyboardInterrupt:
	cprint('exiting...', 'red')
except IndexError:
    cprint('    wrong parameters...', 'red')
except FileNotFoundError:
    cprint("file not found...", 'red')






