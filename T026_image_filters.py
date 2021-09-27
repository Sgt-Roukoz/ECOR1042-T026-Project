# ECOR1042 - P5 Task 2 Team Code: Modified Image Filters

# TeamID: T026

# Names and Student Number: 
# Marwan Zeid, 101185876
# Roy Luong, 101195975
# Alex Jeromel, 101190344
# Johann Ocampo, 101190287

# ===============================================

# Functions/Imports

from Cimpl import choose_file, create_color, create_image, get_color, set_color, load_image, Image, copy, show, save_as, get_width, get_height
from simple_Cimpl_filters import grayscale
from point_manipulation import get_x_y_lists, sort_points
from numpy import polyval, polyfit

def red_channel(image: Image) -> Image:
    """
    Returns a Cimpl.Image with only the red color value of each pixel of the original inputted Cimpl.Image (image).
    
    >>> image = load_image(choose_file())
    >>> red_filtered_image = red_channel(image)
    >>> show(red_filtered_image)
    
    Author: Johann Ocampo, 101190287
    """
    filtered_image = copy(image)
    
    for pixel in image:
        x, y, (r, g, b) = pixel 
        c = create_color(r, 0, 0)
        set_color(filtered_image, x, y, c)
    
    return filtered_image

def green_channel(image: Image) -> Image:
    """
    Returns the given image with the red and blue components filtered out of of each pixel's color.
   
   >>> image = load_image(choose_file())
   >>> green_image = green_channel(image)
   >>> show(green_image)
    
    Author: Alex Jeromel, 101190344
    """
    green_image = copy(image)
    for x, y, (r, g, b) in image:
        green = create_color(0,g,0)
        set_color(green_image, x, y, green)
   
    return green_image

def blue_channel(image: Image) -> Image:
    """
    Returns the selected image with the Red and Green values lowered to zero and 
    the Blue values kept the same
    
    >>> blue_image = blue_channel(image)
    
    Author: Roy Luong, 101195975
    """
    newImage = copy(image)
    for x,y, (r,g,b) in image:
        blue = create_color(0,0,b)
        set_color(newImage, x, y, blue)
    return (newImage)

def combine (image_red:Image, image_green:Image, image_blue:Image) -> Image:
    """Combines the red, green and blue channels of a photo to produce a full 
    color photo and returns the combined image.
    
    image_red is the red channel of the photo
    image_blue is the blue chennel of the photo
    image_green is the green channel of the photo
    
    >>>combine(red_pic, green_pic, blue_pic)
    
    Author: Marwan Zeid, 101185876
    """
    combined_image = create_image(1,1) # Create blank image
    if ((image_red.get_width() == image_green.get_width() == image_blue.get_width()) & (image_red.get_height() == image_green.get_height() == image_blue.get_height())):
        combined_image = create_image(image_red.get_width(), image_red.get_height())
    else:
        print("These images are not the same size!")
    
    for x, y, (r, g, b) in combined_image: # Go through blank image and setting RGB values of individual pixel
        red = get_color(image_red, x, y)
        green = get_color(image_green, x, y)
        blue = get_color(image_blue, x, y)
        col = create_color(red[0], green[1], blue[2])
        
        set_color(combined_image, x, y, col)
    
    return combined_image

