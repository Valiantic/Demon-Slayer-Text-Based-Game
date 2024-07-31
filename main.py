
import random
import os 
import speech_recognition as sr #voice recognition para makilala yung boses mo 
import pyttsx3 #text to speech / nagcoconvert ng texto sa salita

# SPEECH GENERATION
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 145)
    engine.say(text)
    engine.runAndWait()

def clear_screen():
  
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def Start():
  clear_screen()  # Clear screen before starting
  print("\n\n----------Kimetsu No Python: Code of the Demon Slayers----------")
  print("------------------Developed by Steven Madali--------------------\n\n\n\n")
  speak("Welcome to Kimetsu no Python: Code of the Demon slayers, A Text based game developed by steven madali. press k to hunt demons")
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
    print("[2] Hiro Aoiumi\n The Water Breathing Successor\n -Known 4 Water Breathing Forms\n")
    print("[3] Kasumi Arashi\n The Wind Breathing Jackal\n -Known 3 Wind Breathing Forms\n")
    print("[4] Kaito Kaminari\n The Thunder Breathing Genius\n -Known 2 Thunder Breathing Forms\n")
    speak("Choose your demon slayer")
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
  print(" Aoi Kanzaki, orphaned by a demon attack, seeks vengeance as a Demon Slayer Corps caretaker. Though a skilled fighter, \n self-doubt led her to support injured Slayers at the Butterfly Mansion. Her kindness and hidden strength\n make her a valuable asset.")
  from Aoi_character import Mission
  Mission()
 
def Hiro_Aoiumi():
  clear_screen()
  print("You Choose Hiro Aoiumi\nThe Water Breathing Prodigy\n")
  print(" Hiro Aoiumi, a solitary figure cloaked in an indigo haori, bore the weight of a heavy past. Orphaned\n by a demon attack that ravaged his village, he wandered the land, a relentless hunter.\n His nichirin, Ikazuchi, sang a mournful song as he danced with demons, each strike fueled by a silent vow of\n vengeance. Legends whispered of a storm swordsman, a harbinger of destruction for demons, and fear followed Hiro wherever he went.")
  from Hiro_character import Mission
  Mission()

def Kasumi_Arashi():
  clear_screen()
  print("You Choose Kasumi Arashi\nThe Wind Breathing Jackal\n")
  print(" A vibrant young woman with eyes like a stormy sky, was a whirlwind of steel and laughter. Her twin katanas, Ame (Rain) and Yuki (Snow),\n were as unpredictable as the mountain storms she called home. Kasumi's breath technique wove illusions that dazzled and disoriented,\n leaving opponents bewildered as her blades found their mark. Renowned for her flamboyant fighting style and\n relentless optimism, Kasumi left a trail of vanquished demons and bewildered onlookers in her wake.")
  from Kasumi_character import Mission
  Mission()

def Kaito_Kaminari():
  clear_screen()
  print("You Choose Kaito Kaminari\nThe Thunder Breathing Genius\n")
  print(" Kaito Kaminari, a prodigy with an unnervingly calm demeanor, possessed an intellect that rivaled the sharpest blade. \n Despite his youth, he\n had risen through the ranks of the Demon Slayers with meteoric speed. His\n wakizashi, Raijin (Thunder God) and Fuujin (Wind God),\n moved with a deadly precision, a testament to his rigorous training and strategic mind. Kaito's breath technique\n granted him heightened reflexes and perception, allowing him to anticipate his opponents' moves\n and dismantle them with surgical efficiency. Though his methods were unorthodox, his success was undeniable, \n making him a valuable asset to any mission.")
  from Kaito_character import Mission
  Mission()
  

if __name__ == '__main__':
  Start()
