import os

def run(**args):
	print "[*] In dirlister..."
	files = os.listdir(".")
	return str(files)
