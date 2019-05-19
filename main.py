import sqlite3 as lite 
import sys


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
second_query_string = '''
    SELECT a.FirstName, a.LastName, a.Phone, b.FirstName, b.LastName, b.Phone
    FROM Employee as a
    LEFT JOIN Employee as b 
    ON a.EmployeeId  =  b.ReportsTo
'''


second_query_string = '''
    SELECT a.FirstName, a.LastName, a.Phone, b.FirstName, b.LastName, b.Phone
    FROM Employee as a
    LEFT JOIN Employee as b 
    ON a.EmployeeId  =  b.ReportsTo
'''


third_query_string = '''
    SELECT a.FirstName, a.Phone, d.UnitPrice, d.TrackId
    FROM Customer as a
    LEFT JOIN Invoice as b 
    ON a.CustomerId  =  b.InvoiceId
    LEFT JOIN InvoiceLine as c
    ON b.InvoiceId  =  c.InvoiceId
    LEFT JOIN Track as d
    ON c.TrackId  =  d.TrackId
'''


con = None
try:
    con = lite.connect('Chinook_Sqlite.sqlite')
    cur = con.cursor()    
    cur.execute(second_query_string)
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
