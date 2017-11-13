#! /usr/bin/python3

#Use of the fileinput modeule to replace strings found in a file.

#import modules
import fileinput
import re

#Prompt user
filename = input("Please type the full name of your input file e.g. my_syslog_file.txt:\n")


#Iterate over each line finding the first octet match with regex and replacing it with 123
with fileinput.FileInput('./'+filename, inplace=True, backup='.bak') as file:
	for line in file:
		line = re.sub('(dip\W)([0-9][0-9][0-9]|[0-9][0-9]|[0-9])','dip=123', line.rstrip())
		line = re.sub('(sip\W)([0-9][0-9][0-9]|[0-9][0-9]|[0-9])','sip=123', line.rstrip())
		line = re.sub('(dip\W\W)([0-9][0-9][0-9]|[0-9][0-9]|[0-9])','dip="123', line.rstrip())
#Handle the top-dip messages		
		line = re.sub('(ip1=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip1=123', line.rstrip())
		line = re.sub('(ip2=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip2=123', line.rstrip())
		line = re.sub('(ip3=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip3=123', line.rstrip())
		line = re.sub('(ip4=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip4=123', line.rstrip())
		line = re.sub('(ip5=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip5=123', line.rstrip())
		line = re.sub('(ip6=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip6=123', line.rstrip())
		line = re.sub('(ip7=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip7=123', line.rstrip())
		line = re.sub('(ip8=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip8=123', line.rstrip())
		line = re.sub('(ip9=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip9=123', line.rstrip())
		line = re.sub('(ip10=([0-9][0-9][0-9]|[0-9][0-9]|[0-9]))', 'ip10=123', line.rstrip())
		print(line)



#Confirm opertion is complete
print("\a")
print("Your file is now ready for use, along with a backup of the original, appended .bak.")