def three_tone (image: Image, c1: str, c2: str, c3: str)->Image:
    """
    Team ID: T027
    Author: Alex Jeromel (101190344)
    Tester: Johann Ocampo (101190287)
   
    Returns a copy of the specified image with the three_tone filter applied to it.
    This function cycles through each pixel, calculates its brightness (average of the rgb components)
    and changes its color depending on the given pixel's brightness. If the pixel has a brightess less than or
    equal to 84, its color will be changed to c1. If the pixel has a brightness between or equal to 85 and 170, its
    color will be changed to c2. If the pixel has a brightness between or equal to 171 and 255, its color will be changed
    to c3.
   
    The colors compatible with this function, which are defined below, are:  
    black, white, blood, green, blue, lemon, aqua, pink, and gray.
   
    >>>image = load_image(choose_file())
    >>>three_tone_image = three_tone(image, "black", "gray", "white")
    >>>show(image)
    >>>show(three_tone_image)
    """
   
    black = create_color(0,0,0)
    white = create_color(255,255,255)
    blood = create_color(255,0,0)
    green = create_color(0,255,0)
    blue = create_color(0,0,255)
    lemon = create_color(255,255,0)
    aqua = create_color(0,255,255)
    pink = create_color(255,0,0)
    gray = create_color(128,128,128)   
    
    three_tone_image = copy(image)
    colors = [c1, c2, c3]
    new_color = black
        
    for x, y, (r, g, b) in image:
        pixel = get_color(image, x, y)
        r, g, b = pixel
        brightness = (r+g+b)/3
        
        if 0 <= brightness <= 84:
            i=0
        
        elif 85 <= brightness <= 170:
            i=1
        
        elif 171 <= brightness <= 255:
            i=2   
        
        color = colors[i]
        
        if color == "black":
            new_color = black
        elif color == "white":
            new_color = white
        elif color == "blood":
            new_color = blood
        elif color == "green":
            new_color = green
        elif color == "blue":
            new_color = blue
        elif color == "lemon":
            new_color = lemon
        elif color == "aqua":
            new_color = aqua
        elif color == "pink":
            new_color = pink
        elif color == "gray":
            new_color = gray      
        
        set_color(three_tone_image, x, y, new_color)
    
    return three_tone_image

def extreme_contrast(image)-> Image:
    """
    Team ID: T027
    Author: Roy Luong (101195975)
    Tester: Marwan Zeid (101185876)
    
    Returns the selected image with the RGB values adjusted to maximize contrast 
    between pixels
    
    >>> extreme_contrast_image = extreme_contrast(image)
    
    """
    newImage = copy(image)
    for x,y, (r,g,b) in image:
        if r <= 127:
            r2 = 0
        else:
            r2=255
            
        if g <= 127:
            g2 = 0
        else:
            g2=255
            
        if b <= 127:
            b2 = 0
        else:
            b2=255
        
        blue = create_color(r2,g2,b2)
        set_color(newImage, x, y, blue)
    return (newImage)

def sepia (original_image: Image) -> Image:
    """
    Returns an image that is tinted slightly yellow, a sepia tint
    
    >>> image = load_image(choose_file())
    >>> sepia_image = sepia(image)
    >>> show(sepia_image)
    
    Author: Marwan Zeid (101185876)
    Tester: Roy Luong (101195975)
    """
    temp_image = grayscale(original_image)
    
    for x, y, (r, g, b) in temp_image:
        if (r < 63): # Since in a grayscale image, the values of RGB are the same. Check if the RGB values are less than 63, dark gray
            col = create_color(int(r*1.1), g, int(b*0.9)) # Sets the R and B values to display a more yellowish colour
            set_color(temp_image, x, y, col) # Changes the color of that pixel in the image
        elif (r <= 191): # Checks if the values are between 63 and 191, medium gray
            col = create_color(int(r*1.15), g, int(b*0.85)) # sets the R value to be 1.15 times larger, while the B values to be 0.85 times smaller
            set_color(temp_image, x, y, col)
        elif (r <= 255): # checks if the RGB values are greater than 191, but smaller than 255. Light gray -> white
            col = create_color(int(r*1.08), g, int(b*0.93)) # sets the R value to be 1.08 times larger, while the B value to be 0.93 times smaller
            set_color(temp_image, x, y, col)            
    
    return temp_image

