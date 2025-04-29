import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time
import threading

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Pygame vs Arcade - Game Launcher")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Configure colors and fonts
        self.bg_color = "#2E2E2E"
        self.fg_color = "#FFFFFF"
        self.button_color = "#3E3E3E"
        self.highlight_color = "#4E4E4E"
        self.title_font = ("Arial", 18, "bold")
        self.button_font = ("Arial", 12)
        self.info_font = ("Arial", 10, "italic")
        
        self.root.configure(bg=self.bg_color)
        
        # Title
        self.title_label = tk.Label(
            root, 
            text="Pygame vs Arcade Comparison", 
            font=self.title_font,
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.title_label.pack(pady=20)
        
        # Find all matching games
        self.games = self.find_matching_games()
        
        # Game selection frame
        self.selection_frame = tk.Frame(root, bg=self.bg_color)
        self.selection_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create buttons for each game
        for game in self.games:
            formatted_name, filename = game
            button = tk.Button(
                self.selection_frame,
                text=formatted_name,
                font=self.button_font,
                bg=self.button_color,
                fg=self.fg_color,
                activebackground=self.highlight_color,
                activeforeground=self.fg_color,
                relief=tk.FLAT,
                width=30,
                height=2,
                command=lambda g=game: self.launch_game(g)
            )
            button.pack(pady=5)
        
        # Information label
        self.info_label = tk.Label(
            root, 
            text="Select a game to launch both Pygame and Arcade versions",
            font=self.info_font,
            bg=self.bg_color,
            fg=self.fg_color
        )
        self.info_label.pack(pady=10)
    
    def find_matching_games(self):
        """Find all Python files that exist in both pygame_version and arcade_version folders"""
        pygame_files = []
        arcade_files = []
        
        # Get all .py files in pygame_version
        if os.path.exists("pygame_version"):
            pygame_files = [f[:-3] for f in os.listdir("pygame_version") if f.endswith(".py")]
        
        # Get all .py files in arcade_version
        if os.path.exists("arcade_version"):
            arcade_files = [f[:-3] for f in os.listdir("arcade_version") if f.endswith(".py")]
        
        # Find the common games (files with same name in both directories)
        common_games = sorted(list(set(pygame_files) & set(arcade_files)))
        
        # Format game names for display (convert snake_case to Title Case)
        formatted_games = [game.replace("_", " ").title() for game in common_games]
        
        # Return both the formatted names (for display) and original filenames
        return list(zip(formatted_games, common_games))
    
    def launch_game(self, game):
        """Launch both Pygame and Arcade versions of the selected game"""
        display_name, filename = game
        
        # Update info label
        self.info_label.config(text=f"Launching {display_name}...")
        self.root.update()
        
        try:
            # Create threads for running each version
            pygame_thread = threading.Thread(
                target=self.run_game,
                args=("pygame_version", filename)
            )
            
            arcade_thread = threading.Thread(
                target=self.run_game,
                args=("arcade_version", filename)
            )
            
            # Start both threads
            pygame_thread.start()
            arcade_thread.start()
            
            # Update info label
            self.info_label.config(text=f"Running {display_name} - Close game windows to return")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch {display_name}: {str(e)}")
            self.info_label.config(text="Select a game to launch both Pygame and Arcade versions")
    
    def run_game(self, directory, filename):
        """Run a specific game file in a separate process"""
        try:
            # Get the path to the game file
            game_path = os.path.join(directory, f"{filename}.py")
            
            # Use the current Python interpreter to run the game
            subprocess.run([sys.executable, game_path], check=True)
            
        except subprocess.CalledProcessError:
            # Game was closed or crashed
            pass
        except Exception as e:
            # Other error occurred
            print(f"Error running {filename} in {directory}: {str(e)}")

def main():
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()

if __name__ == "__main__":
    main() 