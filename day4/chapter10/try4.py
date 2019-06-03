
try:
	40/10
	f = open("demo")
except Exception as e:
	print("Number can not be divisible by zero ({})".format(e))
except Exception as a:
	print("File failed to open ({})".format(a))