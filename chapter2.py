import random

class Chapter2:
    def __init__(self):
        self.key_part_found = None
        self.spy_action = None

    def find_key_part(self):
        key_parts = ["part of the diamond", "mysterious gem", "shiny fragment"]
        self.key_part_found = random.choice(key_parts)
        print(f"The team has found the first part of the key: {self.key_part_found}")

    def handle_spy(self):
        self.spy_action = input("Is the spy trying to distract the team? (y/n): ").lower()
        if self.spy_action == "y":
            print("The team talks about the spy's suspicious behavior.")
        else:
            print("The team keeps searching and disabling traps.")

    def play(self):
        self.find_key_part()
        self.handle_spy()
        print("The team discusses their next steps.")
        print("The first key part is secured, and the team is ready to move to Chapter 3.")
        return True

