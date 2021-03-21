N=int(input("Enter the Number")) #taking input

fact=1 #declaring and initializing a temperory variable to stor value of fact

for i in range(1,N+1): #using loop to iterate

    fact=fact*i #statement for getting factorial

print("The factorial of",N,"is",fact) #print