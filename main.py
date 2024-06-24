
import random
import os 

def clear_screen():
  # This function depends on your operating system
  # For Windows
  if os.name == 'nt':
    os.system('cls')
  # For Linux/Mac
  else:
    os.system('clear')

def Start():
  clear_screen()  # Clear screen before starting
  print("\n\n----------Kimetsu No Python: Code of the Demon Slayers----------")
  print("------------------Developed by Steven Madali--------------------\n\n\n\n")
  button = input(">>>>Press [K] to Hunt<<<<\n\n>>>>Press [X] to Exit<<<<\n")  # Get user input

  if button == "k" or "K":
    Characterselect()
  else:
    exit()

def Characterselect():
  clear_screen()  # Clear screen before character selection
  
  while True:
    print("------------------Pick Your Demon Slayer--------------------")
    print("[1] Aoi Kanzaki\n The Flame Breathing Prodigy\n -Known 4 Flame Breathing Forms\n")
    print("[2] Hiro Aoiumi\n The Water Breathing Successor\n -Known 7 Water Breathing Forms\n")
    print("[3] Kasumi Arashi\n The Wind Breathing Jackal\n -Known 5 Wind Breathing Forms\n")
    print("[4] Kaito Kaminari\n The Thunder Breathing Genius\n -Known 3 Thunder Breathing Forms\n")
    selectcharacter = int(input())
  
    if selectcharacter == 1:
      Aoi_Kenzaki()
      break
    elif selectcharacter == 2:
      Hiro_Aoiumi()
      break
    elif selectcharacter == 3:
      Kasumi_Arashi()
      break
    elif selectcharacter == 4:
      Kaito_Kaminari()
      break
    else:
      print("Please choose an active Demon Slayer!")
  
# CHARACTERS

def Aoi_Kenzaki():
  clear_screen()  # Clear screen before mission assignment
  print("You Choose Aoi Kanzaki\nThe Flame Breathing Prodigy\n")
  mission_place = ["Mount Yokogawa", "Swordsmith Village", "Entertainment District", "Crimson Light District"]
  
  random_mission = random.choice(mission_place)
  
  print(">You Mission is to go in: \n", random_mission,"!\n")
  if random_mission == "Mount Yokogawa":
    input("Press anything to Enter\n")
    Mount_Yokogawa()
  elif random_mission == "Swordsmith Village":
    input("Press anything to Enter\n")
    Swordsmith_Village()
  elif random_mission == "Entertainment District":
    input("Press anything to Enter\n")
    Entertainment_District()
  elif random_mission == "Crimson Light District":
    input("Press anything to Enter\n")
    Crimson_Light_District()
  
def Hiro_Aoiumi():
  clear_screen()
  print("You Choose Hiro Aoiumi\nThe Water Breathing Prodigy\n")
  # ... (similar structure to Aoi_Kenzaki)

def Kasumi_Arashi():
  clear_screen()
  print("You Choose Kasumi Arashi\nThe Wind Breathing Jackal\n")
  # ... (similar structure to Aoi_Kenzaki)

def Kaito_Kaminari():
  clear_screen()
  print("You Choose Kaito Kaminari\nThe Thunder Breathing Genius\n")
  # ... (similar structure to Aoi_Kenzaki)

def Mount_Yokogawa():
  print("Welcome to Mount Yokogawa!")
def Swordsmith_Village():
  print("Welcome to Swordsmith Village!")
def Entertainment_District():
  print("Welcome to Entertainment District!")
def Crimson_Light_District():
  print("Welcome to Crimson Light District!")

if __name__ == '__main__':
  Start()
