
print("EsosCMD early testing version\nThis version is an early release and is subject to change.")

# Python imports
import time, random, getpass, datetime, webbrowser, os, platform, socket
# EsosCMD imports
import EsosFunctions

EsosFunctions.StartupMessage()

EsosRunning = True
while EsosRunning:

    CurrentWorkingDirectory = os.getcwd()
    Arg1 = ""
    Arg2 = ""

    PromptText = "\033[1;32m" + getpass.getuser() + "@" + socket.gethostname() + "\033[1;37m:\033[1;34m" + CurrentWorkingDirectory + "$ "

    CmdLine = input(PromptText + "\033[0;37m")

    Command = CmdLine.split(" ")[0]
    try:
        Arg1 = CmdLine.split(" ")[1]
        Arg2 = CmdLine.split(" ")[2]
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
            print(CurrentWorkingDirectory)
    else:
        EsosFunctions.ProgramLaunch(Command)