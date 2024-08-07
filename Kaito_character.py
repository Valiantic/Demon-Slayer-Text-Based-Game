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

 
# Fighting Attributes
class Character:
    def __init__(self, name, max_health, attack_power, attacks):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attack_power = attack_power
        self.attacks = attacks

    def is_alive(self):
        return self.current_health > 0

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0

    def display_stats(self):
        print(f"{self.name}'s Stats:")
        print(f"  Health: {self.current_health}/{self.max_health}")

def generate_enemy(level):
    enemy_names = ["Raging oni", "Illusionist imp", "Pestilent ghoul", "Spectral slayer"]
    enemy_health = level * 20 + random.randint(10, 20)
    attack_power = level * 5 + random.randint(2, 5)
    enemy_attacks = ["Claw Attack", "Slam", "Shadow Bolt","Brutal Bite"]
    return Character(random.choice(enemy_names), enemy_health, attack_power, enemy_attacks)


def clear_screen():
  
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear') 
    
def Mission():
 
    mission_place = ["Mount Yokogawa", "Swordsmith Village", "Entertainment District", "Crimson Light District"]
    
    random_mission = random.choice(mission_place)
    
    print("\n>You Mission is to go in: \n", random_mission,"!\n")

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
  
  
# Places
  
def Mount_Yokogawa():
  clear_screen()
  print("\nWelcome to Mount Yokogawa!\n")
  print("A demon outbreak ravaged a village on Mount Yokogawa, leaving its inhabitants forever \nmarked by the harrowing encounter. This event sparked a\nvow for vengeance in one determined survivor.")
  speak("\nWelcome to Mount Yokogawa!\n")
  speak("A demon outbreak ravaged a village on Mount Yokogawa, leaving its inhabitants forever \nmarked by the harrowing encounter. This event sparked a\nvow for vengeance in one determined survivor.")
  wonder = input("\nPress anything to wonder >>>")
  battle(player, enemy)
  
def Swordsmith_Village():
  clear_screen()
  print("\nWelcome to Swordsmith Village!\n")
  print("Driven by this oath, the survivor ventured to the hidden Swordsmith Village. Their unwavering\n determination impressed a master smith who recognized their potential and\ncrafted a unique weapon to aid them in their fight against demons.")
  speak("\nWelcome to Swordsmith Village!\n")
  speak("Driven by this oath, the survivor ventured to the hidden Swordsmith Village. Their unwavering\n determination impressed a master smith who recognized their potential and\ncrafted a unique weapon to aid them in their fight against demons.")
  wonder = input("\nPress anything to wonder >>>")
  battle(player, enemy)
def Entertainment_District():
  clear_screen()
  print("\nWelcome to Entertainment District!\n")
  print("Rumors of a powerful demon lurking within the dazzling yet deceitful Entertainment District drew the warrior in.\nThis vibrant location with its hidden dangers became their next destination.")
  speak("\nWelcome to Entertainment District!\n")
  speak("Rumors of a powerful demon lurking within the dazzling yet deceitful Entertainment District drew the warrior in.\nThis vibrant location with its hidden dangers became their next destination.")
  wonder = input("\nPress anything to wonder >>>")
  battle(player, enemy)
def Crimson_Light_District():
  clear_screen()
  print("\nWelcome to Crimson Light District!\n")
  print("Undeterred by whispers of danger, the warrior ventures even deeper into the clandestine Crimson Light District.\nThis even more secretive area is rumored to hold the\n key to their past or destiny, motivating them to confront the evil they seek.")
  speak("\nWelcome to Crimson Light District!\n")
  speak("Undeterred by whispers of danger, the warrior ventures even deeper into the clandestine Crimson Light District.\nThis even more secretive area is rumored to hold the\n key to their past or destiny, motivating them to confront the evil they seek.")
  wonder = input("\nPress anything to wonder >>>")
  battle(player, enemy)
  
  
# Battleground

def battle(player, enemy):
    while True:
        clear_screen()
        # Display stats
        
        print(f"You've encountered a: {enemy.name}\n")
        player.display_stats()
        enemy.display_stats()
        
    

        # Player turn
        print("\nWhat form will you use?")
        for i, attack in enumerate(player.attacks):
            print(f"  {i+1}. {attack}")
        attack_choice = int(input("> ")) - 1

        if attack_choice < 0 or attack_choice >= len(player.attacks):
            print("Invalid attack choice. Please try again.")
            continue

        damage = player.attack_power
        print(f"{player.name} uses {player.attacks[attack_choice]}!")
        enemy.take_damage(damage)

        if not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy turn (simplified for this basic example)
        enemy_damage = enemy.attack_power
        print(f"\n{enemy.name} attacks you!")
        player.take_damage(enemy_damage)

        if not player.is_alive():
            print(f"You have been defeated. Game Over!")
            break

# Game setup
player_name = "Kaito Kaminari"
player_attacks = ["First Form: Thunderclap and Flash ", "Second Form: Rice Spirit"]  # Replace with your desired attacks

player = Character(player_name, 100, 12, player_attacks)
enemy = generate_enemy(1)  # Adjust level as needed

# Start the battle
if __name__ == '__main__':
    Mission()
    battle(player, enemy)

