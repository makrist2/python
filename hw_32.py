import collections


def count_words(file_path_text, file_path_stop_words, top_n):
    c = collections.Counter()
    stop_words = []
    wordss = []
    punct = ',.!?:;-......"'

    with open(file_path_stop_words) as f2:
        for text in f2:
            for word in text.split():
                stop_words.append(word)

    with open(file_path_text) as f1:
        for text in f1:
            for word in text.split():
                if word.lower() not in stop_words and word.lower() not in punct:
                    wordss.append(word)

    for word in wordss:
        c[word] += 1

    return c.most_common(top_n)


print(count_words('galaxy.txt', 'hw_32_stop_words.txt', 10))