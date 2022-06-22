import keyboard
from Maze import Maze

# Not needed for Gui

maze = Maze()

while True:
    user_input = keyboard.read_event(suppress=False)
    if user_input.name == "esc" and user_input.event_type == "down":
        break
    if user_input.event_type == "down":
        maze.movement()
