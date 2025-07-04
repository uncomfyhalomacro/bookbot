def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(contents):
    return len(contents.split())

def get_character_count(contents):
    contents = contents.lower()
    unique_chars = set(contents)
    char_dict = dict((c, contents.count(c)) for c in unique_chars)
    char_dict = dict(sorted(char_dict.items()))
    return char_dict
