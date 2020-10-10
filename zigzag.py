import time,sys
indent = 0 #how many spaces to indent
indent_increasing = True #whether the indentation is increasing or not.
try:
	while True:
		print(' '*indent,end=' ')
		print("Hello_Friend")
		time.sleep(0.1) #pause for 1/10 of a  second.
		if indent_increasing:
			indent= indent +1
			if indent == 20:
				indent_increasing = False
		else:
			indent= indent-1
			
		if indent == 0:
			indent_increasing = True
			
except Keyboardinterrupt:
			sys.exit()
			
			
		
