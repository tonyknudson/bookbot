import sys
from stats import get_book_text

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        get_book_text(path_to_file)
    print(sys.argv)
    # Prints ['main.py']

main()