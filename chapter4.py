import random

class Chapter4:
    def __init__(self):
        self.third_key_part = None
        self.spy_behavior = None

    def search_key_part(self):
        key_parts = ["part of the diamond", "mysterious gem", "shiny fragment"]
        self.third_key_part = random.choice(key_parts)
        print("The team searches for the hidden third part of the key.")
        print(f"The hidden key part found: {self.third_key_part}")

    def observe_spy_behavior(self):
        self.spy_behavior = input("Do you notice the spy's weird behavior? (y/n): ").lower()
        if self.spy_behavior == "y":
            print("The team discusses the spy's secret actions.")
        else:
            print("The team keeps protecting the key parts without realizing the spy's intentions.")

    def play(self):
        self.search_key_part()
        self.observe_spy_behavior()
        print("The key collection is now complete.")
        print("The team is ready to activate the key and move forward to Chapter 5.")
        return True
