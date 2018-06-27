import re
import random


def pemrtuate(text):
    words = re.findall(r'\w+', text)
    shuffled_text = ''
    for word in words:
        if len(word) <= 3:
            shuffled_word = word + ' '
            shuffled_text += shuffled_word
            continue
        middle = word[1:-1]
        start = 0
        stop = 3
        shuffled_word = ''
        shuffle_step = 3
        for i in range(0, len(middle), shuffle_step):
            to_shuffle = list(middle[start + i: stop + i])
            random.shuffle(to_shuffle)
            to_shuffle = ''.join(to_shuffle)
            shuffled_word += to_shuffle
        shuffled_word = word[0] + shuffled_word + word[-1] + ' '
        shuffled_text += shuffled_word
    shuffled_text_list = shuffled_text.split()
    for i in range(len(shuffled_text_list)):
        text = text.replace(words[i], shuffled_text_list[i])
    return text


text = """У нас было 2 пакета травы, 75 таблеток мескалина, 5 упаковок кислоты, полсолонки кокаина и целое множество 
транквилизаторов всех сортов и расцветок, депрессанты, а также текила, ром, ящик пива, пинта чистого эфира и 2 дюжины 
ампул амилнитрита. 
Не то чтобы это был необходимый запас для поездки, но если начал собирать дурь, становится трудно остановиться. 
Единственное, что вызывало у меня опасение — это эфир. 
Ничто в мире не бывает более беспомощным, безответственным и порочным, чем эфирные зомби. 
Я знал, что рано или поздно мы перейдем и на эту дрянь."""

print(pemrtuate(text))