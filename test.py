def check_freq(word):

    freq = {}
    uniques = []
    for letter in word:
        freq[letter] = word.count(letter)

    for unique in freq:
        if freq[unique] == 1:
            uniques.append(unique)

    print(uniques)


check_freq("anagram")
