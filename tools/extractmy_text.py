# importing the library
from bs4 import BeautifulSoup

with open("index.html","r") as f:
	t=f.read()
	# Initializing variable
	gfg = BeautifulSoup(t)
	 
	# Calculating result
	res = gfg.get_text()
	 
	# Printing the result
	print(res)
