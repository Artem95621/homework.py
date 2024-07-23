def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
                if other_words[i].lower() in root_words.lower():
            same_words.append(other_words[i])
        elif root_words.lower() in other_words[i].lower():
            same_words.append(other_words[i])

    return same_words

same_words_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
same_words_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(same_words_1)
print(same_words_2)
