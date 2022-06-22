import keyboard
from Board import Board


class Maze:

    def __init__(self, height=15, width=14):
        """Maze constructor"""
        board_class = Board()
        self.height = height
        self.width = width
        self.board = board_class.grab_board(height, width)
        self.x = 0
        self.y = 0
        self.finish = (self.height-1, self.width-1)
        self.position = (self.x, self.y)
        self.player_position = self.board[self.x][self.y]

    def movement(self):
        """Movement of player through maze (Run through GUI)"""

        while self.x != self.height-1 and self.y != self.width-1:
            while True:
                user_input = keyboard.read_event(suppress=False)
                if user_input.name == "esc" and user_input.event_type == "down":
                    break
                elif user_input.event_type == "down":

                    # Up movement
                    if keyboard.is_pressed("up"):
                        if self.player_position == 3:
                            pass
                        elif self.player_position == 6:
                            pass
                        elif self.player_position == 7:
                            pass
                        elif self.player_position == 10:
                            pass
                        elif self.player_position == 12:
                            pass
                        elif self.player_position == 13:
                            pass
                        elif self.player_position == 14:
                            pass
                        else:
                            print("up")
                            self.player_position = self.board[self.x - 1][self.y]
                            self.x -= 1

                    # Down movement
                    elif keyboard.is_pressed("down"):
                        if self.player_position == 3:
                            pass
                        elif self.player_position == 4:
                            pass
                        elif self.player_position == 5:
                            pass
                        elif self.player_position == 11:
                            pass
                        elif self.player_position == 12:
                            pass
                        elif self.player_position == 13:
                            pass
                        elif self.player_position == 15:
                            pass
                        else:
                            print("down")
                            self.player_position = self.board[self.x + 1][self.y]
                            self.x += 1

                    # Right movement
                    elif keyboard.is_pressed("right"):
                        if self.player_position == 2:
                            pass
                        elif self.player_position == 5:
                            pass
                        elif self.player_position == 6:
                            pass
                        elif self.player_position == 8:
                            pass
                        elif self.player_position == 12:
                            pass
                        elif self.player_position == 14:
                            pass
                        elif self.player_position == 15:
                            pass
                        else:
                            print("right")
                            self.player_position = self.board[self.x][self.y + 1]
                            self.y += 1

                    # Left movement
                    elif keyboard.is_pressed("left"):
                        if self.player_position == 2:
                            pass
                        elif self.player_position == 4:
                            pass
                        elif self.player_position == 7:
                            pass
                        elif self.player_position == 9:
                            pass
                        elif self.player_position == 13:
                            pass
                        elif self.player_position == 14:
                            pass
                        elif self.player_position == 15:
                            pass
                        else:
                            print("left")
                            self.player_position = self.board[self.x][self.y - 1]
                            self.y -= 1
