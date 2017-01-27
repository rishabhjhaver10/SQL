import sqlite3
from datetime import date
from random import randrange
from random import choice
from random import randint

conn = sqlite3.connect('employee.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS emp(empno INT, ename TEXT, job TEXT, hire_date TEXT, salary INT, comm INT, deptno INT)")
    c.execute("CREATE TABLE IF NOT EXISTS dept(deptno INT, dname TEXT, location)")
    c.execute("CREATE TABLE IF NOT EXISTS salgrade(grade INT, losal INT, hisal INT)")
    
def data_entry():
    c.execute("INSERT INTO dept VALUES(10, 'Accounting', 'NewYork')")
    c.execute("INSERT INTO dept VALUES(20, 'Research', 'Dallas')")
    c.execute("INSERT INTO dept VALUES(30, 'Sales', 'Chicago')")
    c.execute("INSERT INTO dept VALUES(40, 'Operations', 'Boston')")
    
    c.execute("INSERT INTO salgrade VALUES(1, 500, 1000)")
    c.execute("INSERT INTO salgrade VALUES(2, 1001, 1500)")
    c.execute("INSERT INTO salgrade VALUES(3, 1501, 2000)")
    c.execute("INSERT INTO salgrade VALUES(4, 2001, 2500)")
    c.execute("INSERT INTO salgrade VALUES(5, 2501, 3000)")


def dynamic_data_entry():
    enames = ['Smith', 'Jones', 'Clark', 'Johnson', 'Scott', 'Blake', 'Miller', 'Ford', 'James', 'Martin', 'Allen', 'Williams']
    jobs = ['Clerk', 'Salesman', 'Manager', 'Analyst', 'Vice President']
    department = [10, 20, 30, 40]
    
    job = choice(jobs)
    
    if job == 'Clerk':
        salary = randrange(500, 1000, 50)
        comm = randrange(50, 100, 10)
        deptno = choice(department)
    
    elif job == 'Salesman':
        salary = randrange(1000, 1500, 50)
        comm = randrange(300, 800, 20)
        deptno = department[2]
        
    elif job == 'Manager':
        salary = randrange(2000, 3000, 100)
        comm = randrange(500, 1000, 50)
        deptno = choice(department)
        
    elif job == 'Analyst':
        salary = randrange(3000, 3500, 100)
        comm = randrange(500, 1000, 50)
        deptno = choice(department)
        
    elif job == 'Vice President':
        salary = 5000
        comm = 1000
        deptno = choice(department)
    
    year = randint(1991, 2000)
    month = randint(1, 12)
    day = randint(1, 28)
    hire_date = date(year, month, day)
    
    empno = randrange(7360,7900)
    
    ename = choice(enames)
    
    c.execute("INSERT INTO emp (empno, ename, job, hire_date, salary, comm, deptno) VALUES (?, ?, ?, ?, ?, ?, ?)",
          (empno, ename, job, hire_date, salary, comm, deptno))

    conn.commit()

create_table()
data_entry()
    
for i in range(25):
    dynamic_data_entry()

c.close
conn.close()