Raspberry Pi Project: Keypad Audio Mixer and Soundboard
Project Description:
This project displays the usage of the matrix keypad by creating sounds and display images with a click of the pad. This was created through the Raspberry Pi 4 with the hardware and coding from various components that will be listed below. Most of the code was made from scratch and was built on upon the basic keypad entry. I decided to create a basic music mixer for users to use and create their own music with. Everything plays at 90 BPM (Beats per minute) for consistency. With 12 different audio loops, users can create unique tracks and create their own tune. When I created this, I realized the possibility of creating music with the Raspberry Pi. For future implementations, I plan to add recording options to record your unique audio that was created.  

Hardware Components:
- Raspberry Pi 4
- Samsung MicroSD 256GB
- Project Board
- GPIO Extension Board
- GPIO Cable
- 4x10k Resistors
- 8 Jump Wires
- JBL Speaker Jack Output

Files and Modules:
- MatrixKeypad_GUI.py
-Keypad.py
-Keypad2.py
-sounds/: Directory containing sound files.
-images/: Directory containing image files.

Coding Components:
-Python3
-Pillow
-Pygame library
-TKinter
-Random
How to run:
1.	Run the ‘MatrixKeypad1_GUI.py’
2.	GUI will appear and show the current mode (DEFAULT AT MODE: A)
3.	Interact with the keypad to see output.
4.	Trigger numpad ‘A’ ‘B’ ‘C’ ‘D’ to dynamically switch from each mode.

Modes and Functions:
-Mode A: Will be the DEFAULT outputs; meaning that the keys on the keypad will be displayed.
-Mode B: Will be the EMOTICON output; meaning that each key will display a unique emoticon.
-Mode C: Will be the MIXER output; meaning that each key will display a looped instrumental. Each input would be layered to create a unique tune. 
-Mode D: Will be the SOUND output; meaning that each key will play a sound through the default audio output. In addition, an image will also be displayed.

Known Issues:
There has been an issue with importing certain libraries such as ImageTK and Pillow. Due to this, images have not been able to be displayed. 

Images have successfully been able to be displayed. The images that pop up will be at random sections of the window screen. I have implemented the random function for the window to pop up for comedic purposes.

