class Team:
    # This class defines the Teams that will be selecting Players

    # Each team is defined by their team name
    # yourTeam is only True for the user team
    def __init__(self, name = 'Your Team', yourTeam = False):

        # This attribute will only be True for the user team
        self.yourTeam = yourTeam

        # User team name will be 'Your Team', assigned by DraftDriver
        if self.yourTeam:
            self.name = name
        else:
            # Non-User teams will be given letter names, e.g. 'Team A'
            self.name = 'Team ' + name

        # Each team will contain a list of their players at each position
        self.QBs = []
        self.RBs = []
        self.WRs = []
        self.TEs = []

    # This method will be used to print the team's name
    def __repr__(self):
        return self.name

    # This method will be used to print the team's name and roster
    # The roster will be categorized by position
    def displayRoster(self):
        print(self.name + " Roster:")
        print("QBs: " + str(self.QBs))
        print("RBs: " + str(self.RBs))
        print("WRs: " + str(self.WRs))
        print("TEs: " + str(self.TEs))

