import pymysql


class DB_Connection:
    _conn = None

    # ==========================================================================
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "newmysqlpass66"
        db = "mma_db"

        self.con = pymysql.connect(host=host, user=user,
                                   password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    # ==========================================================================
    def getResult(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        return [it[0] for it in cur.description], list(cur)

    # ==========================================================================
    def getFighter(self, wc, name):
        db_query = "SELECT * FROM " + wc + " WHERE name='" + name + "'";
        self.cur.execute(db_query)
        result = self.cur.fetchall()
        #print(result[0].get("name"))
        # print (row.get('id'), row.get('name'))
        return result

    # ==========================================================================
    def get_fighter_by_name(self, name):
        fighter = self.get_fighter_by_name_fw(name)
        if len(fighter) > 0:
            wc = 'fw'
            return fighter, wc

        fighter = self.get_fighter_by_name_lw(name)
        if len(fighter) > 0:
            wc = 'lw'
            return fighter, wc

        fighter = self.get_fighter_by_name_ww(name)
        if len(fighter) > 0:
            wc = 'ww'
            return fighter, wc

        fighter = self.get_fighter_by_name_mw(name)
        if len(fighter) > 0:
            wc = 'mw'
            return fighter, wc

        #print(result[0].get("name"))
        #print(row.get('id'), row.get('name'))

    # ==========================================================================
    def get_fighter_by_name_fw(self, name):
        db_query = "SELECT * FROM fw WHERE name='" + name + "'";
        self.cur.execute(db_query)
        result = self.cur.fetchall()
        return result

    # ==========================================================================
    def get_fighter_by_name_lw(self, name):
        db_query = "SELECT * FROM lw WHERE name='" + name + "'";
        self.cur.execute(db_query)
        result = self.cur.fetchall()
        return result

    # ==========================================================================
    def get_fighter_by_name_ww(self, name):
        db_query = "SELECT * FROM ww WHERE name='" + name + "'";
        self.cur.execute(db_query)
        result = self.cur.fetchall()
        return result

    # ==========================================================================
    def get_fighter_by_name_mw(self, name):
        db_query = "SELECT * FROM mw WHERE name='" + name + "'";
        self.cur.execute(db_query)
        result = self.cur.fetchall()
        return result

    # ==========================================================================
    def getAllFightersFromWeight(self, weightclass):
        db_query = "SELECT * FROM " + weightclass + "";
        self.cur.execute(db_query)
        result = self.cur.fetchall()
        # print (row.get('id'), row.get('name'))
        return result

    # ==========================================================================
    def getFighterWins(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("wins"))

    # ==========================================================================
    def getFighterName(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("name"))

    # ==========================================================================
    def getFighterid(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("id"))

    # ==========================================================================
    def getFighterLosses(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("losses"))

    # ==========================================================================
    # returns the number the of KO wins of a specific fighter
    def getFighterKOs(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("KO_wins"))

    # ==========================================================================
    # returns the number of submission wins of a specific fighter
    def getFighterSubs(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("SUB_wins"))

    # ==========================================================================
    # returns the number of decision wins of a specific fighter
    def getFighterDecs(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("DEC_wins"))

    # ==========================================================================
    # returns striking accuracy percentage of a specific fighter
    def getFighterStrAccur(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("str_accur"))

    # ==========================================================================
    # returns grappling accuracy percentage of a specific fighter
    def getFighterGrpAccur(self, wc, name):
        result = self.getFighter(wc, name)
        return (result[0].get("grp_accur"))

    # ==========================================================================
    # adds a new fighter of a specific weight class table to the database
    def addNewFighter(self, wc, name, wins, losses, ko_wins, sub_wins, dec_wins, str_acr, grp_acr):
        data = (name, wins, losses, ko_wins, sub_wins, dec_wins, str_acr, grp_acr)

        db_query = "INSERT INTO " + wc + "(name, wins, losses, KO_wins, SUB_wins, DEC_wins, str_accur, grp_accur) "\
                                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(db_query, data)
        self.con.commit()
