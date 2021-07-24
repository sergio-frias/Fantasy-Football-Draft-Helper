from Strategy import*

# This class defines the Draft
# draftOrder defines when a team can select a player
# draftPool provides a list of available players to select
# numRounds defines how many rounds the DraftHelper will account for
# Each round, every team will select one player
class Draft():
    def __init__(self, draftOrder, draftPool, numRounds = 17):
        self.draftOrder = draftOrder
        self.draftPool = draftPool
        self.numRounds = numRounds

        # Initiate the draft at Round 1
        self.round = 1

    # This method will display the top 10 available players to select
    def displayTop10(self):
        print("\nHere are the top 10 available players:")
        stop = 1
        for player in self.draftPool:
            if stop < 11:
                # e.g. of first loop: '1: Christian McCaffrey'
                print(str(stop) + ": " + str(player))
                stop += 1
            else:
                return

    # This method will be called each time a player is selected
    # The player will be added to the respective team's roster
    def assignPlayer(self, player, team):
        if player.position == "QB":
            team.QBs.append(player.name)
        elif player.position == "RB":
            team.RBs.append(player.name)
        elif player.position == "WR":
            team.WRs.append(player.name)
        else:
            team.TEs.append(player.name)
        # After a team selects a player their updated roster will immediately be displayed
        team.displayRoster()

    # This method will prompt the User to enter each player selection
    def selectPlayer(self, team, teamIDX):
        validSelection = False

        # Method will not return until a valid player has been selected
        while not validSelection:
            selection = (input("\nEnter the name of the player that " + str(self.draftOrder[teamIDX]) + \
                               " selected, then press enter: "))
            for player in range(len(self.draftPool)):
                # Checks to see if User input matches an available player
                if self.draftPool[player].name == selection:
                    # Adds valid selection to respective team
                    self.assignPlayer(self.draftPool[player], team)
                    # Removes selection from pool of available players
                    self.draftPool.pop(player)
                    # Runs an assessment of User team after they select a player
                    if team.yourTeam:
                        Strategy.runAssessment(self, team, self.round)
                    return
            print("The player you entered is invalid!")
            print("Please enter a valid player selection")

    def snakeOrder(self):
        for i in range(len(self.draftOrder)):
            # Prints the current round and pick number, e.g. 'Round 1: Pick 1:
            print("\nRound: " + str(self.round) + ", " + "Pick: " + str(i + 1))
            # Prints the name of the team who is currently selecting, e.g. 'Team A is on the clock'
            print(str(self.draftOrder[i]) + " is on the clock")
            self.displayTop10()
            self.selectPlayer(self.draftOrder[i], i)
        # reverses the draft order for each round
        self.draftOrder.reverse()

    # initiates the first selection
    def runDraft(self):
        for r in range(1, self.numRounds+1):
            # Updates the draft strategy after each round
            Strategy.roundUpdate(self, r)
            self.snakeOrder()
            self.round += 1


