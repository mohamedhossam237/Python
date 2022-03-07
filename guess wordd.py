import random as rdm  
  
# Here the user will be asked to enter their name first  
name1 = input("What is your NAME ? ")  
  
print("Best of Luck! ", name1)  
   
words1 = ['Donkey', 'Aeroplane', 'America', 'Program',  
         'Python', 'language', 'Cricket', 'Football',  
         'Hockey', 'Spaceship', 'bus', 'flight']  
   
word1 = rdm.choice(words1)  
    
print ("Please guess the characters: ")  
   
guesses1 = ''  
   
turns1 = 10  
   
while turns1 > 0:  
       
     
    failed1 = 0  
       
    for char in word1:  
           
           
        if char in guesses1:  
            print(char)  
               
        else:  
            print("_")  
               
             
            failed1 += 1  
               
   
    if failed1 == 0:  
         
        print("User Win")  
           
        print("The correct word is: ", word1)  
        break  
       
    guess1 = input("Guess another character:")  
       
    guesses1 += guess1  
       
    if guess1 not in word1:  
           
        turns1 -= 1  
          
        print("Wrong Guess")  
           
        print("You have ", + turns1, 'more guesses ')  
           
        if turns1 == 0:  
            print("User Loose")  



        
        
