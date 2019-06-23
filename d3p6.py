#!/usr/bin/env python
# We need os module for creating a few funny things 
import os
# and random for yup random stuff
from random import randrange as rand
# CONSTANTS 
COLSIZ = 10
# We have used login, userid and projid as a tuple for creating strings
FIELDS = ('login', 'userid', 'projid')
# a dictionary for stating which database to use
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16
# Forget this for now, I am covering lamda and iterators and generators latter on
tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)

def setup():
    return RDBMSs[input('''
Choose a database system:

(M)ySQL
(G)adfly
(S)QLite

Enter choice: ''').strip().lower()[0]]
# Trick question what does strip do?
def connect(db):
    # global variables are bad but somtimes you need them
    # to use a global variable in a function you need to redeclare it
    # so how do you distingush between global and local variables defined with 
    # the same name?
    global DB_EXC
    dbDir = '%s_%s' % (db, DBNAME)

    if db == 'sqlite':
        try:
            # Import sqlite3 for using the the package a
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        # You know these commands... if it does not exist mkdir
        # Finally some RDBMS stuff
        # just as you have to open a file you need to connect to a database
        # other databases need the adapter and te user code and password
        # the so called connection string with port number . Will talk about it in
        # MySQL
        cxn = sqlite3.connect(os.path.join(dbDir, DBNAME))
        # Connect takes several parameters but returns a connection object
        # print(cxn.apilevel)
        # it also has several methods like .close() to close the connection
        # .commit() to save the transactions made
        # .rollback() to undo all transactions made using this connection object
        # . cursor() - hang onto to this . This guy is the Rajnikanth of databases
    elif db == 'mysql':
        try:
            import MySQLdb
            import _mysql_exceptions as DB_EXC
        except ImportError:
            return None

        try:
            # Here is the connection string  with the DBname and user
            cxn = MySQLdb.connect(db=DBNAME)
        except DB_EXC.OperationalError:
            try:
                cxn = MySQLdb.connect(user=DBUSER)
                # to execute any query you get the return of a connection object
                # mySQL also permits certain query operations such ad create and drop database
                cxn.query('CREATE DATABASE %s' % DBNAME)
                cxn.commit()
                cxn.close()
                cxn = MySQLdb.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                return None

    elif db == 'gadfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError:
            return None

        try:
            cxn = gadfly(DBNAME, dbDir)
        except IOError:
            cxn = gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            cxn.startup(DBNAME, dbDir)
    else:
        return None
    return cxn

def create(cur):
    try:
        
        # see I am executing an create table command and forming this string dynamically
        # mane .. you can create you sql commands on the fly for execute
        # the return value is not defined... try it and find out what this dpes
        cur.execute('''
            CREATE TABLE users (
                login  VARCHAR(%d),
                userid INTEGER,
                projid INTEGER)
        ''' % NAMELEN)
    except DB_EXC.OperationalError:
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (
    ('aaron', 8312), ('angela', 7603), ('dave', 7306),
    ('davina',7902), ('elliot', 7911), ('ernie', 7410),
    ('jess', 7912), ('jim', 7512), ('larry', 7311),
    ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
    ('serena', 7003), ('stan', 7607), ('faye', 6812),
    ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)

def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur, db):
    if db == 'sqlite':
        # quiz 1: Please answer what is the  executemany and excute difference
        # clue look below and you will know
        cur.executemany("INSERT INTO users VALUES(?, ?, ?)",
        [(who, uid, rand(1,5)) for who, uid in randName()])
    elif db == 'gadfly':
        for who, uid in randName():
            cur.execute("INSERT INTO users VALUES(?, ?, ?)",
            (who, uid, rand(1,5)))
    elif db == 'mysql':
        cur.executemany("INSERT INTO users VALUES(%s, %s, %s)",
        [(who, uid, rand(1,5)) for who, uid in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.execute(
        "UPDATE users SET projid=%d WHERE projid=%d" % (to, fr))
    return fr, to, getRC(cur)

def delete(cur):
    rm = rand(1,5)
    cur.execute('DELETE FROM users WHERE projid=%d' % rm)
    return rm, getRC(cur)

def dbDump(cur):
    cur.execute('SELECT * FROM users')
   # when you do a fetchall() it returns a set of rows . which you can iterate
   # print '\n%s' % ''.join(map(cformat, FIELDS))
    for data in cur.fetchall():
        print( ''.join(map(tformat, data)))

def main():
    db = setup()
    print( '*** Connect to %r database' % db)
    cxn = connect(db)
    if not cxn:
        print( 'ERROR: %r not supported or unreachable, exiting' % db)
        return
    # Ye cursor kya he Appa. Think of this as a temporary memory area in your
    # database in which you do all your transactions .. like the white sheets
    # supplied in your CBT. We take them back right and are destroyed ( not actaully) and the end of the
    # test. You can do certain operations using the cursor such as
    # create table, select (read), Update and Delete . CRUD operations and it will store all these in the
    # temporary area. Unlike CBT you can have as many curs as you want and the actions of one cursor
    # are not reflected on the other cursor
    # so what are the standard methods and how do you execute them.
    # cur.rowcount() gives you the rowcount of the particular operation
    # cur.execute('any valid sql command.like insrt update delete etc)
    
    cur = cxn.cursor()

    print ('\n*** Create users table (drop old one if appl.)')
    # Let us see this
    create(cur)

    print ('\n*** Insert names into table')
    insert(cur, db)
    dbDump(cur)

    print ('\n*** Move users to a random group')
    fr, to, num = update(cur)
    print ('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    dbDump(cur)

    print ('\n*** Randomly delete group')
    rm, num = delete(cur)
    print ( '\t(group #%d; %d users removed)' % (rm, num))
    dbDump(cur)

    print ( '\n*** Drop users table')
    drop(cur)
    print ('\n*** Close cxns')
    cur.close()
    cxn.commit()
    cxn.close()

if __name__ == '__main__':
    main()
