from os import walk
from os.path import getctime, getsize
from argparse import ArgumentParser
import sqlite3

DBPATH = "fridge.db"

parser = ArgumentParser(description='Get file information.')
parser.add_argument('-d', '--directory', default='/')
args = parser.parse_args()

def initTable():
    conn = sqlite3.connect(DBPATH)
    cur = conn.cursor()
    sql = """
    create table food(
        name varchar,
        size bigint,
        ctime date
        )
    """
    try:
        cur.execute(sql)
        conn.commit()
    except Exception, ex:
        pass
    finally:
        conn.close()

def insertFood(food):
    conn = sqlite3.connect(DBPATH)
    cur = conn.cursor()
    cur.executemany("""INSERT INTO food(name,size,ctime) VALUES (?,?,?)""", food)
    conn.commit()
    conn.close()

def checkFood():
    food = []
    for path, dirnames, fnames in walk(args.directory):
        for fname in fnames:
            fpath = path + "/" + fname
            try:
                food.append([fpath, getctime(fpath), getsize(fpath)])
                print "Name:", fpath, "CTime:", getctime(fpath), " Size:", getsize(fpath)
            except OSError:
                print "error:", fpath
    
    insertFood(food)
    print len(food)

if __name__ == '__main__':
    checkFood()
    initTable()
