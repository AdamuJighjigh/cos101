print("welcome to Yusuf and Sons")
p = float(input("Enter your initial amount(₦):"))
r = float(input("nuber of times interest is applied (%):"))
t = float(input("number of times interest applied per time period:"))
n = int(input("number of time periods elapsed:"))
simple_interest = (p*(1+r*t))
compound_interest = (p*(1+r/n)**(n*t))
print("simple interest = "+str(simple_interest))
print("compound interest = "+str(compound_interest))





