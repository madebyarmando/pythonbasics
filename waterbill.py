
def main():

    
    gallons_used = float(input("Enter thousands of gallons used: "))
    
    res_bus = str(input("Are you a residential or business (r/b): "))
        
        
    geo_them = str(input("Do you have geothermal heating system (y/n) "))
    
        
    if res_bus == "r":
    
        if gallons_used <= 500:
            
            total = gallons_used * .05
        
        elif gallons_used > 500 and gallons_used <= 1000:
            
            total = gallons_used * .09
        
        elif gallons_used > 1000:
            
            total = gallons_used * .11    
    
    
    elif res_bus == "b": 
        if gallons_used <= 1000:
            total = gallons_used * .15
            
        elif gallons_used > 1000 and gallons_used <= 2000:
            total = gallons_used * .19
        
        elif gallons_used > 2000:
            total = gallons_used * .25    
    
    
    if geo_them == "y":
        total = round(total + 10, 2) 
    
    else:    
        total = round(total + 0, 2) 
    
    
    
    print("Your water bill is ", total, sep="$")
    
main()