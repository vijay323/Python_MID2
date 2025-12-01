"""Q16. Write a Python program using mysql.connector to connect to a MySQL database, create a 
table students, insert multiple records, and display them. And, extend the program to allow 
user-driven operations: • Add new records • Update marks • Delete a record • Search by roll 
number.""" 
import mysql.connector 
from mysql.connector import Error 
 
DB_CONFIG = { 
    "host": "localhost", 
    "user": "root", 
    "password": "your_password", 
    "database": "test_db" 
} 
 
def get_conn(): 
    return mysql.connector.connect(**DB_CONFIG) 
 
def setup(): 
    try: 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS students ( 
            roll INT PRIMARY KEY, 
            name VARCHAR(100), 
            marks INT 
        ) 
        """) 
        conn.commit() 
    except Error as e: 
        print("DB Error during setup:", e) 
    finally: 
        if conn.is_connected(): 
            cur.close() 
            conn.close() 
 
def insert_multiple(records): 
    try: 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.executemany("INSERT INTO students (roll, name, marks) VALUES (%s, %s, %s)", records) 
        conn.commit() 
        print(cur.rowcount, "rows inserted.") 
    except Error as e: 
        print("Insert error:", e) 
    finally: 
        cur.close(); conn.close() 
 
def display_all(): 
    try: 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.execute("SELECT roll, name, marks FROM students ORDER BY roll") 
        rows = cur.fetchall() 
        for r in rows: 
            print(r) 
    except Error as e: 
        print("Display error:", e) 
    finally: 
        cur.close(); conn.close() 
 
def add_record(): 
    try: 
        r = int(input("Roll: ")) 
        n = input("Name: ").strip() 
        m = int(input("Marks: ")) 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.execute("INSERT INTO students (roll, name, marks) VALUES (%s, %s, %s)", (r, n, m)) 
        conn.commit() 
        print("Added.") 
    except Error as e: 
        print("DB error:", e) 
    except Exception as e: 
        print("Input error:", e) 
    finally: 
        cur.close(); conn.close() 
 
def update_marks(): 
    try: 
        r = int(input("Roll to update: ")) 
        m = int(input("New marks: ")) 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.execute("UPDATE students SET marks=%s WHERE roll=%s", (m, r)) 
        conn.commit() 
        print("Updated rows:", cur.rowcount) 
    except Error as e: 
        print("DB error:", e) 
    finally: 
        cur.close(); conn.close() 
 
def delete_record(): 
    try: 
        r = int(input("Roll to delete: ")) 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.execute("DELETE FROM students WHERE roll=%s", (r,)) 
        conn.commit() 
        print("Deleted rows:", cur.rowcount) 
    except Error as e: 
        print("DB error:", e) 
    finally: 
        cur.close(); conn.close() 
 
def search_by_roll(): 
    try: 
        r = int(input("Roll to search: ")) 
        conn = get_conn() 
        cur = conn.cursor() 
        cur.execute("SELECT roll, name, marks FROM students WHERE roll=%s", (r,)) 
        row = cur.fetchone() 
        if row: 
            print("Found:", row) 
        else: 
            print("No record with that roll.") 
    except Error as e: 
        print("DB error:", e) 
    finally: 
        cur.close(); conn.close() 
 
def menu(): 
    setup() 
    while True: 
        print("\n1.Add multiple sample records\n2.Display all\n3.Add record\n4.Update 
marks\n5.Delete record\n6.Search by roll\n7.Exit") 
        ch = input("Choice: ").strip() 
        if ch == "1": 
            # sample batch insert (change as needed) 
            sample = [(1, "Aman", 78), (2, "Bina", 85), (3, "Chetan", 66)] 
            insert_multiple(sample) 
        elif ch == "2": 
            display_all()
  elif ch == "3": 
            add_record() 
        elif ch == "4": 
            update_marks() 
        elif ch == "5": 
            delete_record() 
        elif ch == "6": 
            search_by_roll() 
        elif ch == "7": 
            break 
        else: 
            print("Invalid choice.") 
 
if __name__ == "__main__": 
    menu()
