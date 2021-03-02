# Python imports
import time, random, getpass, datetime, webbrowser, os, platform, socket
# EsosCMD imports
import EsosInbuilt as esosfunc

esosfunc.startup()

EsosRunning = True
while EsosRunning:
    CurrentWorkingDirectory = os.getcwd()

    PromptText = getpass.getuser() + "@" + socket.gethostname() + "|" + CurrentWorkingDirectory + "$ "

    CmdLine = input(PromptText)
    CmdCheck = CmdLine.split('$')[0]

    print(CmdCheck)