def posterize(image: Image) -> Image:
    """
    Returns a Cimpl.Image that posterizes each pixel of the original inputted Cimpl.Image (image).
    
    It posterizes each red, green, blue value of each pixel by setting its value to the mid point of the quadrant that it falls under.
    Color value sets to 31 if within 0-63, 95 if within 64-127, 159 if within 128-191, and 223 if within 192-255.
    The color value is determined by the function _adjust_component
    
    Author: Johann Ocampo (101190287)
    Tester: Alex Jeromel (101190344)
    
    >>> image = load_image(choose_file())
    >>> posterized_image = posterize(image)
    >>> show(posterized_image)
    """
    posterized_image = copy(image)
    
    for pixel in image:
        x,y,(r,g,b) = pixel
        c = create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b))
        set_color(posterized_image, x, y, c)
    
    return posterized_image

def detect_edges(image,threshold: int)-> Image:
    """
    Team ID: T027
    Author: Roy Luong (101195975)
    Tester: Marwan Zeid (101185876)
    Returns an image that looks like a pencil sketch, by changing the pixels'
    colors to black or white based on whether the difference between the brightness
    of the pixel and the one below it is greater or less than the given threshold.
    Threshold values below 50 work the better for regular images.
    
    >>> detect_edges_image = detect_edges(image,threshold)
    
    """
    newImage = copy(image)
    height = (get_height(image)-1)
    for x,y, (r,g,b) in image:
        
        #for every pixel except the last row checks the difference in brightness 
        #between the pixel and the one below it
        if y < height:
            brightness1 = (r+g+b)/3
            
            pixel2 = get_color(image, x, y+1)
            brightness2 = (pixel2[0]+pixel2[1]+pixel2[2])/3
            
            diff = abs(brightness1-brightness2)
            if diff > threshold:
                colour= 0
            else: 
                colour = 255
        else:
            colour = 255
        
        #Sets the colour of the pixel based on whether the contrast was high or low
        newColour = create_color(colour,colour,colour)
        set_color(newImage, x, y, newColour)
    return newImage

def draw_curve(image: Image, color: str, points_list:list = None) -> tuple:
    ''' 
    Returns a tuple containing the image with a curve that is 9 pixels wide drawn upon it based on
    chosen Image, chosen color and a list of the points on the border of the image 
    
    >>> draw_curve(image, "red", [(300,56), (200, 346), (89, 100)])
    (curve_image, [(310, 0), (None, 480)])
    >>> draw_curve(image, "green")
    (curve_image, bounds)
    
    Author: Marwan Zeid (101185876)
    Tester: Roy Luong (101195975)
    '''
    
    curve_image = copy(image) # Create copy of image
    pixel_x = get_width(image) # Get Width and Height of the image
    pixel_y = get_height(image)
    
    print(f"This image has a width of {pixel_x} and a height of {pixel_y}")
    
    line_color = _translate_color(color)
        
    if (points_list == None):
        points_list = []
        
        valid = False
        while not valid:
            number_of_points = int(input("How many points do you want to provide? The number should be greater than or equal to 2: ")) # get number of points from user
            if number_of_points >= 2:
                valid = True
            else:
                print ("The number must be greater than or equal to 2")
        
        print("Input the coordinates of the points")
        
        for i in range(number_of_points): # Allow user to input coordinates
            print("Coordinates of point " + str(i+1) + ":")
            x = int(input("Input X coordinate: "))
            y = int(input("Input y coordinate: "))
            points_list.append((x,y))
    
    coefficients = _interpolation(points_list) # Generate function based on points given
    
    bounds = _image_border_finding((pixel_x,pixel_y), coefficients) # Get curve bounds within image

    x = 0
    
    while x < pixel_x: # Draw curve on image based on polyval values
        y = int(polyval(coefficients, x)) # Evaluate y value at current x (iteration)
        
        if ((y < 0) or (y >= pixel_y)): # If out of bounds, skip drawing
            x += 1
        
        else:
            for i in range(-4,5):
                if ((y+i < pixel_y) and (y+i >= 0)):  # Draws line that is 9 wide (+- 4 pixels from y and x)
                    set_color(curve_image, x, y+i, line_color)
                    if ((x+i < pixel_x) and (x+i >= 0)):
                        set_color(curve_image, x+i, y, line_color)
            x += 1
    
    return (curve_image, bounds)

