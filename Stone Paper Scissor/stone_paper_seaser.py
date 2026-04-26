import random
def get_choise():
    option = ["paper" , "stone" ,"seasore"]
    player_choise = input("enter your choise : ")
    computer_choise = random.choice(option)
    choices = {"player" : player_choise ,"computer" : computer_choise}
    return choices
    
def check_win(player , computer):
    if(player == computer):
      return "tie"
    elif(player == "stone" and computer == "paper"):
      return "computer"
    elif(player == "stone" and computer == "seasore"):
      return "player"
    elif(player == "paper" and computer == "stone"):
      return "player"
    elif(player == "paper" and computer == "seasore"):
      return "computer"
    elif(player == "seasore" and computer == "paper"):
      return "player"
    elif(player == "seasore" and computer == "stone"):
      return "computer" 
    else :
        print("invalid choise")
        

choise = get_choise()
win = check_win(choise["player"] ,choise["computer"]  )
print(win)