import os
import sqlite3

"""
SQL sublanguage: DDL (Data Definition Language)

A primary key is a constraint that we can add to a column that labels that column as the unique identifier for a
record in the table. Primary Keys are UNIQUE and NOT NULL implicitly.

Let's say we want to create a "site_user" table that has the following columns:
     |   id  |      username        |        password         |
     ----------------------------------------------------------
     |1      |"user1"               |"pass123"                |
     |2      |"user2"               |"pass123"                |
     |3      |"user3"               |"pass123"                |

     The SQL syntax would be as follows:
     CREATE TABLE site_user (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         username varchar(100),
         password varchar(100)
     );
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    song table
    |   id  |      title        |        artist         |
    -----------------------------------------------------
    |1      |'Let it be'        |'Beatles'              |
    |2      |'Hotel California' |'Eagles'               |
    |3      |'Kashmir'          |'Led Zeppelin'         |

    Assignment: create a table in problem1.sql called "song" that has 3 columns listed above

    NOTE: The "id" column is what we are going to define as the primary key.

    Runs the student's CREATE TABLE statement and returns the open connection so the caller can verify both
    that a surrogate key works, and that the primary key enforces uniqueness. Each call gets a fresh, independent
    in-memory database, so it's safe to call this twice - once per check.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
