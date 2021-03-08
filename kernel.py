print("EsosCMD early testing version")
print("This version is an early release and is subject to change.")

# Python imports
import time, random, getpass, datetime, webbrowser, os, platform, socket
# EsosCMD imports
import EsosFunctions

EsosFunctions.StartupMessage()


OSName = platform.system()
if OSName == "Windows":
	Colour = False
else:
	Colour = True

EsosRunning = True
while EsosRunning:

	CurrentWorkingDirectory = os.getcwd()
	UserName = getpass.getuser()
	ComputerName = socket.gethostname()
	OSName = platform.system()
	Arg1, Arg2, Arg3, Arg4, Arg5, Arg6, Arg7, Arg8, Arg9 = "", "", "", "", "", "", "", "", ""

	if UserName == "root":
		CommandSeparator = "# "
	else:
		CommandSeparator = "$ "

	if Colour:
		PromptText = "\033[1;32m" + UserName + "@" + ComputerName + "\033[1;37m:\033[1;34m" + CurrentWorkingDirectory + "\033[m" + CommandSeparator
	else:
		PromptText = UserName + "@" + ComputerName + CurrentWorkingDirectory + CommandSeparator

	try:
		CmdLine = input(PromptText)
	except KeyboardInterrupt:
		CmdLine = ""
		print("\nThanks for trying out EsosCMD!")
		if OSName == "Windows":
			print("Exiting to command prompt.")
		else:
			print("Exiting to terminal.")
		break

	Command = CmdLine.split(" ")[0]
	try:
		Arg1 = CmdLine.split(" ")[1]
		Arg2 = CmdLine.split(" ")[2]
		Arg3 = CmdLine.split(" ")[3]
		Arg4 = CmdLine.split(" ")[4]
		Arg5 = CmdLine.split(" ")[5]
		Arg6 = CmdLine.split(" ")[6]
		Arg7 = CmdLine.split(" ")[7]
		Arg8 = CmdLine.split(" ")[8]
		Arg9 = CmdLine.split(" ")[9]
	except IndexError:
		pass

	if Command == "cd":
		try:
			if Arg1 != "":
				try:
					os.chdir(Arg1)
				except FileNotFoundError:
					print(f"Couldn't find the folder or path {Arg1}.")
			else:
				print(f"Your current directory is {CurrentWorkingDirectory}.")
				print(f"To change it, type a path after you type cd.")
		except:
			print(f"Your current directory is {CurrentWorkingDirectory}.")
			print(f"To change it, type a path after you type cd.")

	elif Command == "whoami":
		print(f"You are {UserName}.")

	elif Command == "exec":
		try:
			if Arg1 == "":
				print("exec can be used to run native commands, the same way you would in your terminal.")
				print("Usage: exec <command name>")
			else:
				os.system(Arg1 + " " + Arg2 + " " + Arg3 + " " + Arg4)
		except IndexError:
			pass

	elif Command == "cmdlist" or Command == "help":
		print("cd <directory> - Change your current working directory.")
		print("whoami - Print your username.")
		print("exec <command> - Run a native command.")
		print("cmdlist - Show this messsage.")
		print("help - See above.")
		print("colo(u)r - Toggle prompt colour on or off.")
		print("script - Run an EsosScript file.")
	
	elif Command == "color" or Command == "colour":
		if Colour:
			Colour = False
			print("Prompt colours have been disabled.")
		else:
			Colour = True
			print("Prompt colours have been enabled.")
			if OSName == "Windows":
				print("You're on Windows, though, so you'll probably see a bunch of jumbled text.")
				
	elif Command == "script":
		if Arg1 == "":
			print("script can be used to run EsosScript files.")
			print("Usage: script <file name>")
		else:
			EsosFunctions.EsosScript(Arg1)

	elif Command == "exit":
		print("Thanks for trying out EsosCMD!")
		if OSName == "Windows":
			print("Exiting to command prompt.")
		else:
			print("Exiting to terminal.")
		EsosRunning = False

	else:
		print(f"'{Command}' doesn't match any command.")
