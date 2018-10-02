from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess


# Create your views here.
def existFolder ():
	if os.path.exists('D:\WORK\FILENEW\myNgBuilder\src'):
		print("FOLDER EXISTSSSS")
		return True
	else:
		print("EXIST FAILED")
		return False

def copyFolder ():
	copyCmd = subprocess.Popen('xcopy D:\WORK\FILENEW\XCOPY D:\WORK\FILENEW\myNgBuilder /s /e /c /h /k /y /i',
	                           shell=True)
	copyCmd.communicate()
	copyReturnCode = copyCmd.returncode
	if copyReturnCode == 0:
		print('Succces: Successfully copy Src Folder ')
		# newComp = subprocess.Popen('cd D:/WORK/FILENEW/myNgBuilder & ng g component mycomponet',shell=True)
		# newComp.communicate()
		# newCompReturnCode = newComp.returncode
		# if newCompReturnCode == 0:
		# 	print("Successfully created component")
		# else:
		# 	print("Failed creating component")
		addPwa = subprocess.Popen('cd D:/WORK/FILENEW/myNgBuilder & ng add @angular\/PWA', shell=True)
		addPwa.communicate()
		newCompReturnCode = addPwa.returncode
		if newCompReturnCode == 0:
			print("Successfully created PWA")
		else:
			print("Failed creating PWA")
	else:
		print("Failed Copying SRC Folder")


def suprocess (request):
	if existFolder():
		pObj = subprocess.Popen('rmdir /S /Q  D:\WORK\FILENEW\myNgBuilder\src',shell=True,stdout=subprocess.PIPE,
		                        stderr=subprocess.PIPE)
		rTup = pObj.communicate()
		rCod = pObj.returncode
		if rCod == 0:
			print('Succces: Successfully cleared Src Folder')
			copyFolder()
		else:
			print('Fail: Unable to Clean Windows Src Folder')
	else:
		print('exist folder check failed')
		copyFolder()
	print('Angular project started.....')
	return HttpResponse("Hello world")


def index (request):
	htmlStarttag = "<!doctype html>\n<html>"
	headtag = """
        <head>
            <meta name="viewport" content="width=device-width, user-scalable=no" />
            <link rel="manifest" href="manifest.json" />
        </head>
    
    """
	bodytag = """
        <body>
            <h1>Helloe world</h1>
        </body>
    """
	htmlEndtag = "</html>"
	filename = 'www/index.html'
	os.makedirs(os.path.dirname(filename),exist_ok=True)
	with open(filename,"w+") as f:
		f.write("%s \n %s \n %s \n %s" % (htmlStarttag,headtag,bodytag,htmlEndtag))
		f.close()
	
	# f= open("index.html","w+")
	import subprocess
	
	completed = subprocess.run(['ls','-1'])
	print('returncode:',completed.returncode)
	return HttpResponse("Hello world")
