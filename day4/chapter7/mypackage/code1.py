states = {
    "Imo" : "Owerri",
    "Lagos" : "Ikeja",
    "Oyo" : "Ibadan",
    "Rivers" : "Port Harcourt",
    "Taraba" : "Yalingo",
    "Bornu": "Maidugri"
}

def my_avg(total_avg):
	'''
	 This function takes a list of numbers as
	 an argument and returns the average
	 of that list
	'''
	sum = 0
	for x in total_avg:
		sum += x
	return sum/len(total_avg)

def multiplication(multiply_by, start=1, stop=12):
    '''
    This function takes three argument
    the first one is the multiplication number
    and it is required. The second is the start value
    and is optional while the third on is stop value
    and it is also optional
    '''
    while start <= stop:
        print(multiply_by, " X ", start, " = ", multiply_by * start)
        start += 1
