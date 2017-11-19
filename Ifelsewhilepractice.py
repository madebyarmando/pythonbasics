
# Purpose: Practice Structure Programming, Conditionals, Boolean Flags, and 
# creating new functions. 


from random import *

def main():
     
     
    x = 20
    
    y = 18
    
    z = 12
    
    user = int(input("number? "))
    
    if user > y :
        print("Bigger than 18")
        print(int("20"))
        
    elif user < x:
        print("Less than 21")
    elif user == z:
        print("equal to 12")

    five = False
    
    for i in range(1,6):
        
        x = randrange(1,10)
        
      
        if x == 5:
            five = True
                 
     # this doesn't keep the code running because you have definite values from 1 to 6       
    
    
    #x = True
    
    #if x == 5:
            
     #   x = True
                  
      #  print("Done")    
    
    #while not False:
        
     #   x = randrange(1,10)
        
      #  print(x)
    
    # Can you use bools as sentinel logic??? 
   
    
    
    five = False
         
    
    while not five:
        
        x = randint(1, 7)
        
        if x == 5:
        
            five = True           
        
            print("You got a 5 Stop") 
        
        else:
            print(x)
    
    # this code only stops after 5 is detected. But we want a specific print range.  
     
    
    
    
    
    done = False
    
    total = 0
    
    name = str(input("Enter Student Name: (Press N or n to stop) "))
    
    if name == "N":
    
        done = True          
    
    while done != True:
        
        
        total += len(name)
        
        name = str(input("Enter Student Name: (Press N or n to stop) "))
        
        if name == "N":
        
            done = True        
        
    
    print("There were", total, "characters")
    # how to keep the code going???
    # calculate how many student names were entered?
    
    
    triangle()
    

def triangle():
    
    print("*")
    print("**")
    print("***")

    
    






    
        
main()        






