path = '/Users/tariyelaghazada/Desktop/Python/robinson.txt'

with open(path) as file:
    content = file.read()

def word_counter(content):
    count = 0
    words = content.split()
    for word in words:
        if word.isalpha():
            count+=1
    print(f'there is {count} words in content')

def letter_counter(content):
    l_count = 0
    for letter in content:
        if letter.isalpha():
            l_count+=1
    print(f'there is {l_count} letters in content')

def most_frequent_word(content):
    words = {}
    w = content.replace('’', '').replace('”', '').replace('”', '').replace(',', '').replace(';', '').replace('.', '').replace('?', '').replace('!', '').replace('“', '')
    text = w.split()
    for word in text:
        if words.get(word):
            words[word] +=1
        else:
            words[word] = 1
    maximum, m_f_word = 0, 0
    for k ,v in words.items():
        if v > maximum:
            maximum = v
            m_f_word = k
    return m_f_word

def most_frequent_letter(content):
    letters = {}
    for letter in content:
        better_letter = letter.lower()
        if better_letter.isalpha():
            if letters.get(better_letter):
                letters[better_letter] +=1
            else:
                letters[better_letter] =1
    maximum, m_f_letter = 0, 0
    for k, v in letters.items():
        if v > maximum:
            maximum = v
            m_f_letter = k
    return m_f_letter