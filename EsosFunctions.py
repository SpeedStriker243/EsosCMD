import time, random, getpass, datetime, webbrowser, os, platform

def SystemException(errlevel = 0, errcode = "0"):
    if errlevel == 1:
        errcode = "R-" + errcode
        print("A problem has occurred in the system software.\nIt may be possible to continue normally.")
    elif errlevel == 2:
        errcode = "S-" + errcode
        print("System error.")
    elif errlevel == 3:
        errcode = "F-" + errcode
        print("System error.")
        print(f"Error code: {errcode}")
        print("Shutting down...")
        exit()
    else:
        errcode = "U-" + errcode
        print("Unspecified system error. You should restart the OS.")
    print(f"Error code: {errcode}")

def StartupMessage():
    if platform.system() == "Darwin":
        print(f"Running EsosCMD on macOS with Darwin kernel version {str(platform.release())} - ", str(time.strftime("%a %d %b %Y")))
    else:
        print(f"Running EsosCMD on {str(platform.system())} {str(platform.release())} - " + str(time.strftime("%a %d %b %Y")))
        if getpass.getuser() == "root":
            print("You're logged in as root, so please be careful.")