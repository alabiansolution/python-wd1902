
try:
	40/10
	f = open("demo")
except ZeroDivisionError as e:
	print("Number can not be divisible by zero ({})".format(e))
except FileNotFoundError as a:
	print("File failed to open ({})".format(a))