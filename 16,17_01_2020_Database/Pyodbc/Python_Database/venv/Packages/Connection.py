import pyodbc
class connectingDB:
    # Establishing connection with database
    def connect(self, server, database, username, password):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                               SERVER=' + server + '; \
                               DATABASE=' + database + '; \
                               UID=' + username + '; \
                               PWD=' + password + '; \
                               Trusted_Connection = yes;')
        # create cursor
        return conn.cursor()

conn = connectingDB()
# Insert_query = '''INSERT INTO Customer(FirstName, LastName, Age, City)
#                   VALUES(?,?,?,?);'''
#
# for row in Customer_data:
#     values = (row[0], row[1], row[2], row[3])
#
#     cursor.execute(Insert_query, values)
#
# conn.commit()

# cursor.execute('SELECT * FROM Customer')
#
# for row in cursor:
#     print(row)
