#Python implementation of Simon's 1/3 Rule
def SimonsRule(x,y):
   h = (x[-1]-x[0])/(len(x)-1) #find the value of h
   tot = y[0]+y[-1]
   # apply Simpson’s 1/3 Rule formula
   for i ,val in enumerate(y[1:-1]) :
      if i%2 ==0:
         tot = tot+4.0*val   #for odd numbers
      else:
         tot = tot+2.0*val   #for even numbers
   #final answer
   S = (h/3)*tot
   print("The answer is:",S)

# Driver code
x = (1,2,3,4,5,6,7,8,9)
y=(3.1,4.4,6.4,6.6,5.9,5.6,5.1,4.9,4.6)
SimonsRule(x,y)

