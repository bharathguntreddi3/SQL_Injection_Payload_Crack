# subprocess Allows you to run the terminal commands using python rather than using terminal
# A python terminal interface to show your pc connected wifi's with thier passwords using netsh wlan show profiles 

import subprocess

# subprocess module allows you to spawn processes 
# connect to their input/output/error pipes
# and obtain their return codes.

def wifi_users(): 
	show_users = subprocess.check_output(['NETSH','WLAN','SHOW','PROFILES'])    #cmd wifi users list
	# print(show_users)
 
	deco = show_users.decode("utf-8")  # decoding the characters
	deco = deco.split("\n")
	user_names = []

	for i in deco:
		if ("All User Profile     : " in i):
			# print(i)
			name = i.split(":")[1]
			user_names.append(name[1:-1])

	return user_names

print("\n user_name    -    Password \n")

for name in wifi_users():
	show_passwords = subprocess.check_output(['NETSH','WLAN','SHOW','PROFILE',name,'KEY=CLEAR'])      # cmd wifi users with password

	deco = show_passwords.decode("utf-8")  # decoding the characters
	deco = deco.split("\n")
 
	for i in deco:
		if ("Key Content" in i):
			passwords = i.split(":")[1]
			# print(passwords)
			
	print(name ,"  -  " , passwords, "\n")

print("Successfully Retrived All wifi usernames and the Passwords ! \n\n")
 