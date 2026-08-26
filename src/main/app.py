import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.main.lab import problem1


def main():
    conn = problem1()
    print("problem1() ran. Run the tests to check whether it's correct.")
    conn.close()


if __name__ == "__main__":
    main()
