from Packages import *

cursor = conn.connect(server, database, username, password)


class CRUD:

    def DisplayTable(self, table_name):
        query = 'select * from ' + table_name + ';'
        table = cursor.execute(query)
        for row in table:
            print(row)

    def Insert(self, table_name, data):
        Insert_query = f'''INSERT INTO {table_name}(ProductName, Price)
                          VALUES(?,?);'''

        for row in data:
            value = (row[0], row[1])
            cursor.execute(Insert_query, value)

        cursor.commit()

# o = CRUD()
# o.DisplayTable('Customer')
