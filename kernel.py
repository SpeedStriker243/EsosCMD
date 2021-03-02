# Python imports
import time, random, getpass, datetime, webbrowser, os, platform, socket
# EsosCMD imports
import EsosFunctions as esosfunc

esosfunc.startup()

EsosRunning = True
while EsosRunning:
    CurrentWorkingDirectory = os.getcwd()

    PromptText = "\033[1;32;40m" + getpass.getuser() + "@" + socket.gethostname() + "\033[1;37;40m:\033[1;34;40m" + CurrentWorkingDirectory + "$ "

    CmdLine = input(PromptText)
    CmdCheck = CmdLine.split('$')[0]

    print(CmdCheck)