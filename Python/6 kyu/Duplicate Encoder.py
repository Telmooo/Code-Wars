def duplicate_encode(word):
    word = word.lower()
    occurences = {}
    for char in word:
        occurences[char] = ')' if char in occurences else '('
    return ''.join(occurences[char] for char in word)
