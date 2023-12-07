import Keypad   # import module Keypad
import pygame
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

pygame.mixer.init()

ROWS = 4        # number of rows of the Keypad
COLS = 4        # number of columns of the Keypad
keys = ['1', '2', '3', 'A',    # key code
        '4', '5', '6', 'B',
        '7', '8', '9', 'C',
        '*', '0', '#', 'D']

rowsPins = [18, 23, 24, 25]     # connect to the row pinouts of the keypad
colsPins = [10, 22, 27, 17]     # connect to the column pinouts of the keypad

current_mode = 'A'  # Initial mode

# Define mode_descriptions
mode_descriptions = {
    'A': 'Normal Output',
    'B': 'Emoticons',
    'C': 'Music Mixer',
    'D': 'Sounboard'
}

# Dictionary mapping keys to image file paths
image_paths_mode_d = {
    '1': 'images/image1.png',
    '2': 'images/image2.png',
    '3': 'images/image3.png',
    '4': 'images/image4.png',
    '5': 'images/image5.png',
    '6': 'images/image6.png',
    '7': 'images/image7.png',
    '8': 'images/image8.png',
    '9': 'images/image9.png',
    '0': 'images/image10.png',
    '*': 'images/image11.png',
    '#': 'images/image12.png'
}

# Dictionary mapping keys to music file paths
music_paths_mode_c = {
    '1': 'sounds/music1.wav',
    '2': 'sounds/music2.wav',
    '3': 'sounds/music3.wav',
    '4': 'sounds/music4.wav',
    '5': 'sounds/music5.wav',
    '6': 'sounds/music6.wav',
    '7': 'sounds/music7.wav',
    '8': 'sounds/music8.wav',
    '9': 'sounds/music9.wav',
    '0': 'sounds/music10.wav',
    '*': 'sounds/music11.wav',
    '#': 'sounds/music12.wav'
}

# Dictionary to store loaded sounds and channels
loaded_sounds = {}
playing_channels = {}
last_played_channel = None

# Function to play/stop music with volume adjustment
def play_stop_music(key):
    global loaded_sounds, playing_channels, last_played_channel

    # Stop the last played channel
    if last_played_channel is not None:
        last_played_channel.set_volume(0.75)  # Lower volume for the last played channel

    if key in music_paths_mode_c:
        if key not in loaded_sounds:
            sound_file = music_paths_mode_c[key]
            loaded_sounds[key] = pygame.mixer.Sound(sound_file)

            channel = pygame.mixer.Channel(len(playing_channels) + 1)
            channel.set_volume(1.0)  # Set volume to 100%

            # Play the sound without adjusting playback speed
            channel.play(loaded_sounds[key], loops=-1, fade_ms=1000)
            channel.set_endevent(pygame.constants.USEREVENT)

            playing_channels[key] = channel
            last_played_channel = channel

            # Create a label to display "Now Playing Input {Key}"
            now_playing_label = tk.Label(root, text=f"Now Playing Input {key}")
            now_playing_label.pack()

            # Store the label reference in playing_channels dictionary
            playing_channels[key + "_label"] = now_playing_label
        else:
            loaded_sounds[key].stop()
            loaded_sounds.pop(key)
            playing_channel = playing_channels.pop(key, None)
            if playing_channel:
                playing_channel.stop()

                # Remove the label associated with the stopped input
                label_to_remove = playing_channels.pop(key + "_label", None)
                if label_to_remove:
                    label_to_remove.destroy()

# Function to close the image window
def close_image_window(image_window):
    image_window.destroy()
    
# Function to display image in a new window
def show_image_mode_d(key):
    image_path = image_paths_mode_d.get(key)

    if image_path:
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        # Create a new Toplevel window
        image_window = tk.Toplevel(root)
        image_window.title(f"Mode D: {key}")

        # Set geometry for faster rendering (adjust the size as needed)
        image_window.geometry("200x240")

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate a random position for the window
        x_position = random.randint(0, screen_width - 200)
        y_position = random.randint(0, screen_height - 240)

        # Set the window position
        image_window.geometry(f"+{x_position}+{y_position}")

        # Display the image in the new window
        image_label = tk.Label(image_window, image=img_tk, text=f"Mode D: {key}", compound=tk.TOP)
        image_label.image = img_tk
        image_label.pack()

        # Display text below the image
        text_label = tk.Label(image_window, text=f"Mode D: {key}", font=("Helvetica", 12))
        text_label.pack()

        # Schedule the close_image_window function after 2000 milliseconds (2 seconds)
        image_window.after(6000, lambda: close_image_window(image_window))
        
# Function to play piano sound
def output_piano_sound(key):
    piano_sounds = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '0': '10',
        '*': '11',
        '#': '12'
    }
    sound_file = piano_sounds.get(key)
    
    if sound_file:
        sound_file = f"sounds/{sound_file}.wav"
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        pygame.time.wait(1000)  # Wait for sound to finish playing (adjust as needed)
        result_label.config(text=f"Mode D: {key}")


# Function to switch mode
def select_mode(key):
    global current_mode
    if key in ['A', 'B', 'C', 'D']:
        current_mode = key
        mode_label.config(text=f"Switched to Mode {current_mode} - {mode_descriptions[current_mode]}")

# Callback function when a key is pressed
def on_key_press(key):
    select_mode(key)
    if current_mode == 'A':
        result_label.config(text=f"Mode A: You Pressed Key: {key}")
    elif current_mode == 'B':
        output_emoticons(key)
    elif current_mode == 'C':
        play_stop_music(key)
    elif current_mode == 'D':
        show_image_mode_d(key)
        output_piano_sound(key)

# Function to output emoticons
def output_emoticons(key):
    emoticons = {
        '1': ':)',
        '2': ':(',
        '3': ':D',
        '4': ':O',
        '5': ':|',
        '6': ':p',
        '7': ':/',
        '8': ';)',
        '9': ':*',
        '0': '<3',
        '*': '^_^',
        '#': '-_-'
    }
    result_label.config(text=f"{emoticons.get(key, mode_descriptions['B'])}", font=("Helvetica",200))

# Function to output onomatopoeias
def output_onomatopoeias(key):
    onomatopoeias = {
        '1': 'Bang',
        '2': 'Boing',
        '3': 'Buzz',
        '4': 'Crash',
        '5': 'Drip',
        '6': 'Hiss',
        '7': 'Meow',
        '8': 'Quack',
        '9': 'Roar',
        '0': 'Swoosh',
        '*': 'Tick',
        '#': 'Zap'
    }
    result_label.config(text=f"{onomatopoeias.get(key, mode_descriptions['C'])}", font=("Helvetica",200))

# GUI Initialization
root = tk.Tk()
root.title("Matrix Keypad GUI")

# Mode Label
mode_label = tk.Label(root, text=f"Current Mode: {mode_descriptions[current_mode]}")
mode_label.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Keypad Initialization
keypad = Keypad.Keypad(keys, rowsPins, colsPins, ROWS, COLS)
keypad.setDebounceTime(50)

# Function to handle keypad events
def check_keypad():
    key = keypad.getKey()
    if key != keypad.NULL:
        on_key_press(key)
    root.after(10, check_keypad)

# Start checking keypad events
check_keypad()

# Start GUI main loop
root.mainloop()