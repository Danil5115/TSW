def count_words(text):
    """Count the frequency of each word in the given text."""
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip('.,!?"\'')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def most_common_word(text):
    """Find the most common word in the given text."""
    word_count = count_words(text)
    if not word_count:
        raise ValueError("No words in text")
    most_common = max(word_count, key=word_count.get)
    return most_common
