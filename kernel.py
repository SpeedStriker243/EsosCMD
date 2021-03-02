
print("EsosCMD early testing version\nThis version is an early release and is subject to change.")

# Python imports
import time, random, getpass, datetime, webbrowser, os, platform, socket
# EsosCMD imports
import EsosFunctions

EsosFunctions.StartupMessage()

EsosRunning = True
while EsosRunning:

    CurrentWorkingDirectory = os.getcwd()
    UserName = getpass.getuser()
    ComputerName = socket.gethostname()
    OSName = platform.system()
    Arg1 = ""
    Arg2 = ""
    Arg3 = ""
    Arg4 = ""

    if UserName == "root":
        CommandSeparator = "# "
    else:
        CommandSeparator = "$ "

    PromptText = "\033[1;32m" + UserName + "@" + ComputerName + "\033[1;37m:\033[1;34m" + CurrentWorkingDirectory + "\033[m" + CommandSeparator

    CmdLine = input(PromptText)

    Command = CmdLine.split(" ")[0]
    try:
        Arg1 = CmdLine.split(" ")[1]
        Arg2 = CmdLine.split(" ")[2]
        Arg3 = CmdLine.split(" ")[3]
        Arg4 = CmdLine.split(" ")[4]
    except IndexError:
        pass

    if Command == "cd":
        try:
            if Arg1 != "":
                try:
                    os.chdir(Arg1)
                except FileNotFoundError:
                    print(f"Couldn't find the folder or path " + Arg1 + ".")
            else:
                print(CurrentWorkingDirectory)
        except:
            print(f"Your current directory is {CurrentWorkingDirectory}.")

    elif Command == "whoami":
        print(f"You are {UserName}.")

    elif Command == "exec":
        try:
            if Arg1 == "":
                print("The command was entered incorrectly.")
                print("exec can be used to run native commands, the same way you would in your terminal.")
                print("Usage: exec <command name>")
            else:
                os.system(Arg1 + " " + Arg2 + " " + Arg3 + " " + Arg4)
        except IndexError:
            pass

    elif Command == "exit":
        print("Thanks for trying out EsosCMD!")
        if OSName == "Windows":
            print("Exiting to command prompt.")
        else:
            print("Exiting to terminal.")
        EsosRunning = False

    else:
        EsosFunctions.EsosCommand(Command)