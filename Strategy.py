
class Strategy:
    # This class will provide updates to player rankings based on 2 factors
    # Factor 1: Players available relative to their positional tier
    # Factor 2: Positions of need relative to the User Team's Roster

    def roundUpdate(self, round):
        if round == 1:
            Strategy.R1toR2(self)
        elif round == 3:
            Strategy.R3toR4(self)
        elif round == 5:
            Strategy.R5toR6(self)
        else:
            return

    def R1toR2(self):
        for x in self.draftPool:
            if x.position == "QB":
                x.rating = (round(x.rating * 0.9, 3))
            elif x.position == "RB":
                x.rating = (round(x.rating * 1.05, 3))
            elif x.position == "WR":
                x.rating = (round(x.rating * 1.03, 3))
        self.draftPool = sorted(self.draftPool, reverse=True, key=lambda player: player.rating)

    def R3toR4(self):
        for x in self.draftPool:
            if x.position == "QB":
                x.rating = (round(x.rating * 1.05, 3))
        self.draftPool = sorted(self.draftPool, reverse=True, key=lambda player: player.rating)

    def R5toR6(self):
        for x in self.draftPool:
            if x.position == "QB":
                x.rating = (round(x.rating * 1.05, 3))
            elif x.position == "RB":
                x.rating = (round(x.rating * 0.97, 3))
            elif x.position == "WR":
                x.rating = (round(x.rating * 0.98, 3))
        self.draftPool = sorted(self.draftPool, reverse=True, key=lambda player: player.rating)


    def runAssessment(self, team, round):
        if round == 2:
            Strategy.R2(self, team)
        elif round == 3:
            Strategy.R3(self, team)
        elif round == 4:
            Strategy.R4(self, team)
        else:
            return


    def R2(self, team):
        if len(team.RBs) == 0:
            for x in self.draftPool:
                if x.position == "RB":
                    x.rating = (round(x.rating *1.05, 3))
        else:
            for x in self.draftPool:
                if x.position == "RB":
                    x.rating = (round(x.rating / 1.05, 3))

        if len(team.WRs) == 0:
            for x in self.draftPool:
                if x.position == "WR":
                    x.rating = (round(x.rating *1.03, 3))
        self.draftPool = sorted(self.draftPool, reverse=True, key=lambda player: player.rating)

    def R3(self, team):
        if len(team.RBs) == 0:
            for x in self.draftPool:
                if x.position == "RB":
                    x.rating = (round(x.rating *1.05, 3))
        elif len(team.RBs) == 2:
            for x in self.draftPool:
                if x.position == "RB":
                    x.rating = (round(x.rating * 0.9, 3))
        if len(team.WRs) == 1:
            for x in self.draftPool:
                if x.position == "WR":
                    x.rating = (round(x.rating * 0.9, 3))
        if len(team.WRs) == 2:
            for x in self.draftPool:
                if x.position == "WR":
                    x.rating = (round(x.rating * 0.85, 3))
        elif len(team.WRs) == 0:
            for x in self.draftPool:
                if x.position == "WR":
                    x.rating = (round(x.rating *1.03, 3))
        self.draftPool = sorted(self.draftPool, reverse=True, key=lambda player: player.rating)

    def R4(self, team):
        if len(team.RBs) == 3:
            for x in self.draftPool:
                if x.position == "RB":
                    x.rating = (round(x.rating * 0.9, 3))

        if len(team.WRs) == 0:
            for x in self.draftPool:
                if x.position == "WR":
                    x.rating = (round(x.rating *1.03, 3))
        self.draftPool = sorted(self.draftPool, reverse=True, key=lambda player: player.rating)
