import pygame
from game import Game
from intro import intro


class State_Manager:
    def __init__(self, display):
        self.state = []
        self.run = True
        self.intro_state = intro(display, 640, 400)
        self.game_state = Game(display, 640, 400)



    def change_state(self, state):
        self.state.pop()
        self.state.insert(state)

    def running_states(self):
        self.intro_state.main()




