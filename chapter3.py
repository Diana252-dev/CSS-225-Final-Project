import random

class Chapter3:
    def __init__(self):
        self.broken_equipment = None
        self.equipment_fixed = False
        self.spy_behavior = None

    def find_broken_equipment(self):
        key_parts = ["part of the diamond", "mysterious gem", "shiny fragment"]
        self.broken_equipment = random.choice(key_parts)
        print(f"The team has found some broken equipment, and inside it, they find the second key part: {self.broken_equipment}")

    def fix_equipment(self):
        print("The team begins to fix the equipment.")
        decision = input("Is the equipment fixed? (y/n): ").lower()
        if decision == "y":
            self.equipment_fixed = True
            print("The equipment is successfully fixed.")
        else:
            self.equipment_fixed = False
            print("The equipment remains broken.")

    def observe_spy_behavior(self):
        self.spy_behavior = input("Do you notice the spy's weird behavior? (y/n): ").lower()
        if self.spy_behavior == "y":
            print("The team starts doubting the spy's intentions.")
        else:
            print("The team remains unaware of the spy's actions.")

    def play(self):
        self.find_broken_equipment()
        self.fix_equipment()
        self.observe_spy_behavior()
        print("The team moves forward, ready to continue their journey.")
        print("The second key part is secured, and the team is ready to go to Chapter 4.")
        return True
