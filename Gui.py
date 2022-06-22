import tkinter as tk
import keyboard
from PIL import ImageTk, Image
from Maze import Maze


class Gui:

    def __init__(self):
        """GUI constructor"""

        # Maze backend
        self.maze = Maze()

        # Basic setup
        self.window = tk.Tk()
        self.window.wm_title("Maze")
        self.window.geometry("600x400")

        # Frames
        self.menu_frame = tk.Frame(master=self.window, height=400, width=100, relief="raised")
        self.menu_frame.pack(side="left")

        self.game_frame = tk.Frame(master=self.window, height=600, width=700, relief="raised", bg="gray46")
        self.game_frame.pack(side="left", padx=75)

        # Menu frame
        menu_title = tk.Label(master=self.menu_frame, text="Complete this maze\n to receive a cat pic!", font="Arial, 12")
        menu_title.pack()
        self.play_game_button = tk.Button(master=self.menu_frame, text="Play Game", bg="cyan2", command=self.play_game)
        self.play_game_button.pack()

    def create_board(self, position):
        for element in self.game_frame.winfo_children():
            element.destroy()
        for x in range(self.maze.height):
            for y in range(self.maze.width + 1):
                if y == self.maze.width:
                    canvas = tk.Canvas(master=self.game_frame, width=4, height=20, bg="black", borderwidth=0, bd=-2)
                    canvas.grid(row=x, column=y)
                else:
                    canvas = tk.Canvas(master=self.game_frame, width=20, height=20, bg="white", borderwidth=0, bd=-2)
                    canvas.grid(row=x, column=y)
                    if self.maze.board[x][y] == 2:
                        # right
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                        # left
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                    elif self.maze.board[x][y] == 3:
                        # up
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                        # down
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 4:
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 5:
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 6:
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 7:
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                    elif self.maze.board[x][y] == 8:
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 9:
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                    elif self.maze.board[x][y] == 10:
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                    elif self.maze.board[x][y] == 11:
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 12:
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                    elif self.maze.board[x][y] == 13:
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                    elif self.maze.board[x][y] == 14:
                        canvas.create_rectangle(0, 0, 21, 1, fill="black")
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                    elif self.maze.board[x][y] == 15:
                        canvas.create_rectangle(20, 0, 21, 21, fill="black")
                        canvas.create_rectangle(0, 18, 21, 21, fill="black")
                        canvas.create_rectangle(0, 0, 3, 21, fill="black")
                    if position == (x, y):
                        canvas.create_oval(4, 2, 19, 18, fill="red")
        self.game_frame.pack()

    def movement(self):
        while True:
            user_input = keyboard.read_event(suppress=False)
            if user_input.event_type == "down":
                # Up movement
                if keyboard.is_pressed("up"):
                    if self.maze.player_position == 3:
                        pass
                    elif self.maze.player_position == 6:
                        pass
                    elif self.maze.player_position == 7:
                        pass
                    elif self.maze.player_position == 10:
                        pass
                    elif self.maze.player_position == 12:
                        pass
                    elif self.maze.player_position == 13:
                        pass
                    elif self.maze.player_position == 14:
                        pass
                    else:
                        print("up")
                        self.maze.player_position = self.maze.board[self.maze.x - 1][self.maze.y]
                        self.maze.x -= 1
                        break
                # Down movement
                elif keyboard.is_pressed("down"):
                    if self.maze.player_position == 3:
                        pass
                    elif self.maze.player_position == 4:
                        pass
                    elif self.maze.player_position == 5:
                        pass
                    elif self.maze.player_position == 11:
                        pass
                    elif self.maze.player_position == 12:
                        pass
                    elif self.maze.player_position == 13:
                        pass
                    elif self.maze.player_position == 15:
                        pass
                    else:
                        print("down")
                        self.maze.player_position = self.maze.board[self.maze.x + 1][self.maze.y]
                        self.maze.x += 1
                        break
                # Right movement
                elif keyboard.is_pressed("right"):
                    if self.maze.player_position == 2:
                        pass
                    elif self.maze.player_position == 5:
                        pass
                    elif self.maze.player_position == 6:
                        pass
                    elif self.maze.player_position == 8:
                        pass
                    elif self.maze.player_position == 12:
                        pass
                    elif self.maze.player_position == 14:
                        pass
                    elif self.maze.player_position == 15:
                        pass
                    else:
                        print("right")
                        self.maze.player_position = self.maze.board[self.maze.x][self.maze.y + 1]
                        self.maze.y += 1
                        break
                # Left movement
                elif keyboard.is_pressed("left"):
                    if self.maze.player_position == 2:
                        pass
                    elif self.maze.player_position == 4:
                        pass
                    elif self.maze.player_position == 7:
                        pass
                    elif self.maze.player_position == 9:
                        pass
                    elif self.maze.player_position == 13:
                        pass
                    elif self.maze.player_position == 14:
                        pass
                    elif self.maze.player_position == 15:
                        pass
                    else:
                        print("left")
                        self.maze.player_position = self.maze.board[self.maze.x][self.maze.y - 1]
                        self.maze.y -= 1
                        break
        position = (self.maze.x, self.maze.y)
        return position

    def play_game(self):
        """Allows player to move through maze and issues reward"""
        movement = (self.movement())
        if movement == self.maze.finish:
            for element in self.game_frame.winfo_children():
                element.destroy()
            image_canvas = tk.Canvas(master=self.game_frame, width=500, height=600)
            cat = ImageTk.PhotoImage(Image.open("cat.png"))
            image_canvas.create_image(10, 10, anchor="nw", image=cat)
            image_canvas.image = cat
            image_canvas.pack()
        else:
            self.create_board(movement)


if __name__ == "__main__":
    gui = Gui()
    maze = Maze()
    position = (maze.x, maze.y)
    gui.create_board(position)
    tk.mainloop()
