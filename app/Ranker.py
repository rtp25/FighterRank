from app.DB_Connection import DB_Connection
from operator import itemgetter


class Ranker:
    conn = DB_Connection()

    # ==========================================================================
    def __init__(self):
        self.fighters_dict = dict()
        self.fighters_list = [[0 for x in range(2)] for y in range(11)]

    # ==========================================================================
    def calculateRank(self, wc, name):
        win_ratio = self.getWinRatio(wc, name)
        wins = self.conn.getFighterWins(wc, name)
        kos = self.conn.getFighterKOs(wc, name)
        subs = self.conn.getFighterSubs(wc, name)
        decs = self.conn.getFighterDecs(wc, name)
        str_accur = self.conn.getFighterStrAccur(wc, name)
        grp_accur = self.conn.getFighterGrpAccur(wc, name)
        rank = win_ratio + (kos/wins) * 0.4 + (subs/wins) * 0.4 + (decs/wins) * .2 + str_accur + grp_accur
        return rank

    # ==========================================================================
    def displayRankedFighters(self, wc):
        ranked_fighters  = self.rankFighters(wc)

        for i in range(11):
            print(ranked_fighters[i])

    # adds all fighters from a weight class to list and returns the list as a table with rankings
    # ==========================================================================
    def addFighters(self, wc):
        fighters_wc = self.conn.getAllFightersFromWeight(wc)
        x = 0
        for row in fighters_wc:
            fighter_name = self.conn.getFighterName(wc, row.get('name'))
            rank = self.calculateRank(wc, fighter_name)
            self.fighters_list[x] = (fighter_name, rank)
            x = x + 1
        return self.fighters_list

    # adds single fighter from a weight class to list and returns the list as a table with the fighter rank
    # ==========================================================================
    def addFighter(self, wc, name):
        a_fighter = self.conn.getFighter(wc, name)
        x = 0
        for row in a_fighter:
            fighter_name = self.conn.getFighterName(wc, row.get('name'))
            rank = self.calculateRank(wc, fighter_name)
            self.fighters_list[x] = (fighter_name, rank)
            x = x + 1
        return self.fighters_list

    # ==========================================================================
    def add_fighter_by_name(self, name):

        try:
            a_fighter, wc = self.conn.get_fighter_by_name(name)
            x = 0
            for row in a_fighter:
                fighter_name = self.conn.getFighterName(wc, row.get('name'))
                rank = self.calculateRank(wc, fighter_name)
                self.fighters_list[x] = (fighter_name, rank)
                x = x + 1
            return self.fighters_list
        except TypeError:
            print("That fighter does not exist in the database!")

    # ==========================================================================
    def rankFighters(self, wc):
        fighters = self.addFighters(wc)
        fighters.sort(key=itemgetter(1), reverse=True)
        return fighters

    # ==========================================================================
    def getWinRatio(self, wc, name):
        wins = self.conn.getFighterWins(wc, name)
        losses = self.conn.getFighterLosses(wc, name)
        win_ratio = wins / (wins + losses)
        return win_ratio

