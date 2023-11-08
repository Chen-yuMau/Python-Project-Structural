import tkinter as tk
import subprocess
# from Structural import StructuraL

def play_friend_offline():
	# Implement the functionality for "Play Friend Offline" here
	subprocess.Popen(["python", "Structural.py"])
	pass

def play_friend_online():
	# Implement the functionality for "Play Friend Online" here
	pass

# def play_ai_offline():
#	 # Implement the functionality for "Play AI Offline" here
#	 pass
		
# Create the main window
root = tk.Tk()
root.title("Structural")
	
# Create a label for the game title
title_label = tk.Label(root, text="Structural", font=("Arial", 24), fg="blue")
title_label.pack(pady=20)

# Create buttons for menu choices
play_friend_offline_button = tk.Button(root, text="Play Friend Offline", command=play_friend_offline, width=20, height=2)
play_friend_offline_button.pack()

play_friend_online_button = tk.Button(root, text="Play Friend Online", command=play_friend_online, width=20, height=2)
play_friend_online_button.pack()

# play_ai_offline_button = tk.Button(root, text="Play AI Offline", command=play_ai_offline, width=20, height=2)
# play_ai_offline_button.pack()

root.geometry("400x300")  # Set the window size
root.mainloop()
