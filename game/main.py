import random





def choose_options():
  options=("piedra","papel","tijera")
  option_player1=(input("Ingrese la palabra 'piedra','papel','tijera' : "))
  option_player1=option_player1.lower()

 
  

  if not option_player1 in options:
    print("la opcion no es valida")
    #continue
    return None,None
  
  computer=random.choice(options)

  print("player option:",option_player1)
  print("Computer Options:", computer)
  return option_player1,computer

def check_rules(option_player1,computer,user_wins,computer_wins):
  if option_player1==computer:
    print("Es un empate")

  elif option_player1=="piedra":
    if computer=="tijera":
      print("piedra gana a tijera")
      print("player 1 gano")
      user_wins+=1
    else:
      print("papel gana a piedra")
      print("COMPUTER gano")
      computer_wins +=1

  elif option_player1=="papel":
    if computer=="piedra":
      print("papel gana a prieda")
      print("player 1 gano")
      user_wins+=1
    else:
      print("tijera gana a papel")
      print("COMPUTER gano")
      computer_wins +=1

  elif option_player1=="tijera":
    if computer=="papel":
      print("tijera gana a papel")
      print("player 1 gano")
      user_wins+=1
    else:
      print("piedra gana a tijera")
      print("COMPUTER gano")
      computer_wins +=1
  return user_wins,computer_wins

def run_game():
  computer_wins=0
  user_wins=0
  rounds=1

 

  while  True:

    print("*"*20)
    print("Round",rounds)
    print("*"*20)

    print("computer wins",computer_wins)
    print("palyer wins",user_wins)
    rounds+=1

    option_player1,computer=choose_options()
    user_wins,computer_wins= check_rules(option_player1,computer,user_wins,computer_wins)


    if computer_wins==2:
      print("El ganador es la computadora")
      break
    if user_wins==2:
      print("El ganador es el player")
      break

run_game()

