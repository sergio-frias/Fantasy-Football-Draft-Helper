class Player:
    # This class defines the Players that are available to select

    # Each player is defined by their name, position, rating, and tier
    # Players at the same position with similar ratings will share the same tier
    def __init__(self, name, position, rating, tier):
        self.name = name
        self.position = position
        self.rating = rating
        self.tier = tier

    # This method will be called on to print the player's name, position, and rating
    def __repr__(self):
        return self.name + ', ' + self.position + ', ' + str(self.rating)
        # Example of how function will return:
        # Alvin Kamara, RB, 99.9

# This method will populate the pool of available players along with their attributes
def makePool():
    pool = []
    pool.append(Player("Christian McCaffrey", "RB", 99.9, 1))
    pool.append(Player("Saquon Barkley", "RB", 99.5, 1))
    pool.append(Player("Ezekiel Elliot", "RB", 99, 1))
    pool.append(Player("Derrick Henry", "RB", 99, 1))
    pool.append(Player("Miles Sanders", "RB", 95, 2))
    pool.append(Player("Josh Jacobs", "RB", 94.5, 2))
    pool.append(Player("Dalvin Cook", "RB", 94, 2))
    pool.append(Player("Joe Mixon", "RB", 94, 2))
    pool.append(Player("Michael Thomas", "WR", 94, 1))
    pool.append(Player("Clyde Edwards Helaire", "RB", 93, 2))
    pool.append(Player("Austin Ekeler", "RB", 93, 2))
    pool.append(Player("Kenyan Drake", "RB", 93, 2))
    pool.append(Player("Nick Chubb", "RB", 93, 1))
    pool.append(Player("Davante Adams", "WR", 93.5, 1))
    pool.append(Player("Tyreek Hill", "WR", 93, 1))
    pool.append(Player("Julio Jones", "WR", 93, 1))
    pool.append(Player("Alvin Kamara", "RB", 89, 3))
    pool.append(Player("Aaron Jones", "RB", 88, 3))
    pool.append(Player("Travis Kelce", "TE", 89, 1))
    pool.append(Player("Chris Godwin", "WR", 89, 2))
    pool.append(Player("Lamar Jackson", "QB", 89, 1))
    pool.append(Player("DeAndre Hopkins", "WR", 88, 2))
    pool.append(Player("DJ Moore", "WR", 88, 2))
    pool.append(Player("Adam Thielen", "WR", 88, 2))
    pool.append(Player("George Kittle", "TE", 88, 1))
    pool.append(Player("Allen Robinson II", "WR", 87, 2))
    pool.append(Player("Mike Evans", "WR", 86, 2))
    pool.append(Player("Kenny Golladay", "WR", 86, 2))
    pool.append(Player("Chris Carson", "RB", 82, 3))
    pool.append(Player("James Conner", "RB", 81, 3))
    pool.append(Player("Robert Woods", "WR", 85, 2))
    pool.append(Player("Amari Cooper", "WR", 85, 2))
    pool.append(Player("AJ Brown", "WR", 85, 2))
    pool.append(Player("Mark Andrews", "TE", 85, 2))
    pool.append(Player("Patrick Mahomes", "QB", 85, 2))
    pool.append(Player("Melvin Gordon III", "RB", 80, 3))
    pool.append(Player("DJ Chark Jr", "WR", 80, 3))
    pool.append(Player("Terry McLaurin", "WR", 80, 3))
    pool.append(Player("Tyler Lockett", "WR", 80, 3))
    pool.append(Player("Calvin Ridley", "WR", 80, 3))
    pool.append(Player("Cooper Kupp", "WR", 80, 3))
    pool.append(Player("Jonathan Taylor", "RB", 75, 4))
    pool.append(Player("Cam Akers", "RB", 74, 4))
    pool.append(Player("Odell Beckham Jr", "WR", 79, 3))
    pool.append(Player("Juju Smith-Schuster", "WR", 78, 3))
    pool.append(Player("Stefon Diggs", "WR", 78, 3))
    pool.append(Player("DK Metcalf", "WR", 78, 3))
    pool.append(Player("Kareem Hunt", "RB", 73, 4))
    pool.append(Player("Darren Waller", "TE", 80, 3))
    pool.append(Player("Tyler Boyd", "WR", 77, 3))
    pool.append(Player("Courtland Sutton", "WR", 70, 4))
    pool.append(Player("DeVante Parker", "WR", 70, 4))
    pool.append(Player("Marquise Brown", "WR", 70, 4))
    pool.append(Player("Dak Prescott", "QB", 80, 3))
    pool.append(Player("Kyler Murray", "QB", 79, 3))
    pool.append(Player("Deshaun Watson", "QB", 78, 3))
    pool.append(Player("Russell Wilson", "QB", 77, 3))
    pool.append(Player("Keenan Allen", "WR", 70, 4))
    pool.append(Player("Julian Edelman", "WR", 70, 4))
    pool.append(Player("Zach Ertz", "TE", 75, 4))
    pool.append(Player("D'Andre Swift", "RB", 68, 5))
    pool.append(Player("James White", "RB", 67, 5))
    pool.append(Player("Raheem Mostert", "RB", 66, 5))
    pool.append(Player("Le'Veon Bell", "RB", 65, 5))
    pool.append(Player("Leonard Fournette", "RB", 64, 5))
    pool.append(Player("Todd Gurley", "RB", 63, 5))
    pool.append(Player("Zack Moss", "RB", 62, 5))
    pool.append(Player("Jared Cook", "TE", 65, 5))
    pool.append(Player("JK Dobbins", "RB", 61, 5))
    pool.append(Player("Michael Gallup", "WR", 65, 5))
    pool.append(Player("Antonio Gibson", "RB", 60, 5))
    pool.append(Player("TY Hilton", "WR", 64, 5))
    pool.append(Player("Deebo Samuel", "WR", 63, 5))
    pool.append(Player("Dionate Johnson", "WR", 63, 5))
    pool.append(Player("Christian Kirk", "WR", 63, 5))
    pool.append(Player("Devin Singletary", "RB", 55, 6))
    pool.append(Player("Phillip Lindsay", "RB", 55, 6))
    pool.append(Player("Tevin Coleman", "RB", 55, 6))
    pool.append(Player("Jarvis Landry", "WR", 62, 5))
    pool.append(Player("Brandin Cooks", "WR", 61, 5))
    pool.append(Player("DeSean Jackson", "WR", 60, 5))
    pool.append(Player("Carson Wentz", "QB", 65, 4))
    pool.append(Player("Matt Ryan", "QB", 64, 4))
    pool.append(Player("Cam Newton", "QB", 63, 4))
    pool.append(Player("Tyler Higbee", "TE", 60, 6))
    pool.append(Player("Josh Allen", "QB", 62, 4))
    pool.append(Player("Mark Ingram", "RB", 50, 7))
    pool.append(Player("Matt Breida", "RB", 50, 7))
    pool.append(Player("Marvin Jones Jr", "WR", 55, 6))
    pool.append(Player("Will Fuller V", "WR", 54, 6))
    pool.append(Player("Hayden Hurst", "TE", 58, 6))
    pool.append(Player("Tom Brady", "QB", 55, 7))
    pool.append(Player("Matthew Stafford", "QB", 54, 7))
    pool.append(Player("Chris Herndon", "TE", 57, 6))
    pool.append(Player("TJ Hockenson", "TE", 57, 6))
    pool.append(Player("Jamison Crowder", "WR", 53, 6))
    pool.append(Player("Sterling Shepard", "WR", 52, 6))
    pool.append(Player("Drew Brees", "QB", 53, 7))
    pool.append(Player("Henry Ruggs III", "WR", 51, 6))
    pool.append(Player("Austin Hooper", "TE", 56, 6))

    # Sorts the pool of players by their ranking, greatest to least
    pool = sorted(pool, reverse=True, key=lambda player: player.rating)

    return pool



if __name__ == "__main__":
    print(makePool())