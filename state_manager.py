import pygame
from game import Game
from intro import intro


class State_Manager:

    def __init__(self, display):
        self.state = []
        self.run = True
        self.intro_state = intro(display, 600, 400)
        self.game_state = Game(display, 600, 400)

    print()


    def change_state(self, state):
        self.state.pop()
        self.state.insert(state)

    def running_states(self):
        print(self.intro_state.state)
        print(self.game_state.state)


state_m = State_Manager(display="bla")
state_m.running_states()
