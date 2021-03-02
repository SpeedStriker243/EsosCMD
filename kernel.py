import time, random, getpass, datetime, webbrowser, os, platform

osname = "EsosCMD"
print(f"Now loading {osname}…")
time.sleep(5)
if platform.system == "Darwin":
    print(f"Running {osname} on macOS with Darwin kernel version {str(platform.release())} - ", str(time.strftime("%a %d %b %Y")))
else:
    print(f"Running {osname} on {str(platform.system())} {str(platform.release())} - ", str(time.strftime("%a %d %b %Y")))
