import sqlite3
import unittest

from src.main.lab import problem1


def _has_text_affinity(declared_type):
    declared_type = (declared_type or "").upper()
    return any(marker in declared_type for marker in ("CHAR", "CLOB", "TEXT"))


class LabTest(unittest.TestCase):
    def test_create_table_surrogate_key(self):
        """
        To test that the table exists, we attempt to insert a row into it, without manually providing an id -
        the db should generate one for us because of the auto-incrementing primary key.

        NOTE: SQLite only auto-generates an id when the column's declared type is exactly "INTEGER" (not
        "INT", "BIGINT", "SERIAL", or any other synonym) combined with PRIMARY KEY - that specific combination
        is the only one that becomes an alias for SQLite's internal rowid. Anything else looks like it works
        (the insert doesn't raise an error) but silently stores NULL for id instead of generating a value - so
        we check the actual inserted id, not just whether the insert succeeded.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("INSERT into song (Title, Artist) VALUES ('Let it Be', 'Beatles')")
            conn.commit()
            cur.execute("SELECT id FROM song WHERE Title = 'Let it Be';")
            row = cur.fetchone()

            cur.execute("PRAGMA table_info(song);")
            # PRAGMA table_info columns are: cid, name, type, notnull, dflt_value, pk
            columns = {r[1].lower(): r[2] for r in cur.fetchall()}
        except Exception as e:
            print(f"problem1: {e}\n")
            self.fail(str(e))
        finally:
            conn.close()

        self.assertIsNotNone(row, "the inserted row could not be found")
        self.assertIsNotNone(
            row[0],
            "id was not auto-generated (it's NULL) - make sure the column is declared as exactly "
            "'INTEGER PRIMARY KEY', not 'INT', 'SERIAL', or any other synonym",
        )

        self.assertIn("title", columns, "title column was not found")
        self.assertTrue(
            _has_text_affinity(columns["title"]),
            f"title should be a text type (e.g. varchar(100)), but it was declared as '{columns['title']}'",
        )

        self.assertIn("artist", columns, "artist column was not found")
        self.assertTrue(
            _has_text_affinity(columns["artist"]),
            f"artist should be a text type (e.g. varchar(100)), but it was declared as '{columns['artist']}'",
        )

    def test_primary_key_unique_constraint(self):
        """
        This test uses a fresh copy of the table (from a new call to problem1()) and checks that the primary
        key actually enforces uniqueness: inserting two rows with the same id should raise an integrity error.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("INSERT into song (id, Title, Artist) VALUES (1,'Let it Be', 'Beatles');")
            cur.execute("INSERT into song (id, Title, Artist) VALUES (1,'Imagine', 'Beatles');")
            conn.commit()
            print("problem1: Primary Key constraint not implemented due to unique constraint not being enforced")
            self.fail("duplicate id was inserted without error")
        except sqlite3.IntegrityError:
            # this is the expected outcome - the primary key constraint stopped the duplicate insert
            pass
        finally:
            conn.close()


if __name__ == "__main__":
    unittest.main()
