class Chapter5:
    def __init__(self):
        self.portal_activated = False
        self.spy_stopped = False

    def activate_portal(self):
        print("The team has gathered all key parts and is now activating the portal.")
        decision = input("Is the portal successfully activated? (y/n): ").lower()
        if decision == "y":
            self.portal_activated = True
            print("The portal is activated successfully.")
        else:
            self.portal_activated = False
            print("The portal activation failed.")

    def stop_spy(self):
        self.spy_stopped = input("Was the spy stopped? (y/n): ").lower() == "y"
        if self.spy_stopped:
            print("The spy was stopped, and the mission was a success!")
        else:
            print("Mission failed! The spy interfered.")

    def play(self):
        self.activate_portal()
        self.stop_spy()
        if self.spy_stopped and self.portal_activated:
            print("Success: The team has completed the mission and saved the day!")
            return True
        else:
            print("Mission failed. The team must face the consequences of the spy's interference.")
            return False
