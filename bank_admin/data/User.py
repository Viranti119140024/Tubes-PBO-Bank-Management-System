from data.Database import Database

class User:
    def __init__(self):
        # from Database import Database
        database = Database()
        self._db = database.getDb()
        self._cursor = database.getCursor()
        self._id = None
        self._email = None
        self._password = None
    
    def createUser(self, email, password):
        #create user
        query = "INSERT INTO users(email, password) VALUES('"+str(email)+"', '"+str(password)+"')"
        self._cursor.execute(query)
        self._db.commit()
        return self._cursor.lastrowid

    def getUserLogin(self, email, password):
        query = "SELECT * FROM users WHERE email='"+str(email)+"' AND password='"+str(password)+"'"
        self._cursor.execute(query)
        result = self._cursor.fetchone()
        if result == None:
            return None
        self._id = result[0]
        self._email = result[1]
        return self

    def getUserByEmail(self, email):
        query = "SELECT * FROM users WHERE email='" + email + "'"
        self._cursor.execute(query)
        user = self._cursor.fetchone()
        if user == None:
            return None
        self._id = user[0]
        self._email = user[1]
        return self
    
    def getUserById(self, id):
        query = "SELECT * FROM users WHERE id='" + str(id) + "'"
        self._cursor.execute(query)
        user = self._cursor.fetchone()
        if user == None:
            return None
        self._id = user[0]
        self._email = user[1]
        return self
    
    def getId(self):
        return self._id
    
    def getEmail(self):
        return self._email
class Customer(User):
    def __init__(self):
        super().__init__()

        self._id = None
        self._userId = None
        self._phone = None        
        self._address = None
        self._name = None
    
    def getCustomerByEmail(self, email):
        user = self.getUserByEmail(email=email)
        if user==None:
            return None
        query = "SELECT * FROM customers WHERE user_id='"+str(user.getId())+"'"
        self._cursor.execute(query)
        customer = self._cursor.fetchone()
        if customer == None:
            return None
        self._id = customer[0]
        self._email = user.getEmail()
        self._userId = customer[1]
        self._phone = customer[2]
        self._address = customer[3]
        self._name = customer[4]
        return self
    
    def getCustomerById(self, customer_id):
        query = "SELECT * FROM customers WHERE id='"+str(customer_id)+"'"
        self._cursor.execute(query)
        customer = self._cursor.fetchone()
        if customer == None:
            return None
        user = self.getUserById(id=customer[1])
        if user==None:
            return None
        self._id = customer[0]
        self._email = user.getEmail()
        self._userId = customer[1]
        self._phone = customer[2]
        self._address = customer[3]
        self._name = customer[4]
        return self

    def getAllCustomer(self):
        query = "SELECT a.name, a.address, a.phone, b.email FROM customers a, users b WHERE a.user_id=b.id";
        self._cursor.execute(query)
        result = self._cursor.fetchall()
        return result
        
    def create(self, email, phone, address, name, password):
        try:
            userid = self.createUser(email, password)
            query = "INSERT INTO customers(user_id, phone, address, name) VALUES('"+str(userid)+"', '"+str(phone)+"', '"+str(address)+"', '"+str(name)+"')"
            self._cursor.execute(query)
            self._db.commit()
            return self._cursor.lastrowid
        except:
            return False

    def login(self, email, password):
        user = self.getUserLogin(email, password)
        if user == None:
            return False
        
        query = "SELECT * FROM customers WHERE user_id='"+str(user.getId())+"'"
        self._cursor.execute(query)
        customer = self._cursor.fetchone()
        if customer == None:
            return False
        else:
            return True
    
    def getUserId(self):
        return self._userId
    
    def getPhone(self):
        return self._phone
    
    def getAddress(self):
        return self._address
    
    def getName(self):
        return self._name

    def setPhone(self, phone):
        self._phone = phone
        return True

    def setAddress(self, address):
        self._address = address
        return True
    
    def setName(self, name):
        self._name = name
        return True
    
    def save(self):
        query = "UPDATE customers SET phone=%s, address=%s, name=%s WHERE id=%s"
        self._cursor.execute(query, (str(self._phone), str(self._address), str(self._name), str(self._id)))
        self._db.commit()
        return True
    
class BankAdmin(User):
    def __init__(self):
        super().__init__()
        
        self._id = None
        self._userId = None      
        self._address = None
        self._name = None

    def getBankAdminByEmail(self, email):
        user = self.getUserByEmail(email=email)
        if user == None:
            return None
        query = "SELECT * FROM bank_admins WHERE user_id='"+str(user.getId())+"'"
        self._cursor.execute(query)
        bank_admin = self._cursor.fetchone()
        if bank_admin == None:
            return None
        
        self._id = bank_admin[0]
        self._userId = bank_admin[1]
        self._address = bank_admin[2]
        self._name = bank_admin[3]
        return self

    def login(self, email, password):
        user = self.getUserLogin(email, password)
        if user == None:
            return False
        
        query = "SELECT * FROM bank_admins WHERE user_id='"+str(user.getId())+"'"
        self._cursor.execute(query)
        bank_admin = self._cursor.fetchone()
        if bank_admin == None:
            return False
        else:
            return True
    
    def getUserId(self):
        return self._userId
    
    def getAddress(self):
        return self._address
    
    def getName(self):
        return self._name
    
    def setAddress(self, address):
        self._address = address
        return True
    
    def setName(self, name):
        self._name = name
        return True
    
    def save(self):
        query = "UPDATE bank_admins SET address=%s, name=%s WHERE id=%s"
        self._cursor.execute(query, (str(self._address), str(self._name), str(self._id)))
        self._db.commit()
        return True
    