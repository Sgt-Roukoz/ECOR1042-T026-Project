# ECOR1042 - P5 Task 1 Team Code: Interactive UI

# TeamID: T026

# Names and Student Number: 
# Marwan Zeid, 101185876
# Roy Luong, 101195975
# Alex Jeromel, 101190344
# Johann Ocampo, 101190287

# ===============================================

# Functions/Imports
from Cimpl import choose_file, load_image, save, save_as, Image
from T026_image_filters import *


def interactive_ui() -> None:
    """
    The main script of the T026 image filters, does not return any values but 
    walks the user through the image filter program.
    
    >>> interactive_ui()
    """
    interact = True 
    image = None # Create empty Image
    recognized_commands = ["L", "S", "3", "X", "T", "P", "E", "D", "V", "H", "Q"] # List of accepted inputs
    
    print("\nWelcome to T026's Image Editing Program.\nTo execute a command, the user types the number or upper-case letter to the left of the ‘)’, \nthen presses the Enter key.\n")
    
    while interact:
        if image != None and response in recognized_commands: show(image)
        
        print("\nL)oad image  S)ave-as\n3)-tone  X)treme contrast  T)int sepia  P)osterize\nE)dge detect  D)raw curve  V)ertical flip  H)orizontal flip\nQ)uit\n")
        response = input(": ")
        response = response.upper()
        
        if response not in recognized_commands: # Checks if command is found in list, if it isn't, it informs the user
            print("\nNo such command")
        elif response == "Q": # quits program if user inputted q or Q
            print("Quitting Program")
            interact = False
        elif response == "L": # lets user choose to load an image if inputted l or L
            image = load_image(choose_file())
        elif image == None: # if user attempted to apply filters with no image loaded, inform user
            print("\nNo image loaded\n")        
        elif response == "S" and image != None: # allows user to save image if inputted s or S (as long as image exists)
            save_as(image)
        elif response == "X": # apply extreme contrast filter if user inputted x or X
            image = extreme_contrast(image)
        elif response == "T": # apply sepia tint filter if user inputted t or T
            image = sepia(image)
        elif response == "P": # apply posterize filter if user inputted p or P
            image = posterize(image)
        elif response == "E": # apply edge detection filter if user inputted e or E
            thresh = int(input("\nEnter threshold value: "))
            image = detect_edges(image, thresh) # Run detect edges filter with a threshold set by user
        elif response == "D": # apply draw_curve filter if user inputted d or D
            returned_tuple = draw_curve(image, "lemon") # Run draw curve filter with lemon as default color
            image = returned_tuple[0]
        elif response == "V": # apply vertical flip filter if user inputted v or V
            image = flip_vertical(image)
        elif response == "H": # apply horizontal flip filter if user inputted h or H
            image = flip_horizontal(image)
        elif response == "3": # apply three-tone filter if user inputted 3
            image = three_tone(image, "aqua", "blood", "lemon") # Run three-tone filter with aqua, blood, and lemon as default colors


#Main Script
if __name__ == "__main__":
    interactive_ui()