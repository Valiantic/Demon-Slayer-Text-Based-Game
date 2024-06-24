#BATTLE SYSTEM CONCEPT

# import random

# class Character:
#     def __init__(self, name, max_health, attack_power, attacks):
#         self.name = name
#         self.max_health = max_health
#         self.current_health = max_health
#         self.attack_power = attack_power
#         self.attacks = attacks

#     def is_alive(self):
#         return self.current_health > 0

#     def take_damage(self, damage):
#         self.current_health -= damage
#         if self.current_health < 0:
#             self.current_health = 0

#     def display_stats(self):
#         print(f"{self.name}'s Stats:")
#         print(f"  Health: {self.current_health}/{self.max_health}")

# def generate_enemy(level):
#     enemy_names = ["Goblin", "Ogre", "Skeleton Mage"]
#     enemy_health = level * 20 + random.randint(10, 20)
#     attack_power = level * 5 + random.randint(2, 5)
#     enemy_attacks = ["Claw Attack", "Slam", "Shadow Bolt"]
#     return Character(random.choice(enemy_names), enemy_health, attack_power, enemy_attacks)

# def battle(player, enemy):
#     while True:
#         # Display stats
#         player.display_stats()
#         enemy.display_stats()

#         # Player turn
#         print("\nWhat attack will you use?")
#         for i, attack in enumerate(player.attacks):
#             print(f"  {i+1}. {attack}")
#         attack_choice = int(input("> ")) - 1

#         if attack_choice < 0 or attack_choice >= len(player.attacks):
#             print("Invalid attack choice. Please try again.")
#             continue

#         damage = player.attack_power
#         print(f"{player.name} uses {player.attacks[attack_choice]}!")
#         enemy.take_damage(damage)

#         if not enemy.is_alive():
#             print(f"{enemy.name} has been defeated!")
#             break

#         # Enemy turn (simplified for this basic example)
#         enemy_damage = enemy.attack_power
#         print(f"\n{enemy.name} attacks you!")
#         player.take_damage(enemy_damage)

#         if not player.is_alive():
#             print(f"You have been defeated. Game Over!")
#             break

# # Game setup
# player_name = input("Enter your name, adventurer: ")
# player_attacks = ["Sword Slash", "Shield Bash", "Healing Potion"]  # Replace with your desired attacks

# player = Character(player_name, 100, 10, player_attacks)
# enemy = generate_enemy(1)  # Adjust level as needed

# # Start the battle
# battle(player, enemy)
