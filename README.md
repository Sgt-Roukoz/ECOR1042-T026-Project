T026 Image Editing Program(R) Version 1.1 04/01/2021

Contact Information
_________________
Marwan Zeid, the head developer of the T026 Image Editing Program can be reached at:
Phone:		613-447-5733
Email:		marwanzeid@cmail.carleton.ca
Website:	www.realt026website.com	


Description
_________

This program will ask for an image from the user and keep applying filters of the user's choice to the image until the user is satisfied. This program also allows the user to write a set of instructions on a text file which will be read to perform batch image processing. 


Installation
_________

To successfully run this image manipulation program, the installations of certain prerequisite programs must be completed. This image manipulating program requires Python version 3.9, and the latest versions of Pillow and NumPy must be installed on the system to function properly. You must extract Cimpl.py, Image.py, simple_Cimpl_filters.py, point_manipulation.py, T026_image_filters.py, T026_interactive_ui.py and T026_batch_ui.py into the same folder for the program to function correctly.


Usage
_____
The user has two ways to interact with the program. Through the interactive UI or through the batch UI.

Interactive UI:
For an interactive experience that shows the user the applied filters live, run T026_interactive_ui.py. The program will prompt the user, listing a group of commands that can be run by inputting the letter behind the “)” in the list of commands.

Note:
-The Program will only accept filter commands if an image has been loaded.
-If you decide to load an image without saving your current image, the current instance of the image will be lost forever.
-The draw curve and detect edges filter will prompt the user for extra information when executed.
 

Batch UI:
For editing a batch of images, run the batch_ui.py program. The user will be prompted to enter the name of the text file containing the instructions. 
The input for the name of the text file is case sensitive and must include the ".txt" type extension. 
The images to be edited must be in the same folder as the batch_ui.py program and the processed images are saved within the same folder. 
 
Text File Format:
x.jpg y.jpg C1 C2 C3 Cn
 
- x: Name of the image to be edited.
- y: Name of the image to be saved as after editing.
- C: Command of what type of filter will be performed on the image. 

There must be a minimum of 1 command and there can be "n" times of different command performed on the image.
The following are list of available commands for Batch UI:
- 3: Three Tone 
- X: Extreme Contrast
- P: Posterize
- V: Filp Vertical
- H: Flip Horizontal
- T: Sepia
 
Note:
- Everything must be separated by a single space.
- Succeeding images to be processed must be separated by a new line.
- The Draw Curve command is not available for batch editing.
- The default color for Three Tone is "aqua" (0,255,255) for replacing dark pixels, "blood" (255,0,0) for replacing mid-range brightness pixels, and "lemon" (255,255,0) for replacing bright pixels.
- The default threshold value for the Edge Detection Filter is 15
 
Example Usage of Batch UI:
A sample of a text file with the name "SampleBatchFile.txt" containing the following:
miss_sullivan.jpg test1.jpg 3 X P
miss_sullivan.jpg test2.jpg V H
 
Example Input on the Python Shell:
>>> Please input file name: (Format: 'xxx.txt')
>>> SampleBatchFile.txt


Credits
______

Marwan Zeid (101185876):
Combine filter, Sepia filter, Draw Curve filter, and Interactive UI

Johann Ocampo (101190287):
Red filter, Posterize filter, Flip Vertical filter, and Batch UI

Roy Luong (101195975):
Blue filter, Extreme Contrast filter, Edge Detection filter, and Interactive UI

Alex Jeromel (101190344):
Green filter, Three Tone filter, Flip Horizontal filter, and Batch UI

D.L. Bailey
Cimpl (Carleton Image Manipulation Python Library) Module

Carleton University
Point Manipulation Module

MIT License
__________

Copyright (c) 2021 Marwan Zeid, Roy Luong, Alex Jeromel, Johann Ocampo
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


