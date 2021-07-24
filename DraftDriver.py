from Players import*
from Teams import Team
from Draft import*
import string

# This method will have the user select their position in the Draft order
def selectPosition():
    # Valid will be set to True when the User selects a number from 1 to 10
    # Method will exit once the User has selected a valid number
    valid = False
    while not valid:
        myPosition = int(input("Please enter your draft position: "))
        validNumbers = list(range(1, 11))
        if myPosition in validNumbers:
            valid = True
            return myPosition
        else:
            print("Oops! Draft position must be a number from 1 to 10")

# This method will assign the order in which Teams select their players
def assignOrder(playerPosition):
    draftOrder = []
    # Non-User teams will populate the Draft order
    for i in range(9):
        # Team A to to Team I will be added to the Draft order
        draftOrder.append(Team(string.ascii_uppercase[i]))

    # User team will be inserted in their specified Draft position
    draftOrder.insert(playerPosition - 1, Team("Your Team", True))
    print("Here is the draft order: " + str(draftOrder))
    return draftOrder



if __name__ == '__main__':

    print("Welcome to Sergio's DraftHelper\n")

    # Prompts the User to selcted their Draft position
    myPosition = selectPosition()

    # Populates a list to represent the Draft order
    draftOrder = assignOrder(myPosition)

    # Populates the Draft pool using Players.makePool()
    draftPool = makePool()

    # Initiates an instance of the class Draft
    myDraft = Draft(draftOrder, draftPool)

    # Begins the Draft
    myDraft.runDraft()





