
# Purpose: To use basic conditionals If/Else


def main ():
   # set gold flag to False
   gld = False
   # set lived flag to False
   lived = False
   # display first prompt  Door #1/#2
   print("You enter a room with 2 exits. Do you take Door #1 or Door #2?")
   
   first_choice = int(input('> ' ))
   
   # get user's first choice
   
   if first_choice == 1:
   # if user chooses 1
   #     display lion prompt Run away/Wrestle      
      print("You see a lion!\n What do you do?\n 1. Run Away\n 2. Wrestle the lion")
      lion_choice = int(input('> '))
   #     if chooses Run away
   #         lived flag is set to True
   #             output You get away!      
      if lion_choice == 1: 
         print("You get away!")
         lived = True 
      
      else:  
         print("You get eaten")
         # output a blank line

      print()
      
   else: 
      print("You see a pot of gold. Do you\n 1. Try to carry it away\n 2. Take some gold")    
      pot_gold = int(input('> ' ))
      if pot_gold == 1: 
         print("It's too heavy and the strain kills you!")
      else: 
         print("You got away with 500 gold coins!")
         gld = True
   # output a blank line
   
   print()
   # output Game Over!
   print('Game over!') 
   # if lived flag has value True
   if lived == True:
      #   output Congratulations! you got through the game alive!
      print("Congratulations! you got through the game alive!")
      
      if gld == True:
         print("You got away with 500 gold coins!")
      else:
         print("You at least got away with your life, no gold though")
      
   else: 
      print("Too bad! you didn't make it")
   
main()

