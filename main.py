from chapter1 import Chapter1
from chapter2 import Chapter2
from chapter3 import Chapter3
from chapter4 import Chapter4
from chapter5 import Chapter5

class GameState:
    def __init__(self):
        self.current_chapter = 1

    def play_game(self):
        while self.current_chapter == 1:
            chapter1 = Chapter1()
            if chapter1.play():
                self.current_chapter = 2
            else:
                print("Game Over! Try again.")
                break

        while self.current_chapter == 2:
            chapter2 = Chapter2()
            if chapter2.play():
                self.current_chapter = 3
            else:
                print("Game Over! Try again.")
                break

        while self.current_chapter == 3:
            chapter3 = Chapter3()
            if chapter3.play():
                self.current_chapter = 4
            else:
                print("Game Over! Try again.")
                break

        while self.current_chapter == 4:
            chapter4 = Chapter4()
            if chapter4.play():
                self.current_chapter = 5
            else:
                print("Game Over! Try again.")
                break

        while self.current_chapter == 5:
            chapter5 = Chapter5()
            if chapter5.play():
                print("Congratulations! You've completed the game successfully!")
                break
            else:
                print("Game Over. Better luck next time!")
                break

if __name__ == "__main__":
    game = GameState()
    game.play_game()

