#!/usr/bin/env python3
import random
import string
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

GameElements = {'moves': ['rock', 'paper', 'scissors'],
                'GameModes': ['random', 'reflect', 'cycle']}

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def __init__(self):
        self.my_move = None
        self.their_move = None
        self.score = 0
        self.cycle = 0
        self.lenMoves = len(GameElements['moves'])
        self.playerName = None
        self.rounds = 0
        self.roundsInpCheck = False
        self.GameMode = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class ReflectPlayer(Player):
    def move(self):
        if not self.their_move:
            return random.choice(GameElements['moves'])
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        return GameElements['moves'][self.cycle]


class RandomPlayer(Player):
    def move(self):
        return random.choice(GameElements['moves'])


class HumanPlayer(Player):
    def move(self):
        move = input("Rock, Paper or Scissors? > ")
        move = move.lower()
        while move not in GameElements['moves']:
            if move == "":
                move = input("\nRock, Paper or Scissors? > ")
                move = move.lower()
                print("\n")
            else:
                move = input(f"Invalid Input: '{move}', try again. > ")
                move = move.lower()
                print("\n")
        return move.lower()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):

        self.p1 = RandomPlayer()
        self.p2 = HumanPlayer()
        print(f"Please choose one game mode: {GameElements['GameModes']}")
        self.p2.GameMode = input("Game mode: > ")
        self.p2.GameMode = self.p2.GameMode.lower()

        while self.p2.GameMode not in GameElements['GameModes']:
            if self.p2.GameMode == "":
                self.p2.GameMode = input("Choose one game mode. > ")
                self.p2.GameMode = self.p2.GameMode.lower()
                print("\n")
            else:
                self.p2.GameMode = input(f"Invalid Input, try again. > ")
                self.p2.GameMode = self.p2.GameMode.lower()
                print("\n")

        if self.p2.GameMode == 'random':
            self.p1 = RandomPlayer()
        elif self.p2.GameMode == 'reflect':
            self.p1 = ReflectPlayer()
        else:
            self.p1 = CyclePlayer()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        p1Name = self.p1.playerName
        p2Name = self.p2.playerName

        if beats(move1, move2) is True:
            print(f"\n** {p1Name} WON. **")
            print(f"{p2Name}: '{move2}'\t{p1Name}: '{move1}'")
            self.p1.score += 1
        elif move1 == move2:
            print("\n** DRAW **")
            print(f"{p2Name}: '{move2}'\t{p1Name}: '{move1}'")
        else:
            print(f"** {self.p2.playerName} WON. **")
            print(f"{p2Name}: '{move2}'\t{p1Name}: '{move1}'")
            self.p2.score += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        p1Name = self.p1.playerName
        p2Name = self.p2.playerName
        p1Score = self.p1.score
        p2Score = self.p2.score

        print("\nLet's play Rock, Paper or Scissors!")

        self.p2.playerName = input("Please enter your name. > ")
        self.p1.playerName = input("Who would you like to play with? > ")
        self.p2.rounds = input("How many rounds would you like to play? > ")

        while self.p2.roundsInpCheck is False:
            try:
                int(self.p2.rounds) + 1
                int(self.p2.rounds) - 1
                self.p2.roundsInpCheck = True

            except ValueError:
                self.p2.rounds = input("Please enter a valid number. > ")

        for round in range(1, int(self.p2.rounds) + 1):
            print(f"Round {round}:")
            self.play_round()
            print(f"{p1Name}: {p2Score}\t{p2Name}: {p2Score}")
            print("-----------------------------\n")

            if self.p1.cycle <= self.p1.lenMoves - 2:
                self.p1.cycle += 1
            else:
                self.p1.cycle = 0

        if self.p1.score > self.p2.score:
            print(f"++{self.p1.playerName} won the Game!++")
            print(f"Total Score: {self.p2.score}x{self.p1.score}")
        elif self.p1.score == self.p2.score:
            print("** IT'S A DRAW **")
            print(f"Total Score: {self.p2.score}x{self.p1.score}")
        else:
            print(f"** {self.p2.playerName} WON THE GAME **")
            print(f"Total Score: {self.p2.score} x {self.p1.score}\n")

        print("Thank you for playing my first Python game!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
