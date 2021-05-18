from data.Database import Database
from datetime import date, datetime
# Parent class of account

class Transaction:
    def __init__(self):
        database = Database()
        self._db = database.getDb()
        self._cursor = database.getCursor()
        self._id = None
        self._account_id = None
        self._time = None
        self._type = None
        self._amount = None
        self._note = None
    
    def new(self, id, account_id, time, type, amount, note):
        self._id = id
        self._account_id = account_id
        self._time = time
        self._type = type
        self._amount = amount
        self._note = note
        return self

    def getTransactionsByAccountId(self, account_id):
        query = "SELECT * FROM transactions WHERE account_id="+str(account_id)
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()

        dt = []
        for dd in result:
            tmptr = Transaction()
            tmptr = tmptr.new(str(dd[0]), str(dd[1]), str(dd[2]), str(dd[3]), str(dd[4]), str(dd[5]))
            dt.append(tmptr)        
        return dt
    
    def getId(self):
        return self._id
    
    def getAccountId(self):
        return self._account_id
    
    def getTime(self):
        return self._time
    
    def getType(self):
        return self._type
    
    def getAmount(self):
        return self._amount
    
    def getNote(self):
        return self._note
        