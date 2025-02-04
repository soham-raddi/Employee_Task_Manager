import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='12345')
print(mydb)
cur=mydb.cursor()
def create():
    cur.execute("create database project")
    cur.execute("use project")
    cur.execute("create table employees(empid varchar(10) primary key, empname varchar(20) not null, projectname varchar(20) not null, department varchar(20) not null)")
    cur.execute("create table tasks(taskid varchar(10) primary key, taskname varchar(50) not null, duedate date not null, empid varchar(10) not null, foreign key (empid) references employees(empid), status varchar(15) not null default 'incomplete', priority varchar(4) not null)")
    
def employees():
    cur.execute("use project")
    sql=("insert into employees(empid, empname, projectname, department) values('01', 'Emp1', 'project1', 'R&D')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into employees(empid, empname, projectname, department) values('02', 'Emp2', 'project1', 'Finance')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into employees(empid, empname, projectname, department) values('03', 'Emp3', 'project1', 'Management')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into employees(empid, empname, projectname, department) values('04', 'Emp4', 'project1', 'HR')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into employees(empid, empname, projectname, department) values('05', 'Emp5', 'project1', 'Senior Manager')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into employees(empid, empname, projectname, department) values('06', 'Emp6', 'none', 'senior manager')",)
    cur.execute(*sql)
    mydb.commit()

def tasks():
    cur.execute("use project")
    sql=("insert into tasks(taskid, taskname, duedate, empid, status, priority) values('T1', 'make ppt', '2022-10-23', '02', 'complete', 'high')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into tasks(taskid, taskname, duedate, empid, status, priority) values('T2', 'make excel sheet', '2022-10-23', '05', 'incomplete', 'low')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into tasks(taskid, taskname, duedate, empid, status, priority) values('T3', 'make excel sheet', '2022-10-23', '05', 'complete', 'low')",)
    cur.execute(*sql)
    mydb.commit()
    sql=("insert into tasks(taskid, taskname, duedate, empid, status, priority) values('T4', 'make excel sheet', '2022-10-23', '03', 'complete', 'high')",)
    cur.execute(*sql)
    mydb.commit()

def newtask():
    cur.execute("use project")
    empid=input("Enter employee id").strip()
    sql=("Select empid from employees",)
    cur.execute(*sql)
    rec=cur.fetchall()
    if (empid,) in rec:
        cur.execute("use project")
        taskid=input("Enter task id").strip()
        sql=("Select taskid from tasks",)
        cur.execute(*sql)
        rec1=cur.fetchall()
        if (taskid,) not in rec1:
            taskname=input("Enter task name").strip()
            duedate=input("Enter due date (yyyy-mm-dd)").strip()
            status=input("Enter status of completion (complete/incomplete)").strip()
            priority=input("Enter priority of task (high/low)").strip()
            sql=("insert into tasks(taskid, taskname, duedate, empid, status, priority) values(%s, %s, %s, %s, %s, %s)", (taskid, taskname, duedate, empid, status, priority))
            cur.execute(*sql)
            mydb.commit()
        else:
            print("Task already exists")
    else:
        print("Employee id is invalid")

def newemployee():
    cur.execute("use project")
    empid=input("Enter employee id").strip()
    sql=("Select empid from employees",)
    cur.execute(*sql)
    rec=cur.fetchall()
    if (empid,) not in rec:
        empname=input("Enter employee name").strip()
        proj=input("Enter project name").strip()
        dept=input("Enter department name").strip()
        sql=("insert into employees(empid, empname, projectname, department) values (%s, %s, %s, %s)", (empid, empname, proj, dept))
        cur.execute(*sql)
        mydb.commit()
    else:
        print("Employee already exists")

def tdytasks():
    cur.execute("Use project")
    from datetime import date
    x=date.today()
    sql=("select * from tasks where duedate=""%s"" ",(x,))
    cur.execute(*sql)
    rec=cur.fetchall()
    sql=("Select duedate from tasks",)
    cur.execute(*sql)
    rec1=cur.fetchall()
    if (x,) not in rec1:
        print("No tasks due today")
    else:
        for i in rec:
            j=0
            while j<=5:
                print(i[j],end='\t')
                j+=1
            print('\n') 

def priority():
    cur.execute("use project")
    sql=("Select priority from tasks",)
    cur.execute(*sql)
    rec1=cur.fetchall()
    if ('high',) not in rec1:
        print("No high priority tasks found")
    else:
        p=("select * from tasks where priority='high'",)
        cur.execute(*p)
        rec=cur.fetchall()
        for i in rec:
            j=0
            while j<=5:
                print(i[j],end='\t')
                j+=1
            print('\n')

def incomp():
    cur.execute("use project")
    sql=("Select status from tasks",)
    cur.execute(*sql)
    rec1=cur.fetchall()
    if ('incomplete',) not in rec1:
        print("No incomplete tasks found")
    else:
        p=("select * from tasks where status='incomplete'",)
        cur.execute(*p)
        rec=cur.fetchall()
        for i in rec:
            j=0
            while j<=5:
                print(i[j],end='\t')
                j+=1
            print('\n')

def updatestatus():
    cur.execute("use project")
    tid=input("enter task id").strip()
    sql=("Select taskid from tasks",)
    cur.execute(*sql)
    rec=cur.fetchall()
    if (tid,) in rec:
        sql=("update tasks set status='complete' where taskid=""%s"" ", (tid,))
        cur.execute(*sql)
        mydb.commit()
    else:
        print("Task id is invalid")

def viewbyemp():
    cur.execute("use project")
    empid=input("enter employee id").strip()
    sql=("Select empid from tasks",)
    cur.execute(*sql)
    rec=cur.fetchall()
    sql=("Select empid from employees",)
    cur.execute(*sql)
    rec1=cur.fetchall()
    if (empid,) in rec:
        sql=("select * from tasks where empid=""%s"" ", (empid,))
        cur.execute(*sql)
        rec=cur.fetchall()
        for i in rec:
            j=0
            while j<=5:
                print(i[j],end='\t')
                j+=1
            print('\n')
    elif (empid,) not in rec1:
        print("Employee id is invalid")
    else:
        print("No tasks have been assigned to this employee")

def main():
    if (mydb):
        print('Connection Successful')
        reply='y'
        while reply=='y':
            print('***','WELCOME TO TASK MANAGER!','***')
            print('')
            print(' Please choose an option from the menu')
            print('')
            print(' 1: Add a task')
            print('')
            print(" 2: Add an employee")
            print('')
            print(" 3: View today's tasks")
            print('')
            print(' 4: View high priority tasks')
            print('')
            print(' 5: View incomplete tasks')
            print('')
            print(' 6: Update status of completion')
            print('')
            print(' 7: Viewing tasks for a particular employee')
            print('')
            print(' 8: Quit')
            print('')
            ch=int(input(' Enter your choice: '))
            print('')
            if(ch==1):
                newtask()
            elif(ch==2):
                newemployee()
            elif(ch==3):
                tdytasks()
            elif(ch==4):
                priority()
            elif(ch==5):
                incomp()
            elif(ch==6):
                updatestatus()
            elif(ch==7):
                viewbyemp()
            elif (ch==8):
                reply='n'
            else:
                print("Please choose from numbers displayed above")
                print('')
            if ch!=8:
                print('')
                reply=input("Would you like to continue? (y/n)").strip()
                print('')
create()
employees()
tasks()
