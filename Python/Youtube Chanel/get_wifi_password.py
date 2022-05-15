#import subprocess so we can use system commands
import profile
import subprocess

#import the re module so that we can make use of regular expressions
import re

from click import command

# the script is a parent process and creates a child process which runs the system command,
# and will only continue once the child process has completed
# to save the contents that gets sent to the standard output stream(the terminal)
# we have to specify that we want to capture the output,
# so we specify the second argument as capture_output = true.
# This information gets stored in the stdout attibutte.
# The information is stored in bytes and we need to decode it to Unicode
# befere we use it as a String in Python.
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

# We imported the re module so that we can make use of regular expressions.
# We want to find all the Wifi names which is always listed after "All User Profile"
# In the regular expression we create a group of all characters until the return
profile_names = (re.findall("All User Profile    : (.*)\r", command_output))


# we create an empty list outside of the loop where dictionaries with all the wifi
# username and passwords will be saved.
wifi_list = list()

# if we didn't find profile names we didn't have any wifi connections,
# so we only run the part to check for the details of the wifi and
# whether we can get their passwords in this part.
if len(profile_names) != 0:
    for name in profile_names:
        # Every wifi connection will need its own dictionary which will be appended
        wifi_profile = dict()
        # We now run a more specific command to see the information about the specific wifi connection
        # and if the Security key is not absent we ca possibly get the password.
        profile_info = subprocess.run(["netsh", "waln", "show", "profile", name], capture_output= True).stdout.decode()
        if re.search("Secutiry key        : Absent", profile_info):
            continue
        else:
            # Assign the ssid of the wifi profile to the dictionary
            wifi_profile["ssid"] = name
            # These cases aren't absent and we should tun them "key=clear" command part to get the
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            # Again run the regular expressions to capture the group after the : which is the password
            password = re.search("Key Content       : (.*)\r", profile_info_pass)
            # Check if we found a password in the regular expression. All wifi connections will not have passwords.
            if password == None:
                wifi_profile["password"] = None
            else:
                # We assign the grouping (Where the password is contained) we are interested to the
                wifi_profile["password"] = password[1]
            # We append the wifi information to the wifi_list
            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])