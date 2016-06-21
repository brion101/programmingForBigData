# Define classes

import math 
import os 

################################################################################################################################
#
# Class files  
#
################################################################################################################################

class GeneralUtil(object):
    # This class contains general purpose fuctions 
  
    def __init__(self):
	    self.__count = 0	

    def Menulist(self,menulist):
		# This generic menu function does
		# 1. accepts a list as input, this list is used to build the menu
		# 2. prompts a uses to make a selection 
		# 3. returns the selection number ( this is the position on the input list ) 
		# 
        while True:
			os.system('cls')
			print
			print "Enter Number to Select function "
			print 
			for index,(menuitem,data) in enumerate(menulist):
				print "     %d to %s " % (index + 1,menuitem)
			print
			print "     Q to Quit"
			print
			selection = raw_input("Please enter options : ")
			if selection.lower() == 'q':
				return selection.lower()
			try:
				selection = int(selection) - 1
				result = calcFuncList[selection][0]
				return selection 
			except:
				raw_input("Invalid option selected, press return")

    def getParameterValues(self,ValueName,NumOfParameters):
		# This generic function gets X number of values and returns them in a list  
		# 1. accepts name of value and number of parameters required
		# 2. prompts user to enter parameter values (for number required) 
		# 3. returns a list of parameter values 
		# 
		parameterlist = list()
		count = 1
		os.system('cls')
		while count <= NumOfParameters:  
			selection = raw_input("Please enter value %d of %d for %s function : " % (count,NumOfParameters,ValueName))
			try:
				selection = float(selection)
			except:
				print "Invalid value entered"
			else:
				parameterlist.append(selection)
				count = count + 1
		return parameterlist		
		

class Calculator(object):
    # This class contains Calculator functions and a general purpose function to call a calculator function

    def __init__(self):
		# create a tuple list of all calculator functions and the number of values each function requires, this can be used by calling applications
        self.__CalcFunctionlist = [('add', 2), ('subtract', 2), ( 'multiply', 2), ('divide', 2) ,('add_3_Numbers', 3), ('factorial', 1)] 		
        self.__CalcFunctionlist.extend ([('sqrRoot', 1), ('square', 1), ('power', 2), ('floor', 1)]) 		
		
    def getcalclist(self):
        return self.__CalcFunctionlist
	
    def callCalcFunc(self,funcName,FuncParameters):
		# This function calls one of the calculator functions depending on request, any parameters for the called function are in the FuncParameters list 
		# 
		if funcName == "add":
			result =  Calculator.add1(self,FuncParameters[0],FuncParameters[1]) 
		elif funcName == "subtract":
			result =  Calculator.subtract1(self,FuncParameters[0],FuncParameters[1])
		elif funcName == "add_3_Numbers":
			result =  Calculator.add3nums(self,FuncParameters[0],FuncParameters[1],FuncParameters[2])
		elif funcName == "multiply":
			result =  Calculator.multiply1(self,FuncParameters[0],FuncParameters[1])
		elif funcName == "divide":
			result =  Calculator.divide1(self,FuncParameters[0],FuncParameters[1])
		elif funcName == "factorial":
			result =  Calculator.factorial1(self,FuncParameters[0])
		elif funcName == "sqrRoot":
			result =  Calculator.sqrroot1(self,FuncParameters[0])
		elif funcName == "square":
			result =  Calculator.square1(self,FuncParameters[0])
		elif funcName == "power":
			result =  Calculator.power1(self,FuncParameters[0],FuncParameters[1])
		elif funcName == "floor":
			result =  Calculator.floor1(self,FuncParameters[0])
		else:
			result = "error"
		return result 
	
	# The calculator functions are below
	
    def add1(self,n1,n2):
		try:
			return n1 + n2
		except:
			return "error"

    def add3nums(self,n1,n2,n3):
		try:
			return n1 + n2 + n3
		except:
			return "error"
		
    def subtract1(self,n1,n2):
		try:
			return n1 - n2 
		except:
			return "error"
		
    def multiply1(self,n1,n2):
		try:
			return n1 * n2  
		except:
			return "error"
		
    def divide1(self,n1,n2):
		try:
			return n1 / n2
		except:
			return "error"

    def factorial1(self,n1):
		try:
			if n1 < 1:    
				return 1
			else:
				return n1 * Calculator.factorial1(self,n1 - 1 )
		except:
			return "error"
	
    def sqrroot1(self,n1):
		try:
			return math.sqrt(n1)
		except:
			return "error"

    def square1(self,n1):
		try:
			return n1**2
		except:
			return "error"
		
    def power1(self,n1,n2):
		try:
			return math.pow(n1,n2)
		except:
			return "error"
	
    def floor1(self,n1):
		try:
			return math.floor(n1)
		except:
			return "error"
	
################################################################################################################################
#
# Calculator main application code 
#
################################################################################################################################

if __name__ == '__main__':

	#  Create objects for generalutil and calculator classes
	general_util = GeneralUtil()
	calc = Calculator()
	
	#  Get list of available calculator functions, this will be used to build a menulist 
	calcFuncList = calc.getcalclist()

	while True:
	#   This is the main calculator process, it does the following steps 
	#
	#   1. Call a generic menu function using a list of fuctions names from calculator class, this returns a selection from the list
	#   2. Call a generic function to get input parameters for the choosen calculator function, this returns a list of parameters
	#   3. Call a general Calculator function which then calls the specific function choosen from the menu, also pass parameter list
	#   4. Print results from calculation 
	#
	#   Repeat above steps until quit is choosen  (q)

	
	#   Call general menu function, provide  calculator functions list as input
		menuoption = general_util.Menulist(calcFuncList)
		if menuoption == "q":
			break

	# 	when calc function selected from menu list, get parameters required for the function, then call calculator function to process request
		parameterlist = general_util.getParameterValues( calcFuncList[menuoption][0] , calcFuncList[menuoption][1] )
		calcResult = calc.callCalcFunc( calcFuncList[menuoption][0] , parameterlist )

		print ""
		print " Result for %s  is : %s "  % (calcFuncList[menuoption][0],calcResult)
		print ""
		raw_input("press return")
	
