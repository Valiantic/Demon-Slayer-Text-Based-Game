

def Start():
    print("\n\n----------Kimetsu No Python: Code of the Demon Slayers----------")
    print("------------------Developed by Steven Madali--------------------\n\n\n\n")
    button = input(">>>>Press [K] to Hunt<<<<\n\n>>>>Press [X] to Exit<<<<\n")  # Get user input

    if button == "k":
        Characterselect()
    else:
        exit()

def Characterselect():
    
    while True:
        print("------------------Pick Your Demon Slayer--------------------")
        print("[1] Aoi Kanzaki\n The Flame Breathing Prodigy\n -Known 4 Flame Breathing Forms\n")
        print("[2] Hiro Aoiumi\n The Water Breathing Prodigy\n -Known 7 Water Breathing Forms\n")
        print("[3] Kasumi Arashi\n The Wind Breathing Successor\n -Known 5 Wind Breathing Forms\n")
        print("[4] Kaito Kaminari\n The Thunder Breathing Prodigy\n -Known 3 Thunder Breathing Forms\n")
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

def Aoi_Kenzaki():
    print("you choose aoi")
def Hiro_Aoiumi():
    pass
def Kasumi_Arashi():
    pass
def Kaito_Kaminari():
    pass

if __name__ == '__main__':
    Start()
