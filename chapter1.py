import random

class Chapter1:
    def __init__(self):
        self.team_roles = []
        self.suspicious_activity = False

    def assign_roles(self):
        roles = ["Warrior", "Artist", "Engineer", "Explorer", "Spy"]
        self.team_roles = random.sample(roles, len(roles))
        print("The team has arrived in a magical world.")
        print("Roles assigned:")
        for role in self.team_roles:
            print(f"- {role}")

    def investigate(self):
        print("\nThe team discusses how to find the key parts needed for their journey.")
        decision = input("Do you notice anything suspicious in your surroundings? (y/n): ").lower()
        if decision == "y":
            print("The team decides to investigate further.")
            print("All clues collected. Moving to Chapter 2.")
            return True
        else:
            print("The team continues searching for clues to move forward.")
            return False

    def play(self):
        self.assign_roles()
        return self.investigate()

