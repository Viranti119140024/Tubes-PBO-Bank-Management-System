## DATABASE CONNECTOR
class Database:
    def __init__(self, 
                 DB_HOST = "localhost", 
                 DB_USER = "root", 
                 DB_PASSWORD = "", 
                 DB_NAME="bank_management"):
        
        import mysql.connector
        self.__db = mysql.connector.connect(
            host = DB_HOST,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME,   
        )
    def getCursor(self):
        return self.__db.cursor()
    
    def getDb(self):
        return self.__db