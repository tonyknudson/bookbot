def sort_on(items):
    return items["num"]

def get_report_header():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

def get_report_num_words(num_words):
    print(f" Found {num_words} total words")

def get_report_trailer(sorted_items):
    print("--------- Character Count -------")
    
    for x in sorted_items:
        print(*x, sep=': ')
 
    


def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    
        # f is a file object
        file_contents = f.read()
        # print(f"{file_contents}")
        num_words = 0
        for word in file_contents.split():
            num_words += 1

        char_count = {}
        for char in file_contents.lower():
            if char.isalpha():
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        sorted_items = sorted(char_count.items(), key=lambda p: p[1], reverse=True)
        # sorted_items = char_count.sort(reverse=True, key=sort_on)
        # sorted_items = dict(sorted(char_count.items(), key=lambda item: item, reverse=True))

        get_report_header()
        get_report_num_words(num_words)
        get_report_trailer(sorted_items)
