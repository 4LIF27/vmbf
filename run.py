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


if bit == '32bit':
    if os.path.exists("requirements.txt"):
    	
        os.system('pip install -r requirements.txt') 
        os.system("chmod +x v32")
        os.remove("requirements.txt")
        os.system("./v32")
    else:
        
        os.system("./v32")
else:
	exit(" maaf device anada belum support")
        
