from data.Database import Database
from datetime import date, datetime
# Parent class of account
class Account:
    def __init__(self):
        database = Database()
        self._db = database.getDb()
        self._cursor = database.getCursor()

        self._id = None
        self._customer_id = None
        self._type = None
        self._balance = None
    
    def new(self, id, customer_id, type, balance):
        database = Database()
        self._db = database.getDb()
        self._cursor = database.getCursor()

        self._id = id
        self._customer_id = customer_id
        self._type = type
        self._balance = balance
        return self

    def getId(self):
        return self._id

    def getCustomerId(self):
        return self._customer_id

    def getType(self):
        return self._type

    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        if self._id == None:
            return False
        # obj
        self._balance += amount
        # create transaction
        query = "INSERT INTO transactions(account_id, time, type, amount, note) VALUES ("+str(self._id)+", '"+str(datetime.now())+"', 'deposit', "+str(amount)+", 'General deposit')"
        self._cursor.execute(query)
        self._db.commit()
        result = self._cursor.lastrowid
        # update balance on account
        query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True
    
    def withdraw(self, amount):
        if self._id == None:
            return False
        remain = self._balance - amount
        # obj
        if remain > 0:
            self._balance = remain
        # create transaction
        query = "INSERT INTO transactions(account_id, time, type, amount, note)" 
        query += "VALUES ("+str(self._id)+", '"+str(datetime.now())+"', 'withdraw', "+str(amount)+", 'General withdraw')"
        self._cursor.execute(query)
        self._db.commit()
        result = self._cursor.lastrowid
        # update balance on account
        query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True
            
    def balanceEnquiry(self):
        return self._balance
    
    def getAccountsByCustomerId(self, customer_id):
        query = "SELECT * FROM accounts WHERE customer_id="+str(customer_id)
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()
        if result == []:
            return None
        
        accs = []
        for acc in result:
            ac_ = Account()
            ac_ = ac_.new(acc[0], acc[1], acc[2], acc[3])
            accs.append(ac_)

        return accs

        
