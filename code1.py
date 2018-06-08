import time
import os
import webbrowser
import urllib2
x=""" SELECT OPERATION
 Press 1 to check date and time
 press 2 to create a file
 press 3 to create a directory
 Press 4 to search something on google
 Press 5 to log out of system
 press 6 to shut down OS
 press 7 to check Internet connection in your laptop or PC
 press 8 to log in whatsapp on browswer
 press 9 to check all connected IP in your network
"""
print x
choice=raw_input("Enter any number between 1 to 9 ")
if choice=='1':
	print "showing date and time"
	print time.ctime()
if choice=='2':
	name1=raw_input("Enter name of the file")
	print "Creating files"
	os.system("gedit "+name1)
if choice=='3':
	name2=raw_input("Enter name of directory")
	print "Creating Directory"
	os.system("mkdir "+name2)
if choice=='4':
	msg1=raw_input("Enter the item to be searched on google ")
	print "Searching on Google "
	webbrowser.open_new_tab('https://www.google.com/search?q= '+msg1)
if choice=='5':
	print"Logging out of system"
	os.system("exit")
if choice=='6':
	print "Shutting down the system"
	os.system("shutdown ")
if choice=='7':
	print "Checking for Internet connection in your laptop/PC"
	try:
	 urllib2.urlopen("https://www.google.com/",timeout=2)
	 print "Up and Running"
	except urllib2.URLError:
	 print "Network down"
if choice=='8':

	

	



