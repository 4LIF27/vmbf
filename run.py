#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='up':
    	os.system("git pull");os.system('rm -rf run')
except:
    pass
	
bit = platform.architecture()[0]
if bit == '64bit':
	exit(" maaf untuk sc ini belum support 64 bit ")
    if not os.path.isfile('v64'):
        os.system('pip install -r requirements.txt') 
        os.system("chmod +x v64")
        os.system("./run")
    else:
        os.system("./run")

elif bit == '32bit':
    if not os.path.isfile('v32'):
        os.system('pip install -r requirements.txt') 
        os.system("chmod +x v32")
        os.system("./run")
    else:
        os.system("./v32")