# Child class of account
class AccountChecking(Account):
    def __init__(self):
        super().__init__()
        self._credit_limit = None
        self._type = None
        self._account_id = None

    def new(self, id, account_id, customer_id, balance, credit_limit):
        self._id = id 
        self._account_id = account_id
        self._customer_id = customer_id
        self._balance = balance
        self._credit_limit = credit_limit
        self._type = "checking"
        return self

    def create(self, customer_id, balance, credit_limit):
        # create account
        query = "INSERT INTO accounts(customer_id, type, balance) VALUES ('"+ str(customer_id) +"', 'checking', "+str(balance)+")"
        self._cursor.execute(query)
        self._db.commit()
        account_id = self._cursor.lastrowid

        # create checlomg
        query = "INSERT INTO checking(account_id, credit_limit) VALUES("+str(account_id)+", "+str(credit_limit)+")"
        self._cursor.execute(query)
        self._db.commit()
        loan_id = self._cursor.lastrowid

        checking = AccountChecking()
        checking = checking.new(loan_id, account_id, customer_id, balance, credit_limit)
        self._db.close()
        return checking

    def deposit(self, amount):
        if self._id == None:
            return False
        # obj
        self._balance += amount
        # create transaction
        query = "INSERT INTO transactions(account_id, time, type, amount, note) VALUES ("+str(self._account_id)+", '"+str(datetime.now())+"', 'deposit', "+str(amount)+", 'General deposit')"
        self._cursor.execute(query)
        self._db.commit()
        result = self._cursor.lastrowid
        # update balance on account
        query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True
        
    def withdraw(self, amount):
        if self._id==None:
            return False
        remain = self._balance - amount
        if remain > -self._credit_limit:
            self._balance -= amount
            # obj
            self._balance = remain

            # create transaction
            query = "INSERT INTO transactions(account_id, time, type, amount, note)" 
            query += "VALUES ("+str(self._account_id)+", '"+str(datetime.now())+"', 'withdraw', "+str(amount)+", 'Checking withdraw')"
            self._cursor.execute(query)
            self._db.commit()
            result = self._cursor.lastrowid

            # update balance on account
            query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._account_id)
            self._cursor.execute(query)
            result = self._cursor.lastrowid
            self._db.commit()
            self._db.close()
            return True
        else:
            return False
    
    def setCreditLimit(self, credit_limit):
        #obj
        self._credit_limit = credit_limit
        return True
    
    def getCreditLimit(self):
        return self._credit_limit

    def save(self):
        #update account
        query = "UPDATE checking SET credit_limit="+str(self._credit_limit)+" WHERE id="+str(self._id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True

    def getCheckingByCustomerId(self, customer_id):
        query = "SELECT a.id, b.id, b.customer_id, b.balance, a.credit_limit FROM checking a, accounts b WHERE a.account_id=b.id AND b.customer_id="+str(customer_id)
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()
        if result == []:
            return None
        
        accChecks = []
        for accCheck in result:
            tmp = AccountChecking()
            tmp = tmp.new(accCheck[0], accCheck[1], accCheck[2], accCheck[3], accCheck[4])
            accChecks.append(tmp)
        return accChecks

    def getAllCheckings(self):
        query = "SELECT a.id, b.id, b.customer_id, b.balance, a.credit_limit FROM checking a, accounts b WHERE a.account_id=b.id"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()
        
        accChecks = []
        for accCheck in result:
            tmp = AccountChecking()
            tmp = tmp.new(accCheck[0], accCheck[1], accCheck[2], accCheck[3], accCheck[4])
            accChecks.append(tmp)
        return accChecks

    def getCheckingByAccountId(self, account_id):
        query = "select checking.id, accounts.id, accounts.customer_id, accounts.balance, checking.credit_limit from accounts, checking where accounts.id=checking.account_id and accounts.id="+str(account_id)
        self._cursor.execute(query)
        result = self._cursor.fetchone()
        self._db.close()
        if result == []:
            return None

        tmp = AccountChecking()
        tmp = tmp.new(result[0], result[1], result[2], result[3], result[4])
        return tmp
    
    def destroy(self):
        # from transaction
        query = "DELETE FROM transactions WHERE account_id="+str(self._account_id)
        self._cursor.execute(query)
        self._db.commit()

        # from checking
        query = "DELETE FROM checking WHERE id="+str(self._id)
        self._cursor.execute(query)
        self._db.commit()

        # from accounts
        query = "DELETE FROM accounts WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        self._db.commit()

        self._db.close()

        return True
class AccountSaving(Account):
    def __init__(self):
        super().__init__()
        self._interest_rate = None
        self._type = None
        self._account_id = None
    
    def deposit(self, amount):
        if self._id == None:
            return False
        # obj
        self._balance += amount
        # create transaction
        query = "INSERT INTO transactions(account_id, time, type, amount, note) VALUES ("+str(self._account_id)+", '"+str(datetime.now())+"', 'deposit', "+str(amount)+", 'General deposit')"
        self._cursor.execute(query)
        self._db.commit()
        result = self._cursor.lastrowid
        # update balance on account
        query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True
    
    def withdraw(self, amount):
        if self._id == None:
            return False
        remain = self._balance - amount
        # obj
        if remain > 0:
            self._balance = remain
        # create transaction
        query = "INSERT INTO transactions(account_id, time, type, amount, note)" 
        query += "VALUES ("+str(self._account_id)+", '"+str(datetime.now())+"', 'withdraw', "+str(amount)+", 'General withdraw')"
        self._cursor.execute(query)
        self._db.commit()
        result = self._cursor.lastrowid
        # update balance on account
        query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True

    def new(self, id, account_id, customer_id, balance, interest_rate):
        self._id = id 
        self._account_id = account_id
        self._customer_id = customer_id
        self._balance = balance
        self._interest_rate = interest_rate
        self._type = "saving"
        return self
    
    def create(self, customer_id, balance, interest_rate): 
        self._interest_rate = interest_rate
        # create account
        query = "INSERT INTO accounts(customer_id, type, balance) VALUES ('"+ str(customer_id) +"', 'saving', '"+str(balance)+"')"
        self._cursor.execute(query)
        self._db.commit()
        account_id = self._cursor.lastrowid

        # create saving
        query = "INSERT INTO saving(account_id, interest_rate) VALUES("+str(account_id)+", "+str(interest_rate)+")"
        self._cursor.execute(query)
        self._db.commit()
        saving_id = self._cursor.lastrowid

        saving = AccountSaving()
        saving = saving.new(saving_id, account_id, customer_id, balance, interest_rate)
        self._db.close()
        return saving

    def getInterestRate(self):
        return self._interest_rate

    def save(self):
        #update account
        query = "UPDATE saving SET interest_rate="+str(self._credit_limit)+" WHERE id="+str(self._id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True

    def getSavingByCustomerId(self, customer_id):
        query = "SELECT a.id, b.id, b.customer_id, b.balance, a.interest_rate FROM saving a, accounts b WHERE a.account_id=b.id AND b.customer_id="+str(customer_id)
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()
        if result == []:
            return None
        
        accSavings = []
        for accSaving in result:
            tmp = AccountSaving()
            tmp = tmp.new(accSaving[0], accSaving[1], accSaving[2], accSaving[3], accSaving[4])
            accSavings.append(tmp)
        return accSavings

    def getAllSavings(self):
        query = "SELECT a.id, b.id, b.customer_id, b.balance, a.interest_rate FROM saving a, accounts b WHERE a.account_id=b.id"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()

        accSavings = []
        for accSaving in result:
            tmp = AccountSaving()
            tmp = tmp.new(accSaving[0], accSaving[1], accSaving[2], accSaving[3], accSaving[4])
            accSavings.append(tmp)
        return accSavings

    def getSavingByAccountId(self, account_id):
        query = "select saving.id, accounts.id, accounts.customer_id, accounts.balance, saving.interest_rate from accounts, saving where accounts.id=saving.account_id and accounts.id="+str(account_id)
        self._cursor.execute(query)
        result = self._cursor.fetchone()
        self._db.close()
        if result == []:
            return None

        tmp = AccountSaving()
        tmp = tmp.new(result[0], result[1], result[2], result[3], result[4])
        return tmp

    def destroy(self):
        # from transaction
        query = "DELETE FROM transactions WHERE account_id="+str(self._account_id)
        self._cursor.execute(query)
        self._db.commit()

        # from checking
        query = "DELETE FROM saving WHERE id="+str(self._id)
        self._cursor.execute(query)
        self._cursor.fetchall()
        self._db.commit()

        # from accounts
        query = "DELETE FROM accounts WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        self._cursor.fetchall()
        self._db.close()
        self._db.close()

        return True
class AccountLoan(Account):
    def __init__(self):
        super().__init__()
        self._interest_rate = None
        self._loan_duration = None
        self._principal_amount = None
        self._account_id = None
    
    def new(self, id, account_id, customer_id, balance, interest_rate, loan_duration, principal_amount):
        self._id = id 
        self._account_id = account_id
        self._customer_id = customer_id
        self._balance = balance
        self._interest_rate = interest_rate
        self._loan_duration = loan_duration
        self._principal_amount = principal_amount
        self._type = "saving"
        return self
    
    def create(self, customer_id, balance, interest_rate, loan_duration, principal_amount):
        # create account
        query = "INSERT INTO accounts(customer_id, type, balance) VALUES ('"+ str(customer_id) +"', 'loan', '"+str(balance)+"')"
        self._cursor.execute(query)
        self._db.commit()
        account_id = self._cursor.lastrowid

        # create loan
        query = "INSERT INTO loan(account_id, interest_rate, loan_duration,principal_amount) VALUES("+str(account_id)+", "+str(interest_rate)+", "+str(loan_duration)+", '"+str(loan_duration)+"')"
        self._cursor.execute(query)
        self._db.commit()
        loan_id = self._cursor.lastrowid

        loan = AccountLoan()
        loan = loan.new(loan_id, account_id, self._customer_id, balance, interest_rate, loan_duration, principal_amount)
        self._db.close()
        return loan

    def setPrincipalAmount(self, amount):
        self._principal_amount = amount
    
    def setInterestRate(self, interest_rate):
        self._interest_rate = interest_rate

    def setLoanDuration(self, duration):
        self._loan_duration = duration
    
    def getPrincipalAmount(self):
        return self._principal_amount
    
    def getInterestRate(self):
        return self._interest_rate
    
    def getLoanDuration(self):
        return self._loan_duration

    def save(self):
        #update account
        query = "UPDATE loan SET interest_rate="+str(self._interest_rate)+", loan_duration="+str(self._loan_duration)+", principal_amount="+str(self._principal_amount)+" WHERE id="+str(self._id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True

    def getLoanByCustomerId(self, customer_id):
        query = "SELECT a.id, b.id, b.customer_id, b.balance, a.interest_rate, a.loan_duration, a.principal_amount FROM loan a, accounts b WHERE a.account_id=b.id AND b.customer_id="+str(customer_id)
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()

        if result == []:
            return None
        
        accLoans = []
        for accLoan in result:
            tmp = AccountLoan()
            tmp = tmp.new(accLoan[0], accLoan[1], accLoan[2], accLoan[3], accLoan[4], accLoan[5], accLoan[6])
            accLoans.append(tmp)
        return accLoans

    def getAllLoans(self):
        query = "SELECT a.id, b.id, b.customer_id, b.balance, a.interest_rate, a.loan_duration, a.principal_amount FROM loan a, accounts b WHERE a.account_id=b.id"
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        self._db.close()
        
        accLoans = []
        for accLoan in result:
            tmp = AccountLoan()
            tmp = tmp.new(accLoan[0], accLoan[1], accLoan[2], accLoan[3], accLoan[4], accLoan[5], accLoan[6])
            accLoans.append(tmp)
        return accLoans

    def getLoanByAccountId(self, account_id):
        query = "select loan.id, accounts.id, accounts.customer_id, accounts.balance, loan.interest_rate, loan.loan_duration, loan.principal_amount from accounts, loan where accounts.id=loan.account_id and accounts.id="+str(account_id)
        self._cursor.execute(query)
        result = self._cursor.fetchone()
        self._db.close()
        if result == []:
            return None

        tmp = AccountLoan()
        tmp = tmp.new(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        return tmp
    
    def deposit(self, amount):
        if self._id == None:
            return False
        # obj
        self._balance += amount
        # create transaction
        query = "INSERT INTO transactions(account_id, time, type, amount, note) VALUES ("+str(self._account_id)+", '"+str(datetime.now())+"', 'deposit', "+str(amount)+", 'General deposit')"
        self._cursor.execute(query)
        self._db.commit()
        result = self._cursor.lastrowid
        # update balance on account
        query = "UPDATE accounts SET balance="+str(self._balance)+" WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        result = self._cursor.lastrowid
        self._db.commit()
        self._db.close()
        return True
    
    def destroy(self):
        # from transaction
        query = "DELETE FROM transactions WHERE account_id="+str(self._account_id)
        self._cursor.execute(query)
        self._db.commit()

        # from checking
        query = "DELETE FROM loan WHERE id="+str(self._id)
        self._cursor.execute(query)
        self._db.commit()

        # from accounts
        query = "DELETE FROM accounts WHERE id="+str(self._account_id)
        self._cursor.execute(query)
        self._db.commit()

        self._db.close()

        return True