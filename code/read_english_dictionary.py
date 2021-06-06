def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()