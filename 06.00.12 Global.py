def myFunction():
	a = "A is a local variable"
	return a
	
b = myFunction()
print(b) #Changed from print(a) to print(b) otherwise "NameError: name 'a' is not defined"