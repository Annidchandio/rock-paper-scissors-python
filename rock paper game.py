import random
p_s = 0
c_s = 0
t_s = 0
name =input ("Enter your name : ")
ask = input (f"Do you want to Logni =====YES===OR=====NO==?")
if ask  == "no":
    print ("LOGIN SKIPPED ")
else :
    print ("=====LOGIN====")
    input ("Enter user first name :")
    print ("=====PASSWORD======")
    input ("Enter password to play : ")
    print("Login successful!")
print ("Welcome ",name )
print ("let's play ")
print ("======Rock, Paper, Scissors=======")
input ("Press ======__Enter__======")
print ("player====VS====Pc :")
for i in range (1,7):
    print (f"\n=======--ROUND-- {i}======")
    user=input ("Choose :====rock, paper, or scissors====: ")
    com = random.choice(["rock", "paper", "scissors"])
    print(f"\nComputer chose is : {com}")

    if user == com :
        print("It's a tie!")
        t_s +=1
    elif (user == "rock" and com == "scissors") or \
         (user == "paper" and com == "rock") or \
         (user == "scissors" and com == "paper"):
        print("You win this round!")
        p_s +=1
    elif (user == "scissors" and com == "rock") or \
         (user == "rock" and  com == "paper") or \
         (user == "paper" and com == "scissors"):
        print("You lose this round!")
        c_s +=1
    else :
        print("Invalid input! No points.")
        
        
print("\n======= GAME OVER =======")
w=print(f"{name}'s Score: {p_s}")

e=print(f"Computer's Score: {c_s}")
print(f"Ties: {t_s}")
if p_s >=c_s:
    print ("==========YOU WON THIS MATCH===========")
elif c_s >=p_s :
    print ("==========YOU LOSE THIS MATCH===========")
else:
    print ("===========IT'S A DRAW============")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
 