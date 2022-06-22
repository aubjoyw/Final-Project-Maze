import keyboard
import copy
from Board import Board


class Maze:

    def __init__(self, height=15, width=14):
        """Maze constructor"""
        board_class = Board()
        self.height = height
        self.width = width
        self.board = [[7, 3, 12, 13, 10, 3, 3, 3, 3, 3, 3, 3, 3, 12],
                      [2, 7, 3, 3, 11, 3, 12, 13, 3, 3, 3, 3, 10, 6],
                      [2, 2, 7, 3, 3, 3, 6, 7, 3, 3, 3, 6, 2, 2],
                      [2, 2, 2, 7, 3, 10, 5, 9, 3, 12, 14, 2, 2, 2],
                      [2, 2, 2, 9, 6, 4, 3, 5, 13, 6, 2, 9, 8, 2],
                      [2, 2, 15, 2, 4, 6, 7, 3, 3, 1, 8, 2, 15, 2],
                      [4, 8, 14, 2, 7, 5, 9, 6, 14, 2, 2, 2, 14, 2],
                      [14, 2, 2, 2, 9, 6, 9, 1, 8, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 15, 2, 9, 5, 2, 2, 15, 9, 5, 2],
                      [2, 2, 2, 2, 14, 4, 5, 13, 11, 8, 14, 2, 7, 8],
                      [2, 2, 2, 2, 9, 3, 10, 3, 12, 15, 2, 2, 2, 2],
                      [2, 2, 2, 15, 2, 13, 11, 3, 3, 6, 4, 8, 2, 2],
                      [2, 2, 4, 3, 11, 3, 10, 3, 12, 4, 6, 15, 2, 15],
                      [2, 4, 3, 3, 3, 10, 11, 12, 7, 3, 11, 3, 5, 14],
                      [4, 3, 3, 3, 3, 5, 13, 3, 11, 3, 3, 3, 3, 5]]
        self.board = board_class.grab_board(height, width)
        self.x = 0
        self.y = 0
        self.finish = (self.height-1, self.width-1)
        self.position = (self.x, self.y)
        self.player_position = self.board[self.x][self.y]

    def movement(self):
        """Movement of player through maze"""

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
