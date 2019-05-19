import sqlite3 as lite 
import sys


# query_string = '''
#   SELECT e.Phone, c.*
#   FROM Employee as e
#   INNER JOIN Customer as c ON e.EmployeeId  =  c.SupportRepId
#   LEFT JOIN Invoice as i on i.CustomerId = c.CustomerId
# '''


# query_string = '''
#     UPDATE Employee
#     SET FirstName = 'Ясон'
#     WHERE EmployeeId = 4
# '''

# query_string = '''
#     INSERT INTO Employee (EmployeeId, LastName, FirstName)
#     VALUES
#     (21, 'Евгений', 24),
#     (22, 'Николай', 42),
#     (23, 'Петр', 33);
# '''

# query_string = '''
#     DELETE FROM Employee WHERE EmployeeId = 23;
#     DELETE FROM Employee WHERE EmployeeId = 22
# '''

query_string = '''
    DELETE FROM Employee WHERE EmployeeId = 23;
    DELETE FROM Employee WHERE EmployeeId = 22
'''


con = None
try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()    
    cur.execute(query_string)
    # con.commit()
    con.rollback()
    data = cur.fetchall()
    # print(cur.description)
    c = 1
    for item in data:
        print(item, c)
        c += 1
except Exception as e:
    print(e)
    sys.exit(1)
finally:
    if con is not None:
        con.close()
