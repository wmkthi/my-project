#Python implementation of Trapezoidal Rule
def Trapezoidal(x,y):
   h = (x[-1]-x[0])/(len(x)-1) #find the value of h

   #calculate the n-subinterval trapezoidal approximation
   tot = y[0]
   for val in y[1:-1]:
      tot = tot +(2*val)
   tot = tot + y[-1]
   #final answer  
   T = (h/2)*tot
   print("The answer is:",T)

#Driver code to test above function
x = (1,2,3,4,5,6,7,8,9)
y = (3.1,4.4,6.4,6.6,5.9,5.6,5.1,4.9,4.6)
Trapezoidal(x,y)