def flip_horizontal (image: Image)->Image:
    """
    Team ID: T027
    Author: Alex Jeromel (101190344)
    Tester: Johann Ocampo (101190287)
    
    Returns a copy of the specified image with the flip_horizontal filter applied to it.
    The overall result is a picture that has all of its pixels in the exact opposite position
    when flipped about a vertical line that is in the middle of the image.
    
    >>>image = load_image(choose_file())
    >>>flipped_image = flip_horizontal(image)
    >>>show(image)
    >>>show(flipped_image)
    """ 
    flipped_image = copy(image)
    width = get_width(flipped_image)
    center = int(width/2)
        
    for y in range(get_height(flipped_image)):
        for x in range(center):
            color = get_color(flipped_image, x, y)
            
            set_color(flipped_image, x, y, get_color(flipped_image, width-1-x, y))
            
            set_color(flipped_image, width-1-x, y, color)
          
    return flipped_image

def flip_vertical(image : Image) -> Image:
    """
    Returns a Cimpl.Image that flips each pixel of the inputted Cimpl.Image (image) vertically over its imaginary horizontal center line.
    
    Author: Johann Ocampo (101190287)
    Tester: Alex Jeromel (101190344)
    
    >>> image = load_image(choose_file())
    >>> vertical_flip_image = flip_vertical(image)
    >>> show(vertical_flip_image)
    """
    vertical_flip_image = copy(image)
    height = get_height(vertical_flip_image) # Get the height of the image
    center = int(height/2) # Find the horizontal center point of the image
    
    for x in range(get_width(vertical_flip_image)):
        for y in range(center):
            # Temporarily Store the color data of the current pixel
            c = get_color(vertical_flip_image, x, y)
                
            # Set color of current pixel to color of pixel that is opposite to it from the center
            set_color(vertical_flip_image, x, y, get_color(vertical_flip_image, x, (height-1)-y))
            # Set color of the pixel that it is opposite to the current pixel from the center to the color of the current pixel 
            set_color(vertical_flip_image, x, (height-1)-y, c)                
            
    return vertical_flip_image

def _adjust_component(color: int) -> int:
    """
    Returns an integer representing the midpoint of one of the four quadrants of a single color scale that 
    range from 0-255 depending on the value of the color inputted (color).
    
    >>> _adjust_component(0)
    >>> 31
    >>> _adjust_component(40)
    >>> 31
    >>> _adjust_component(63)
    >>> 31
    
    >>> _adjust_component(64)
    >>> 95
    >>> _adjust_component(80)
    >>> 95
    >>> _adjust_component(127)
    >>> 95
    
    >>> _adjust_component(128)
    >>> 159
    >>> _adjust_component(150)
    >>> 159
    >>> _adjust_component(191)
    >>> 159
    
    >>> _adjust_component(192)
    >>> 223
    >>> _adjust_component(200)
    >>> 223
    >>> _adjust_component(255)
    >>> 223
    
    Author: Johann Ocampo (101190287)
    """
    midpoints = (31, 95, 159, 223)
    quandrant = 0
    
    if(0 <= color <= 63):
        quadrant = 0
    elif(color <= 127):
        quadrant = 1
    elif(color <= 191):
        quadrant = 2
    else:
        quadrant = 3
    
    return midpoints[quadrant]

