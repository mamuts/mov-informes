import sys

DATABASE_PATH = "moviments.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/moviments_test.csv"
