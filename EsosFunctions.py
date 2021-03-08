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
			
def EsosScript(filename):
	try:
		ScriptFile = open(filename + ".ess")
		ScriptLine = ""
		LineCount = 0
			
		print(f"Reading {ScriptFile.name}...")
		while ScriptLine != "end":
			LineCount += 1
			ScriptLine = ScriptFile.readline()
			
			if LineCount == 1 and ScriptLine[:7] != "escript":
				print(f"Syntax error. An EsosScript file must start with version definition.")
				break
			if ScriptLine[:3] == "///":
				pass
			elif ScriptLine[:3] == "log":
				print(ScriptLine[4:])
			elif ScriptLine[:7] == "escript":
				print(f"Using EsosScript version {ScriptLine[8:]}")
			elif ScriptLine == "":
				pass
			elif ScriptLine[:3] == "end":
				break
			else:
				print(f"Syntax error. The line '{ScriptLine}' was not understood.")
				break
				
		ScriptFile.close	
	except FileNotFoundError:
		print(f"The script file {Arg1}.ess was not found.")
