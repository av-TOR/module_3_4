def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.upper() in root_word.upper():
            same_words.append(i)
    print(same_words)
    return same_words


Print1 = single_root_words('Гидроэлектростанция', 'Гидро', 'Электро', 'Станция', 'Молния', 'Дрон')
