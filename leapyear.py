

# Purpose: To showcase the knowledge and use of while loop functions and semantics.
# Pre-Conditions: User will a selected year
# Post-Conditions: Program will determine if the year is a leap. If the user inputs -1 then the program should quit.


def main():
    
     year = int(input("Enter a year (press -1 to quit): "))
     
     
     
     mathyear(year)

     
     
     if answer == False: 
     
          print("this is not a leap year")
     else:
          print("Yes, this is a leap year")

def mathyear(x): 
    
   
    
    
    if x / 100 and x % 400 or not x / 4:   
        
         answer = True 
         #print("this is not a leap year")
         
         return answer
    
    else:
         answer = False
         #print("yes this is a leap year")

         return answer


    


main()