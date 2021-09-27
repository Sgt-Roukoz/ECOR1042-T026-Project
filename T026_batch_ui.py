# ECOR1042 - Milestone 3 - Batch User Interface
# Team ID: T026
# Name and Student Number: Johann Padraig Ocampo (Student Number: 101190287) & Alex Jeromel (Student Number: 101190344)

from Cimpl import choose_file, create_color, create_image, get_color, set_color, load_image, Image, copy, show, save_as, get_height, get_width
from T026_image_filters import *

# Dictionary containing the keyword and its corresponding filter
filter_commands = { "3": three_tone,
                    "X": extreme_contrast,
                    "P": posterize,
                    "E": detect_edges,
                    "V": flip_vertical,
                    "H": flip_horizontal,
                    "T": sepia}

def execute_command(instructions: list) -> None:
    """
    Returns a Cimpl.Image that is processed by one or more filters depending on the inputted list (instructions). 
    
    Parameters:
    instructions = ["file name", "name to be saved as", filter 1, filter 2, . . . filter n]
        - The 1st element of the list contains the file name of the image to be processed
        - The 3rd element of the list and beyond are the list of filters that the image will be processed in the order that it is given
          where "n" is the last filter that will be used on the image. The instructions list must always have a minimum size of 3. There 
          is always at least one filter to be used to process the image (3rd elemnt of the list) and the rest of the elements after that 
          are additional fitlers to be used. 
    
    Author: Johann Padraig Ocampo (Student Number: 101190287) & Alex Jeromel (Student Number: 101190344)
    """
    # Load the Image 
    image = load_image(instructions[0])
    
    # Make a copy of the image
    processed_image = copy(image)
    
    # Process the image as many times as instructed with the appropriate filter
    for filters in range(2, len(instructions)):
        if instructions[filters] == "3":
            processed_image = filter_commands[instructions[filters]](processed_image, "aqua", "blood", "lemon")
        elif instructions[filters] == "E":
            processed_image = filter_commands[instructions[filters]](processed_image, 15)
        else:    
            processed_image = filter_commands[instructions[filters]](processed_image)
    
    return processed_image

# Main Function
if __name__ == "__main__":
    # Ask user for file name:
    filename = input("Please input file name: (Format: 'xxx.txt')\n")
    
    # Open file with the given file name:
    batch_file = open(filename)
    
    # Parse each lines of the file
    for line in batch_file:
        items = line.split() 
        
        # Create the processed image
        processed_image = execute_command(items)
        
        # Save the processed image with the given filename 
        save_as(processed_image, items[1])        
    
    # Close File
    batch_file.close()
