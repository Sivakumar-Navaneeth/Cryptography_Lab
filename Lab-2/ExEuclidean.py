def gcdExtended(a, b): 
	# Base Case 
	if a == 0 : 
		return b,0,1
			
	gcd,x1,y1 = gcdExtended(b%a, a) 
	# print(gcd,x1,y1)
	x = y1 - (b//a) * x1 
	y = x1 
	# print(x,y)
	
	return gcd,x,y 
	
a, b = int(input("Enter 'a' value: ")),int(input("Enter 'b' value: "))
g, x, y = gcdExtended(a, b) 
print("The GCD({},{}) = {}".format(a,b,g)) 