def _interpolation(points: list) -> list: 
    '''
    Returns a list containing the coefficients of the interpolating polynomial depending upon the inputted list of points (points).
    The function will perform linear interpolation if 2 points are inputted and quadratic regression if 3 or more points are inputted.
    
    This function will return None if the inputted list has 1 elements or less.
    
    >>>_interpolation([(1,1)])
    None
    
    >>>_interpolation([(1, 1), (2, 2)])
    [0.9999999999999994, 1.0251616081943926e-15]
    
    >>>_interpolation([(1, 1), (2, 1), (3, 3)])
    [1.000000000000002, -3.000000000000007, 3.000000000000006]
    
    >>> _interpolation([(1, 1), (2, 1), (3, 3), (4, -4), (5, 2), (6, 7)])
    [0.73214285714286, -4.382142857142879, 5.90000000000004]
    
    Author: Johann Ocampo (101190287)
    '''
    points = sort_points(points)
    coordinates = get_x_y_lists(points)
    
    if len(points) < 2: # If given only 1 or less coordinates 
        return None
    elif len(points) <= 3: # If given only 2 or 3 coordinates
        coefficients = polyfit(coordinates[0], coordinates[1], len(points)-1)
    else: # If given more than 3 coordinates
        coefficients = polyfit(coordinates[0], coordinates[1], 2)
    
    return list(coefficients)

def _image_border_finding(image_size: list, interpol: list) -> list:
    '''
    Returns the pixels where the curve intersects the border of the image
    
    >>> _image_border_finding((640,480), [6.33e-03,-3.80e+00,5.57e+02])
    [(253, 0), (21, 480)]
    >>>_image_border_finding((640,480),  [7.24e-04,-1.19e+00,4.51e+02])
    [(590, 0), (None, 480)]
    >>> _image_border_finding((976,1080),  [7.24e-04,-1.19e+00,4.51e+02])
    [(590, 0), (None, 1080)]
    
    Author: Marwan Zeid (101185876)
    '''
    
    x_one = _exhaustive_search(image_size[0]-1, interpol, 0)
    x_two = _exhaustive_search(image_size[0]-1, interpol, image_size[1]-1)
    
    border_set = [(x_one, 0), (x_two, image_size[1])]
    
    return border_set

def _exhaustive_search(max_x: int, polycoeff: list, val:int) -> int:
    '''
    Solves f(x)-val=0 for x between 0 and max_x where polycoeff contains
    the coefficients of f, using EPSILONof 1 (as we only need ints for pixels).  
    Returns None if there is no solution between the bounds.
    
    >>> _exhaustive_search(639,[6.33e-03,-3.80e+00,5.57e+02],0)
    253
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],0)
    590
    >>> _exhaustive_search(639,[7.24e-04,-1.19e+00,4.51e+02],479)
    None
    
    Author: Marwan Zeid (101185876)
    '''
    
    EPSILON = 1
    guess = 0
    step = EPSILON
    func = polyval(polycoeff, guess) - val
    
    while abs(func) >= EPSILON and guess <= max_x: # Compare calculated value to chosen threshold (EPSILON), stops if reached a solution or if went past max_x bound
        guess += step
        func = polyval(polycoeff, guess) - val
    
    if guess > max_x: # If guess exceeded the width of the image
        return None
    else:
        return guess
     
def _translate_color(color: str):
    '''
    Returns the RGB value of the given color
    
    >>> _translate_color("red")
    >>> (255,0,0)
    >>> _translate_color("pink")
    >>> (255,0,255)
    >>> _translate_color("gray")
    >>> (128,128,128)
    
    Author: Marwan Zeid (101185876)
    '''
    rgb = create_color(0,0,0) # Set default black
    
    if (color == "black"): # Set color based on inputted string
        rgb = create_color(0,0,0)
    elif (color == "white"):
        rgb = create_color(255,255,255)
    elif (color == "blood" or color == "red"):
        rgb = create_color(255,0,0)
    elif (color == "green"):
        rgb = create_color(0,255,0)
    elif (color == "blue"):
        rgb = create_color(0,0,255)
    elif (color == "lemon"):
        rgb = create_color(255,255,0)
    elif (color == "aqua"):
        rgb = create_color(0,255,255)
    elif (color == "pink"):
        rgb = create_color(255,0,255)
    elif (color == "gray"):
        rgb = create_color(128,128,128)
    
    return rgb

