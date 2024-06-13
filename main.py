def count_words(text):
    #Count the frequency of each word in the given text.
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip('.,!?"\'')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
