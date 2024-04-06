def get_words_ends_with_letter(sentence, letter):
    sentences = sentence.split(". ")
    result = []
    for sentence in sentences:
        words = sentence.split()
        count = sum(1 for word in words if word.endswith(letter))
        word_list = [word for word in words if word.endswith(letter)]
        if count > 0:
            result.append((tuple(word_list), count))
    return result

# Testiranje
sentence = "Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences."
letter = "s"
print(get_words_ends_with_letter(sentence, letter))